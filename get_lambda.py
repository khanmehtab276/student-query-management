import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contact-form')


def convert_decimal(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


def lambda_handler(event, context):
    # Log full event for CloudWatch debugging
    print("EVENT:", json.dumps(event))

    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers(),
            "body": json.dumps({"message": "CORS OK"})
        }

    try:
        # Check for ?mine=true query param
        # If present, return only the logged-in user's queries
        # If absent, return all queries (current behaviour — faculty view)
        params   = event.get("queryStringParameters") or {}
        mine_only = params.get("mine") == "true"

        if mine_only:
            # Get user_id from Cognito Authorizer claims
            # (Only works if you add Cognito Authorizer to GET endpoint too)
            claims  = event.get("requestContext", {}).get("authorizer", {}).get("claims", {})
            user_id = claims.get("sub")

            if not user_id:
                return response(401, {"error": "Unauthorized"})

            # Filter scan by user_id
            result = table.scan(
                FilterExpression="user_id = :uid",
                ExpressionAttributeValues={":uid": user_id}
            )
        else:
            # Return all queries (existing behaviour)
            result = table.scan()

        data = result.get('Items', [])
        print(f"FETCHED {len(data)} items, mine_only={mine_only}")  # CloudWatch log

        return response(200, {
            "count": len(data),
            "data": data
        })

    except Exception as e:
        print("ERROR:", str(e))
        return response(500, {"error": "Internal server error"})


def response(status, body):
    return {
        "statusCode": status,
        "headers": cors_headers(),
        "body": json.dumps(body, default=convert_decimal)
    }


def cors_headers():
    return {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin":  "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "OPTIONS,GET"
    }