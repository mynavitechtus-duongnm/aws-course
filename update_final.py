#!/usr/bin/env python3
"""Update all remaining lessons - final batch"""

with open('data.js', 'r') as f:
    content = f.read()

# Final batch of summaries
final_lessons = {
    "Introduction to Amazon Simple Storage Service (S3)": "Gioi thieu S3 object storage.",
    "Public your Bucket Object": "Lam object public trong S3.",
    "S3 Object - S3 Object Properties": "Tim hieu S3 Object.",
    "How to Redirect in S3 Static Website": "Cau hinh redirect trong S3.",
    "How to Change Prefix in Static Website S3": "Redirect voi prefix trong S3.",
    "S3 Accelerated Transfer": "Su dung S3 Transfer Acceleration.",
    "Same/Cross Region Replication": "S3 Replication giua regions.",
    "Cost Efficiency and Performance with AWS Intelligent Tiering": "S3 Intelligent-Tiering.",
    "What is CORS": "Cau hinh CORS cho S3.",
    "What is Presigned URL": "Su dung Presigned URL.",
    "Securing Your AWS S3 Data": "Bao mat S3 data.",
    "What is Cloudfront": "Gioi thieu CloudFront.",
    "AWS CloudFront Invalidation": "CloudFront cache invalidation.",
    "How to make EC2/ALB Instance Accessible from CloudFront Only": "Bao mat origin voi CloudFront.",
    "CloudFront with S3": "CloudFront voi S3 private bucket.",
    "CloudFront Path Based routing": "CloudFront path-based routing.",
    "CloudFront Custom Error Page": "Custom error pages trong CloudFront.",
    "How to Control Access to Your Content Based on Country": "Geo-restriction trong CloudFront.",
    "How to Disable CloudFront Distribution": "Xoa CloudFront distribution.",
    "What/Why is AWS Roles": "Su dung IAM Roles.",
    "What/Why is CloudShell": "AWS CloudShell.",
    "How to use AWS CLI": "Su dung AWS CLI.",
    "AWS CLI Handle Multiple AWS Accounts": "Quan ly nhieu AWS accounts.",
    "AWS Multi Factor Authentication": "Kich hoat MFA.",
    "Access EC2 Instance From Windows Machine": "Ket noi EC2 tu Windows.",
    "Bootstrap Script in EC2 Instance": "User Data script.",
    "Instance Metadata With UserData": "EC2 Instance Metadata.",
    "Attach Elastic/Static IP": "Gan Elastic IP.",
    "Detach Elastic/Static IP": "Giai phong Elastic IP.",
    "Elastic Block Storage (EBS)": "Gioi thieu EBS.",
    "Create First Elastic Block Storage Vol": "Tao EBS volume.",
    "Detach an EBS volume": "Detach EBS volume.",
    "Resize EBS Volume": "Resize EBS volume.",
    "How to Resize ROOT EBS Volume": "Resize root EBS volume.",
    "Attach One EBS Volume to Multiple EC2 Instance": "EBS Multi-Attach.",
    "Type of EBS Volumes": "Cac loai EBS volumes.",
    "Snapshot Overview": "Gioi thieu EBS Snapshots.",
    "Create First Snapshot": "Tao EBS snapshot.",
    "Automate EBS Volume Backup": "Tu dong hoa backup voi Lifecycle Manager.",
    "Snapshot and AMI Recycle Bin": "Recycle Bin cho snapshots.",
    "Copy Snapshot From One Region to Another": "Copy snapshot across regions.",
    "Encrypt the EBS Volume": "Ma hoa EBS volume.",
    "Delete EBS Snapshot": "Xoa EBS snapshot.",
    "AWS AMI": "Amazon Machine Images.",
    "Share Your AMI": "Share AMI voi account khac.",
    "What is AWS region": "AWS Regions.",
    "What/Why is AWS Availability Zones": "Availability Zones.",
    "What/Why is Local Zones": "Local Zones.",
    "Create AWS Account": "Tao AWS Account.",
    "Create First EC2 Instance": "Tao EC2 instance dau tien.",
    "Access EC2 Instance From Linux Machine": "Ket noi EC2 tu Linux.",
    "Install Nginx in EC2 Instance": "Cai dat Nginx.",
    "AWS Security Group": "Security Groups.",
    "AWS EC2 Instance Type": "EC2 Instance Types.",
    "How Aws Charge": "AWS pricing.",
    "AWS Pricing": "AWS pricing models.",
    "Create Windows Instance In AWS": "Tao Windows EC2 instance.",
    "Access Windows Instance From Linux Machine": "Ket noi Windows tu Linux.",
    "Elastic Load Balancer in AWS": "Gioi thieu ELB.",
    "EC2 Instance Accessible by LoadBalancer Only": "EC2 chi qua Load Balancer.",
    "Delete Classic Load Balancer": "Xoa Classic Load Balancer.",
    "Application Load Balancer": "Application Load Balancer.",
    "Path Base Routing in Application Load Balancer": "ALB path-based routing.",
    "How Get Client IP address": "Lay client IP voi ALB.",
    "Stickiness And Custom Page Routing": "Sticky sessions trong ALB.",
    "Network Load Balancer": "Network Load Balancer.",
    "Auto Scaling in Action": "Auto Scaling policies.",
    "Auto Scaling With Load Balancer": "ASG voi Load Balancer.",
    "Enable Termination Protection": "Termination protection.",
    "How to create Reserve Instance": "Reserved Instances.",
    "How to attach multiple NIC": "Multiple ENIs.",
    "Simple Notification Service - Send First Notification": "Gui notification dau tien voi SNS.",
    "Simple Notification Service - Send Mobile SMS Notification": "Gui SMS voi SNS.",
    "Amazon Simple Email Service": "Amazon SES.",
    "Email Service - Got SES Production Access": "SES production access.",
    "Amazon RDS - What is Read Replica": "RDS Read Replicas.",
    "Amazon RDS - AWS Aurora Database": "Amazon Aurora.",
    "Amazon RDS - Aurora Endpoints": "Aurora Endpoints.",
    "Amazon DynamoDB - Where I am utilizing DynamoDB": "DynamoDB use cases.",
    "Amazon DynamoDB - Scan And Query": "DynamoDB Query vs Scan.",
    "Amazon DynamoDB - Local Secondary Index": "DynamoDB Local Secondary Index.",
    "Amazon DynamoDB - Global Secondary Index": "DynamoDB Global Secondary Index.",
    "Amazon DynamoDB - Point in Time Recovery": "DynamoDB PITR.",
    "Amazon DynamoDB - DynamoDB Global Tables": "DynamoDB Global Tables.",
    "Amazon DynamoDB - Export DynamoDB Data to S3": "Export DynamoDB to S3.",
    "Amazon DynamoDB - Import Data in DynamoDB From S3": "Import S3 to DynamoDB.",
    "Amazon DynamoDB - How to Delete table": "Xoa DynamoDB table.",
    "What is Serverless": "Serverless architecture.",
    "AWS Tutorial 172": "Lambda function dau tien.",
    "AWS Tutorial 173": "Lambda event object.",
    "AWS Tutorial 174": "Lambda URLs.",
    "AWS Tutorial 175": "Lambda events.",
    "AWS Tutorial 176": "Lambda cold start.",
    "AWS Tutorial 177": "Lambda environment variables.",
    "AWS Tutorial 178": "Lambda configuration.",
    "AWS Tutorial 179": "Lambda context object.",
    "AWS Tutorial 180": "Lambda sync vs async.",
    "AWS Tutorial 181": "Lambda DLQ.",
    "AWS Tutorial 181.2": "Lambda DLQ usage.",
    "AWS Tutorial 182": "Lambda S3 trigger.",
    "AWS Tutorial 183": "Lambda ALB trigger.",
    "AWS Tutorial 184": "Lambda ALB cleanup.",
    "Can we Change AWS Lambda Function": "Lambda function name.",
    "How to Write, Upload, and Use AWS Lambda Code from an S3 Bucket": "Lambda from S3.",
    "How to use external libraries in Lambda Function": "Lambda external libraries.",
    "How to use layers in Lambda Function": "Lambda layers.",
    "AWS Tutorial 189": "Lambda shared layers.",
    "AWS Tutorial 190": "Lambda versions.",
    "AWS Tutorial 191": "Lambda aliases.",
    "AWS Tutorial 192": "Lambda IAM roles.",
    "AWS Tutorial 193": "Lambda in VPC.",
    "AWS Tutorial 195": "Lambda test events.",
    "AWS Tutorial 196": "Lambda RDS connection.",
    "AWS Tutorial 203": "Lambda concurrency.",
    "AWS Lambda Destinations": "Lambda Destinations.",
    "What's the REAL Purpose of API Gateway": "API Gateway overview.",
    "AWS API Gateway with HTTP Integrations": "API Gateway HTTP.",
    "AWS API Gateway Rest API Integrations": "API Gateway REST.",
    "AWS API Gateway - Rest API": "API Gateway resources.",
    "How to Integrate AWS API Gateway with AWS Lambda": "API Gateway Lambda integration.",
    "Create Dummy APIs with API Gateway": "Mock integration.",
    "API Gateway + DynamoDB Direct Integration": "API Gateway DynamoDB.",
    "Path & Query String Parameters in API Gateway": "API Gateway parameters.",
    "Headers in AWS API Gateway": "API Gateway headers.",
    "How Add Validation on API Gateway Level": "API Gateway validation.",
    "Modify Requests Before Reach the Backend": "Request transformation.",
    "How to modify Request Body Before Reach Backend": "Response transformation.",
    "Integration Request in API Gateway with AWS Lambda": "Integration request.",
    "Your Lambda Works": "Method response.",
    "Transform Lambda Responses in API Gateway": "Response transformation.",
    "How to Authenticate API Gateway Using IAM Roles": "IAM auth.",
    "How to Protect API Gateway Using API Keys": "API keys.",
    "AWS Custom Authorizer Tutorial": "Custom authorizer.",
    "Pass User Info from Custom Authorizer to Lambda": "Authorizer context.",
    "Zero Downtime API Updates with AWS Lambda Alias": "Zero downtime deployment.",
    "AWS API Gateway Canary Deployment": "Canary deployment.",
    "How to Map Custom Domain to AWS API Gateway": "Custom domain.",
    "AWS Cognito": "Cognito overview.",
    "AWS Cognito Token Flow Explained": "Cognito tokens.",
    "Customize AWS Cognito Hosted UI with CSS": "Cognito UI customization.",
    "Move AWS Cognito Hosted UI to Custom Domain": "Cognito custom domain.",
    "AWS Cognito: User Profiles, Groups": "Cognito user profiles.",
    "Send Emails from Custom Domain using AWS Cognito": "Cognito SES integration.",
    "AWS ECS Tutorial for Beginners": "ECS overview.",
    "How to Create ECS Cluster with Managed Instance": "ECS cluster.",
    "AWS ECS Tutorial for Beginners | Task Definition": "ECS task definition.",
    "How To Create a Service on ECS Cluster": "ECS service."
}

import re

count = 0
for title_part, summary in final_lessons.items():
    # Find lesson containing this title part
    pattern = rf'summary: "Bài học về .*{re.escape(title_part)}.* trong khóa học AWS\."'
    matches = re.findall(pattern, content)
    
    for match in matches:
        # Extract the full title
        title_match = re.search(r'Bài học về (.+) trong khóa học AWS\.', match)
        if title_match:
            full_title = title_match.group(1)
            new_summary = f'summary: "{summary}"'
            
            content = content.replace(match, new_summary, 1)
            
            # Also update explanation
            old_exp = f'explanation: `<p>Bài học về {full_title}. Xem video để hiểu chi tiết.</p>`'
            new_exp = f'explanation: `<p>{summary} Xem video de hieu chi tiet.</p>`'
            if old_exp in content:
                content = content.replace(old_exp, new_exp, 1)
                count += 1
                print(f"Updated: {full_title[:40]}...")

with open('data.js', 'w') as f:
    f.write(content)

print(f"\nTotal updated: {count} lessons")
