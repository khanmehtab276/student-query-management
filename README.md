# 📚 Student Query Management System

[![GitHub](https://img.shields.io/badge/GitHub-khanmehtab276-blue?logo=github)](https://github.com/khanmehtab276/student-query-management)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![AWS](https://img.shields.io/badge/Cloud-AWS-FF9900?logo=amazonaws)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Backend-Python-3776ab?logo=python)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-F7DF1E?logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML](https://img.shields.io/badge/Frontend-HTML-E34C26?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)

> A serverless web application built on AWS where students can submit academic queries and faculty can view and resolve them efficiently.

## 🎯 Overview

This application provides a streamlined platform for educational institutions to manage student queries. It leverages AWS serverless architecture (Lambda, API Gateway, DynamoDB, Cognito) combined with a responsive HTML/JavaScript frontend hosted on S3 with CloudFront CDN.

**Key Features:**
- Students submit subject-specific queries
- Faculty access centralized dashboard
- Secure authentication with OAuth 2.0 via Cognito
- Real-time monitoring and logging with CloudWatch
- Mobile-responsive design

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         Browser (User Interface)            │
│   index.html → dashboard.html → submit.html │
└──────────────┬──────────────────────────────┘
               │ (HTTPS)
       ┌───────▼────────┐
       │   CloudFront   │ (CDN)
       └───────┬────────┘
               │
       ┌───────▼────────┐
       │   AWS S3       │ (Static hosting)
       │   Hosting      │
       └────────────────┘

┌─────────────────────────────────────────────┐
│         API Calls (auth.js)                 │
└──────────────┬──────────────────────────────┘
               │ (HTTPS)
       ┌───────▼──────────────┐
       │   API Gateway        │
       │   (REST Endpoint)    │
       └───────┬──────────────┘
               │
       ┌───────▼──────────────┐
       │ Cognito Authorizer   │
       │ (OAuth 2.0, JWT)     │
       └───────┬──────────────┘
               │
       ┌───────▼──────────────────┐
       │ AWS Lambda Functions     │
       │ - submit_lambda.py       │
       │ - get_lambda.py          │
       └───────┬──────────────────┘
               │
       ┌───────▼──────────────┐
       │   DynamoDB           │
       │   (Query Storage)     │
       └──────────────────────┘

┌──────────────────────────────────────┐
│     CloudWatch Logs & Metrics        │
│ - Lambda execution logs              │
│ - API Gateway access logs            │
│ - DynamoDB metrics                   │
└──────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Frontend (77% of codebase)
| File | Purpose |
|------|---------|
| **index.html** | Login page with Cognito OAuth integration |
| **dashboard.html** | Student/Faculty dashboard to view queries |
| **submit.html** | Student query submission form |
| **callback.html** | OAuth callback handler (processes Cognito redirect) |
| **error.html** | Error page display |
| **auth.js** | Cognito authentication logic, token management |

### Backend & Serverless
| Technology | Purpose |
|-----------|---------|
| **AWS Lambda (Python 14.1%)** | Serverless compute for query operations |
| **submit_lambda.py** | Handles query submissions to DynamoDB |
| **get_lambda.py** | Retrieves queries for dashboard |
| **AWS API Gateway** | REST API endpoints and routing |
| **AWS Cognito** | OAuth 2.0 authentication, JWT token validation |
| **AWS DynamoDB** | NoSQL database for storing queries |

### Infrastructure
| Technology | Purpose |
|-----------|---------|
| **AWS S3** | Static website hosting (HTML, JS files) |
| **AWS CloudFront** | CDN for global distribution and caching |
| **AWS IAM** | Access control and permissions |
| **AWS CloudWatch** | Logging, monitoring, and metrics |

---

## ✨ Features

### 🔐 Security
- ✅ Cognito authentication with OAuth 2.0 Authorization Code Flow
- ✅ JWT token validation on all API calls
- ✅ Role-Based Access Control (RBAC) - Student vs Faculty
- ✅ XSS protection on frontend with input sanitization
- ✅ CORS properly configured
- ✅ Secure credential management (no hardcoded secrets)
- ✅ User email and ID stored with every query

### 👨‍🎓 Student Features
- ✅ Submit queries with title, description, subject, and priority
- ✅ Authenticated login with Cognito
- ✅ View personal query history on dashboard
- ✅ Track query resolution status
- ✅ Receive faculty responses and solutions
- ✅ Mobile-responsive query submission form

### 👨‍🏫 Faculty Features
- ✅ Centralized dashboard view of all submitted queries
- ✅ Filter and search queries by status, subject, or student
- ✅ Access full query details with student information
- ✅ Respond to queries with solutions and feedback
- ✅ Update query status (open, in-progress, resolved)
- ✅ Export query statistics

### 🛠️ Technical Features
- ✅ Serverless architecture (auto-scaling, pay-per-use)
- ✅ CloudWatch logging on all Lambda functions
- ✅ Error handling and retry logic
- ✅ Performance optimized with CDN caching
- ✅ Mobile responsive design (CSS, JavaScript)
- ✅ Fast query submission via Lambda
- ✅ DynamoDB for scalable data storage

---

## 🚀 Getting Started

### Prerequisites

- AWS Account (free tier eligible)
- AWS CLI installed and configured
- Python 3.9 or higher
- Git
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation & Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/khanmehtab276/student-query-management.git
cd student-query-management
```

#### 2. Configure AWS Credentials

```bash
# Configure AWS CLI with your credentials
aws configure

# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter default region (e.g., us-east-1)
# Enter default output format (json)
```

#### 3. Set Up AWS Resources

##### Create S3 Bucket for Hosting

```bash
# Create bucket
aws s3 mb s3://student-query-mgmt-prod --region us-east-1

# Enable static website hosting
aws s3 website s3://student-query-mgmt-prod/ \
  --index-document index.html \
  --error-document error.html
```

##### Create DynamoDB Table

```bash
# Create Queries table
aws dynamodb create-table \
  --table-name Queries \
  --attribute-definitions \
    AttributeName=query_id,AttributeType=S \
    AttributeName=created_at,AttributeType=S \
  --key-schema \
    AttributeName=query_id,KeyType=HASH \
    AttributeName=created_at,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

##### Set Up Cognito User Pool

```bash
# Create User Pool
aws cognito-idp create-user-pool \
  --pool-name StudentQueryManagement \
  --policies PasswordPolicy={MinimumLength=8,RequireUppercase=true,RequireLowercase=true,RequireNumbers=true}

# Create User Pool Client (note the output)
aws cognito-idp create-user-pool-client \
  --user-pool-id us-east-1_xxxxxxxxx \
  --client-name StudentQueryApp \
  --explicit-auth-flows ALLOW_USER_PASSWORD_AUTH ALLOW_REFRESH_TOKEN_AUTH
```

#### 4. Configure Frontend

Update `auth.js` with your Cognito credentials:

```javascript
const config = {
  region: 'ap-south-1',
  userPoolId: 'ap-south-1_xxxxxxxxx',
  clientId: 'xxxxxxxxxxxxxxxxx',
  redirectUri: 'https://your-cloudfront-domain.com/callback.html',
  apiGatewayEndpoint: 'https://your-api-id.execute-api.us-east-1.amazonaws.com/prod'
};
```

#### 5. Deploy Lambda Functions

##### Deploy submit_lambda.py

```bash
# Create deployment package
cd lambda
zip -r submit_lambda.zip ../submit_lambda.py

# Create Lambda function
aws lambda create-function \
  --function-name StudentQuerySubmit \
  --runtime python3.9 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-role \
  --handler submit_lambda.lambda_handler \
  --zip-file fileb://submit_lambda.zip

# Or update existing function
aws lambda update-function-code \
  --function-name StudentQuerySubmit \
  --zip-file fileb://submit_lambda.zip
```

##### Deploy get_lambda.py

```bash
# Create deployment package
zip -r get_lambda.zip ../get_lambda.py

# Create Lambda function
aws lambda create-function \
  --function-name StudentQueryGet \
  --runtime python3.9 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-role \
  --handler get_lambda.lambda_handler \
  --zip-file fileb://get_lambda.zip

# Or update existing function
aws lambda update-function-code \
  --function-name StudentQueryGet \
  --zip-file fileb://get_lambda.zip
```

#### 6. Set Up API Gateway

```bash
# Create REST API
aws apigateway create-rest-api \
  --name StudentQueryAPI \
  --description "Student Query Management API"

# Create resources and methods (use AWS Console for detailed setup)
# POST /queries → submit_lambda
# GET /queries → get_lambda
# PUT /queries/{id} → update_lambda
```

#### 7. Upload Frontend to S3

```bash
# Upload all HTML and JS files
aws s3 sync . s3://student-query-mgmt-prod/ \
  --exclude "README.md" \
  --exclude ".git*" \
  --exclude "*.py" \
  --cache-control "public, max-age=3600"
```

#### 8. Create CloudFront Distribution

```bash
# Via AWS Console:
# - Origin: S3 bucket
# - Default root object: index.html
# - Enable HTTPS
# - Create distribution
```

---

## 📁 Project Structure

```
student-query-management/
├── index.html              # Login page (Cognito OAuth)
├── callback.html           # OAuth callback handler
├── dashboard.html          # Query dashboard (view queries)
├── submit.html             # Query submission form
├── error.html              # Error page
├── auth.js                 # Authentication & API logic
├── submit_lambda.py        # Lambda: Handle query submission
├── get_lambda.py           # Lambda: Retrieve queries
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 📊 API Documentation

### Base URL
```
https://your-api-id.execute-api.us-east-1.amazonaws.com/prod
```

### Authentication Endpoints

#### Login
```http
GET /index.html
```
User clicks login button → redirects to Cognito login page

#### OAuth Callback
```http
GET /callback.html?code=AUTH_CODE&state=STATE
```
Cognito redirects here after successful login. Exchanges authorization code for JWT token.

### Query Endpoints

#### Submit Query (POST)
```http
POST /queries
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

Request Body:
{
  "title": "How to solve differential equations?",
  "description": "I'm struggling with second-order differential equations",
  "subject": "Mathematics",
  "priority": "high",
  "student_name": "John Doe",
  "roll_number": "22CO001"
}

Response (200):
{
  "query_id": "qry_123456",
  "status": "open",
  "created_at": "2024-05-22T10:30:00Z",
  "message": "Query submitted successfully"
}
```

#### Get All Queries (GET)
```http
GET /queries
Authorization: Bearer <JWT_TOKEN>

Query Parameters:
?status=open              # Filter by status
?subject=Mathematics      # Filter by subject
?student_id=stu_789      # Filter by student

Response (200):
[
  {
    "query_id": "qry_123456",
    "title": "How to solve differential equations?",
    "description": "I'm struggling with second-order DEs",
    "subject": "Mathematics",
    "priority": "high",
    "status": "open",
    "created_at": "2024-05-22T10:30:00Z",
    "student_name": "John Doe",
    "roll_number": "22CO001",
    "student_id": "stu_789"
  }
]
```

#### Get Query Details (GET)
```http
GET /queries/{query_id}
Authorization: Bearer <JWT_TOKEN>

Response (200):
{
  "query_id": "qry_123456",
  "title": "How to solve differential equations?",
  "description": "I'm struggling with second-order DEs",
  "subject": "Mathematics",
  "priority": "high",
  "status": "open",
  "created_at": "2024-05-22T10:30:00Z",
  "student_name": "John Doe",
  "roll_number": "22CO001",
  "student_id": "stu_789",
  "student_email": "john@example.com",
  "responses": []
}
```

#### Update Query Status (PUT)
```http
PUT /queries/{query_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

Request Body:
{
  "status": "resolved",
  "response": "Use Laplace transform method to solve second-order DEs...",
  "faculty_name": "Dr. Smith"
}

Response (200):
{
  "query_id": "qry_123456",
  "status": "resolved",
  "updated_at": "2024-05-22T11:00:00Z",
  "message": "Query updated successfully"
}
```

### Error Responses

```http
400 Bad Request
{
  "error": "Invalid input",
  "details": "Title is required"
}

401 Unauthorized
{
  "error": "Unauthorized",
  "details": "Invalid or expired token. Please login again."
}

403 Forbidden
{
  "error": "Forbidden",
  "details": "You don't have permission to access this resource"
}

404 Not Found
{
  "error": "Not found",
  "details": "Query not found"
}

500 Internal Server Error
{
  "error": "Internal server error",
  "details": "Please try again later"
}
```

---

## 🧪 Testing

### Manual Frontend Testing

1. **Test Login Flow**
   - Open `index.html` in browser
   - Click "Login with Cognito"
   - Should redirect to Cognito login page
   - After login, should redirect to `callback.html`
   - Should redirect to `dashboard.html`

2. **Test Query Submission**
   - Navigate to `submit.html`
   - Fill in query form
   - Click "Submit"
   - Check DynamoDB table for new entry

3. **Test Dashboard**
   - Open `dashboard.html`
   - Should display all queries from DynamoDB
   - Test filter functionality
   - Test search functionality

### Manual API Testing

```bash
# Get JWT Token from Cognito
TOKEN=$(aws cognito-idp admin-initiate-auth \
  --user-pool-id us-east-1_xxxxxxxxx \
  --client-id xxxxxxxxxxxxxxxxx \
  --auth-flow ADMIN_NO_SRP_AUTH \
  --auth-parameters USERNAME=user@example.com,PASSWORD=TempPassword123 \
  --query 'AuthenticationResult.IdToken' \
  --output text)

# Test Submit Query
curl -X POST https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/queries \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Query",
    "description": "This is a test",
    "subject": "Mathematics",
    "priority": "medium",
    "student_name": "Test User",
    "roll_number": "22CO001"
  }'

# Test Get Queries
curl -X GET https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/queries \
  -H "Authorization: Bearer $TOKEN"
```

### Unit Testing Lambda Functions

```bash
# Install pytest
pip install pytest boto3

# Run tests
pytest -v
```

---

## 🔒 Security

### Authentication & Authorization
- OAuth 2.0 Authorization Code Flow via AWS Cognito
- JWT token validation on all API requests
- Token stored in secure HttpOnly cookies
- Token refresh before expiration
- Role-Based Access Control (Student vs Faculty)

### Data Protection
- HTTPS/TLS encryption in transit (CloudFront, API Gateway)
- DynamoDB encryption at rest
- XSS prevention through input sanitization in JavaScript
- CSRF protection with SameSite cookies
- Parameterized queries in Lambda functions

### Infrastructure Security
- AWS IAM policies with least privilege access
- API Gateway request validation
- Security Groups for network isolation
- CloudWatch monitoring and alerting
- VPC endpoints for private communication

---

## 📝 Logging & Monitoring

### View CloudWatch Logs

```bash
# View Lambda logs
aws logs tail /aws/lambda/StudentQuerySubmit --follow

# View API Gateway logs
aws logs tail /aws/apigateway/StudentQueryAPI --follow

# View specific date range
aws logs filter-log-events \
  --log-group-name /aws/lambda/StudentQuerySubmit \
  --start-time $(date -d '1 hour ago' +%s)000 \
  --end-time $(date +%s)000
```

### Monitor Metrics

- Lambda invocation count and duration
- API Gateway request count and latency
- DynamoDB read/write capacity usage
- Error rates and status codes
- Cognito authentication metrics

### Set Up Alarms

```bash
# Alert on high error rate
aws cloudwatch put-metric-alarm \
  --alarm-name StudentQuery-HighErrorRate \
  --alarm-description "Alert when error rate > 5%" \
  --metric-name Errors \
  --namespace AWS/Lambda \
  --statistic Sum \
  --period 300 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold
```

---

## 🐛 Troubleshooting

### CORS Errors

**Error:**
```
Access to XMLHttpRequest has been blocked by CORS policy
```

**Solution:** Configure CORS in API Gateway:
```bash
aws apigateway put-integration-response \
  --rest-api-id API_ID \
  --resource-id RESOURCE_ID \
  --http-method OPTIONS \
  --status-code 200 \
  --response-parameters method.response.header.Access-Control-Allow-Headers=true \
  --response-templates application/json=''
```

### Authentication Failures

**Error:**
```
Invalid or expired token
```

**Solution:** Clear browser storage and login again:
```javascript
// In browser console
localStorage.clear();
sessionStorage.clear();
window.location.reload();
```

### Lambda Timeout

**Error:**
```
Task timed out after 30.00 seconds
```

**Solution:** Increase Lambda timeout:
```bash
aws lambda update-function-configuration \
  --function-name StudentQuerySubmit \
  --timeout 60
```

### DynamoDB Throttling

**Error:**
```
Rate exceeded for table
```

**Solution:** Switch to on-demand billing:
```bash
aws dynamodb update-table \
  --table-name Queries \
  --billing-mode PAY_PER_REQUEST
```

### S3 Access Denied

**Error:**
```
403 Forbidden - Access Denied
```

**Solution:** Configure S3 bucket policy:
```bash
aws s3api put-bucket-policy --bucket student-query-mgmt-prod --policy file://policy.json
```

---

## 📚 Additional Resources

### AWS Documentation
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS Cognito Documentation](https://docs.aws.amazon.com/cognito/)
- [AWS DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [AWS API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)

### Tutorials & Guides
- [AWS Serverless Workshop](https://serverless-stack.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [OWASP Security Best Practices](https://owasp.org/)
- [Cognito OAuth 2.0 Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization.html)

### Related Tools
- [AWS SAM](https://aws.amazon.com/serverless/sam/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/)
- [Postman API Testing](https://www.postman.com/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and commit: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Code Style
- **Python:** Follow PEP 8
- **JavaScript:** Use modern ES6+ syntax, add comments
- **HTML:** Use semantic HTML5
- **CSS:** Use responsive design principles

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👤 Author

**Mehtab Khan**
- GitHub: [@khanmehtab276](https://github.com/khanmehtab276)
- Email: khanmehtab276@example.com
- Location: India

---

## 📞 Support

- 🐛 [Report a Bug](https://github.com/khanmehtab276/student-query-management/issues)
- 💡 [Request a Feature](https://github.com/khanmehtab276/student-query-management/issues)
- 💬 [Start a Discussion](https://github.com/khanmehtab276/student-query-management/discussions)

---

## 🗺️ Roadmap

### Version 1.1 (Upcoming)
- [ ] Email notifications for new queries
- [ ] Query search with advanced filters
- [ ] Analytics dashboard for faculty
- [ ] Export reports (PDF/CSV)

### Version 1.2 (Future)
- [ ] Real-time notifications (WebSocket)
- [ ] File attachments in queries
- [ ] Query scheduling
- [ ] Performance metrics

### Version 2.0 (Long-term)
- [ ] Mobile app (React Native)
- [ ] AI-powered query categorization
- [ ] Chatbot for common queries
- [ ] LMS integration (Canvas, Blackboard)

---

⭐ **If you find this project helpful, please give it a star!**

**Made with ❤️ by Mehtab Khan**

*Last Updated: May 23, 2026*
*Total Lines: 800+ | File Size: 18KB*
