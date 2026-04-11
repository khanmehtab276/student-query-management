# Student Query Management System

A serverless web application built on AWS where students can raise 
doubts and faculty can view them.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Hosting: AWS S3 + CloudFront
- Auth: AWS Cognito (OAuth 2.0 Authorization Code Flow)
- API: AWS API Gateway
- Backend: AWS Lambda (Python)
- Database: AWS DynamoDB

## Features
- Cognito authentication with JWT tokens
- Students can submit queries with their name, roll number and subject
- Faculty can view all submitted queries on the dashboard
- User email and ID stored with every query
- CloudWatch logging on all Lambda functions
- XSS protection on frontend
- Proper CORS configuration

## Architecture
Browser → CloudFront → S3 (HTML/JS)
Browser → API Gateway → Cognito Authorizer → Lambda → DynamoDB
