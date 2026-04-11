import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('contact-form')


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
        body = json.loads(event.get('body', '{}'))

        name    = body.get("name", "").strip()
        roll    = body.get("roll", "").strip()
        subject = body.get("subject", "").strip()
        query   = body.get("query", "").strip()

        if not name or not roll or not subject or not query:
            return response(400, {"error": "All fields are required"})

        if len(name) > 100 or len(roll) > 50 or len(subject) > 200 or len(query) > 2000:
            return response(400, {"error": "Input too long"})

        # Extract user info injected by Cognito Authorizer
        # API Gateway verifies the JWT and passes claims automatically
        claims  = event.get("requestContext", {}).get("authorizer", {}).get("claims", {})
        user_id = claims.get("sub", "unknown")
        email   = claims.get("email", "unknown")

        item = {
            "id":        str(uuid.uuid4()),
            "user_id":   user_id,   # Cognito user ID (unique per user)
            "email":     email,     # User's email from token
            "name":      name,
            "roll":      roll,
            "subject":   subject,
            "query":     query,
            "timestamp": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        print("SAVED ITEM:", json.dumps(item))  # CloudWatch log

        return response(200, {
            "message": "Query submitted successfully",
            "data": item
        })

    except Exception as e:
        print("ERROR:", str(e))
        return response(500, {"error": "Internal server error"})


def response(status, body):
    return {
        "statusCode": status,
        "headers": cors_headers(),
        "body": json.dumps(body)
    }


def cors_headers():
    return {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin":  "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    }