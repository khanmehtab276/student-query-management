# 📚 Student Query Management System

[![GitHub](https://img.shields.io/badge/GitHub-khanmehtab276-blue?logo=github)](https://github.com/khanmehtab276/student-query-management)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![AWS](https://img.shields.io/badge/Cloud-AWS-FF9900?logo=amazonaws)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Backend-Python-3776ab?logo=python)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-F7DF1E?logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

> A serverless web application built on AWS where students can submit academic queries and faculty can view, manage, and resolve them efficiently.

## 🎯 Overview

This application provides a streamlined platform for educational institutions to manage student queries and doubts. It leverages AWS serverless architecture for scalability, security, and cost-effectiveness.

**Key Features:**
- Students submit subject-specific queries
- Faculty access centralized dashboard
- Secure authentication with OAuth 2.0
- Real-time monitoring and logging
- Mobile-responsive design

---

## 🏗️ Architecture

```
User Interface (Frontend)
        ↓
   CloudFront (CDN)
        ↓
    S3 Hosting
    (HTML/CSS/JS)
        ↓
   API Gateway
        ↓
  Cognito Auth
   JWT Validation
        ↓
  AWS Lambda
   (Python)
        ↓
  DynamoDB
   (Database)
        ↓
 CloudWatch
   (Logs)
```

## 🛠️ Tech Stack

### Frontend (77% of codebase)
- **HTML5** - Semantic markup and structure
- **CSS3** - Responsive styling and animations
- **JavaScript** (8.9%) - Client-side interactivity and API calls

### Backend & Serverless
- **AWS Lambda** (Python 14.1%) - Serverless compute for business logic
- **AWS API Gateway** - REST API endpoints and routing
- **AWS Cognito** - OAuth 2.0 authentication and authorization
- **AWS DynamoDB** - NoSQL database for storing queries and user data

### Infrastructure
- **AWS S3** - Static website hosting
- **AWS CloudFront** - Content delivery network (CDN) for global distribution
- **AWS IAM** - Access control and permissions
- **AWS CloudWatch** - Logging and monitoring

---

## ✨ Features

### 🔐 Security
- ✅ Cognito authentication with JWT tokens
- ✅ OAuth 2.0 Authorization Code Flow
- ✅ Role-Based Access Control (RBAC)
- ✅ XSS protection on frontend
- ✅ CORS properly configured
- ✅ Secure credential management

### 👨‍🎓 Student Features
- ✅ Submit queries with title, description, subject, and priority
- ✅ View query submission history
- ✅ Track query resolution status
- ✅ Receive faculty responses and solutions
- ✅ Manage user profile information

### 👨‍🏫 Faculty Features
- ✅ View all submitted queries on centralized dashboard
- ✅ Filter queries by subject, status, date, or student
- ✅ Access full query details with student information
- ✅ Respond to queries with solutions and feedback
- ✅ Update query status (open, in-progress, resolved)
- ✅ Export query statistics and reports

### 🛠️ Technical Features
- ✅ Serverless architecture (auto-scaling, pay-per-use)
- ✅ CloudWatch logging on all Lambda functions
- ✅ User email and ID stored with every query
- ✅ Error handling and retry logic
- ✅ Performance optimized with CDN caching
- ✅ Mobile responsive design

---

## 🚀 Getting Started

### Prerequisites

- AWS Account (free tier eligible)
- AWS CLI installed and configured
- Python 3.9 or higher
- Git
- Node.js (optional, for development tools)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/khanmehtab276/student-query-management.git
cd student-query-management
```

#### 2. Set Up AWS Credentials

```bash
# Configure AWS CLI with your credentials
aws configure

# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter default region (e.g., us-east-1)
# Enter default output format (json)
```

#### 3. Set Up Python Environment (for Lambda development)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit with your AWS configuration
nano .env  # or use your preferred editor
```

**Example .env:**
```bash
AWS_REGION=us-east-1
COGNITO_USER_POOL_ID=us-east-1_xxxxxxxxx
COGNITO_CLIENT_ID=xxxxxxxxxxxxxxxxx
COGNITO_DOMAIN=your-domain
APP_NAME=StudentQueryManagement
ENV=development
DEBUG=true
```

---

## 📦 Project Structure

```
student-query-management/
├── frontend/                          # Frontend files (77%)
│   ├── index.html                    # Login page
│   ├── student-dashboard.html        # Student interface
│   ├── faculty-dashboard.html        # Faculty interface
│   ├── admin-panel.html              # Admin interface (optional)
│   ├── css/
│   │   ├── styles.css               # Main styling
│   │   ├── responsive.css           # Mobile responsive design
│   │   └── animations.css           # UI animations
│   └── js/
│       ├── auth.js                  # Cognito authentication
│       ├── api.js                   # API Gateway calls
│       ├── utils.js                 # Helper functions
│       └── dashboard.js             # Dashboard logic
│
├── lambda_functions/                  # Backend (14.1%)
│   ├── submit_query/
│   │   ├── lambda_function.py       # Handle query submissions
│   │   └── requirements.txt         # Dependencies
│   ├── get_queries/
│   │   ├── lambda_function.py       # Retrieve queries
│   │   └── requirements.txt
│   ├── update_query/
│   │   ├── lambda_function.py       # Update query status
│   │   └── requirements.txt
│   └── authorizer/
│       ├── lambda_function.py       # JWT token validation
│       └── requirements.txt
│
├── infrastructure/                    # Infrastructure as Code
│   ├── terraform/                   # Terraform files (optional)
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── cloudformation/              # CloudFormation templates (optional)
│       └── template.yaml
│
├── tests/                             # Test files
│   ├── unit/
│   │   └── test_lambda.py           # Lambda function tests
│   └── integration/
│       └── test_api.py              # API integration tests
│
├── .env.example                       # Example environment file
├── .env                               # Local environment variables (git ignored)
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
├── README.md                          # This file
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                            # MIT License
└── CHANGELOG.md                       # Version history
```

---

## 🌐 Deployment

### Deploy Frontend to AWS S3 & CloudFront

#### 1. Create S3 Bucket

```bash
# Create bucket for static hosting
aws s3 mb s3://student-query-mgmt-prod --region us-east-1

# Enable static website hosting
aws s3 website s3://student-query-mgmt-prod/ \
  --index-document index.html \
  --error-document index.html
```

#### 2. Upload Frontend Files

```bash
# Sync frontend files to S3
aws s3 sync ./frontend s3://student-query-mgmt-prod/ \
  --delete \
  --cache-control "public, max-age=3600"
```

#### 3. Create CloudFront Distribution (via AWS Console)

- S3 Origin: `student-query-mgmt-prod.s3.amazonaws.com`
- Enable HTTPS only
- Set index.html as default root object
- Configure CORS headers

### Deploy Backend Lambda Functions

#### Option 1: Manual Deployment

```bash
# Navigate to Lambda function
cd lambda_functions/submit_query

# Install dependencies
pip install -r requirements.txt -t .

# Create deployment package
zip -r lambda-function.zip .

# Upload to AWS Lambda
aws lambda update-function-code \
  --function-name StudentQuerySubmit \
  --zip-file fileb://lambda-function.zip

# Verify deployment
aws lambda get-function --function-name StudentQuerySubmit
```

#### Option 2: Using AWS SAM (Recommended)

```bash
# Build application
sam build

# Deploy with guided setup
sam deploy --guided

# Or deploy to existing stack
sam deploy
```

#### Option 3: Using Terraform

```bash
cd infrastructure/terraform

# Initialize Terraform
terraform init

# Plan deployment
terraform plan

# Apply changes
terraform apply
```

### Deploy DynamoDB Tables

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
  --billing-mode PAY_PER_REQUEST

# Create Users table
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions \
    AttributeName=user_id,AttributeType=S \
  --key-schema \
    AttributeName=user_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

### Set Up Cognito User Pool

```bash
# Create User Pool
aws cognito-idp create-user-pool \
  --pool-name StudentQueryManagement \
  --policies PasswordPolicy={MinimumLength=8,RequireUppercase=true,RequireLowercase=true,RequireNumbers=true,RequireSymbols=false}

# Create User Pool Client
aws cognito-idp create-user-pool-client \
  --user-pool-id us-east-1_xxxxxxxxx \
  --client-name StudentQueryApp \
  --explicit-auth-flows ALLOW_USER_PASSWORD_AUTH ALLOW_REFRESH_TOKEN_AUTH
```

---

## 📊 API Documentation

### Authentication Endpoints

#### Login
```http
GET /auth/login
```
Redirects user to Cognito login page.

#### Logout
```http
GET /auth/logout
```
Clears session and redirects to login page.

### Query Endpoints

#### Submit New Query
```http
POST /api/queries
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

Request Body:
{
  "title": "How to solve differential equations?",
  "description": "I'm struggling with second-order DEs",
  "subject": "Mathematics",
  "priority": "high"
}

Response (200):
{
  "query_id": "qry_123456",
  "status": "open",
  "created_at": "2024-05-22T10:30:00Z",
  "student_id": "stu_789"
}
```

#### Get All Queries
```http
GET /api/queries?status=open&subject=Mathematics
Authorization: Bearer <JWT_TOKEN>

Response (200):
[
  {
    "query_id": "qry_123456",
    "title": "How to solve differential equations?",
    "status": "open",
    "created_at": "2024-05-22T10:30:00Z",
    "student_name": "John Doe",
    "student_roll": "22CO001",
    "subject": "Mathematics"
  }
]
```

#### Get Query Details
```http
GET /api/queries/{query_id}
Authorization: Bearer <JWT_TOKEN>

Response (200):
{
  "query_id": "qry_123456",
  "title": "How to solve differential equations?",
  "description": "I'm struggling with second-order DEs",
  "status": "open",
  "priority": "high",
  "created_at": "2024-05-22T10:30:00Z",
  "student_id": "stu_789",
  "student_name": "John Doe",
  "student_email": "john@example.com",
  "subject": "Mathematics",
  "responses": []
}
```

#### Update Query Status
```http
PUT /api/queries/{query_id}
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

Request Body:
{
  "status": "resolved",
  "response": "Use Laplace transform method..."
}

Response (200):
{
  "query_id": "qry_123456",
  "status": "resolved",
  "updated_at": "2024-05-22T11:00:00Z"
}
```

#### Delete Query
```http
DELETE /api/queries/{query_id}
Authorization: Bearer <JWT_TOKEN>

Response (204): No Content
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
  "details": "Invalid or expired token"
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

### Unit Tests

```bash
# Run all unit tests
pytest tests/unit/ -v

# Run specific test file
pytest tests/unit/test_lambda.py -v

# Run with coverage report
pytest --cov=lambda_functions tests/unit/
```

### Integration Tests

```bash
# Set test environment
export ENV=test
export AWS_REGION=us-east-1

# Run integration tests
pytest tests/integration/ -v
```

### Manual API Testing

```bash
# Test Submit Query
curl -X POST http://localhost:3000/api/queries \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Query",
    "description": "This is a test",
    "subject": "Mathematics",
    "priority": "medium"
  }'

# Test Get Queries
curl -X GET http://localhost:3000/api/queries \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

---

## 🔒 Security

### Authentication & Authorization
- OAuth 2.0 Authorization Code Flow via AWS Cognito
- JWT token validation on all API requests
- Role-Based Access Control (RBAC) for Students vs Faculty
- Secure token storage with HttpOnly cookies
- Token expiration and refresh mechanisms

### Data Protection
- HTTPS/TLS encryption in transit
- DynamoDB encryption at rest
- XSS prevention through input sanitization
- CSRF protection with SameSite cookies
- Parameterized queries to prevent injection attacks

### Infrastructure Security
- AWS IAM policies with least privilege access
- API Gateway request validation
- Security Groups for network isolation
- CloudWatch monitoring and alerting
- Audit logging of all actions

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
- Cold start times

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

**Solution:**
Check and update API Gateway CORS configuration:
```bash
aws apigateway get-stage \
  --rest-api-id YOUR_API_ID \
  --stage-name prod
```

### Authentication Failures

**Error:**
```
Invalid or expired token
```

**Solution:**
Verify Cognito configuration:
```bash
aws cognito-idp describe-user-pool \
  --user-pool-id us-east-1_xxxxxxxxx
```

### Lambda Timeout

**Error:**
```
Task timed out after 30.00 seconds
```

**Solution:**
Increase Lambda timeout:
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

**Solution:**
Switch to on-demand billing:
```bash
aws dynamodb update-table \
  --table-name Queries \
  --billing-mode PAY_PER_REQUEST
```

---

## 📚 Additional Resources

### AWS Documentation
- [Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Cognito Documentation](https://docs.aws.amazon.com/cognito/)
- [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)

### Tutorials & Guides
- [AWS Serverless Workshop](https://serverless-stack.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [OWASP Security Best Practices](https://owasp.org/)

### Related Tools
- [AWS SAM](https://aws.amazon.com/serverless/sam/)
- [Serverless Framework](https://www.serverless.com/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/)

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
- **JavaScript:** Use ESLint
- **HTML/CSS:** Follow W3C standards

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mehtab Khan**
- GitHub: [@khanmehtab276](https://github.com/khanmehtab276)
- Email: khanmehtab276@example.com

---

## 📞 Support

- 🐛 [Report a Bug](https://github.com/khanmehtab276/student-query-management/issues)
- 💡 [Request a Feature](https://github.com/khanmehtab276/student-query-management/issues)
- 💬 [Start a Discussion](https://github.com/khanmehtab276/student-query-management/discussions)

---

⭐ **If you find this project helpful, please give it a star!**

**Made with ❤️ by Mehtab Khan**

*Last Updated: May 22, 2024*
