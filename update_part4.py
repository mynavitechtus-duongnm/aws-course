#!/usr/bin/env python3
"""Update remaining lessons with shorter summaries"""

with open('data.js', 'r') as f:
    content = f.read()

# Shorter summaries for remaining lessons
shorter_lessons = {
    "Auto Scaling With Load Balancer - Load Balancer with Auto Scaling - AWS (Hindi)": {
        "summary": "Tich hop Auto Scaling Group voi Load Balancer.",
        "explanation": "<p>Ket hop ASG va ELB dam bao high availability.</p><h4>Benefits</h4><ul><li>LB distributes traffic</li><li>ASG replaces unhealthy instances</li></ul>"
    },
    "Enable Termination Protection - Hibernet vs PowerOff - AWS (Hindi)": {
        "summary": "Bao ve instances khoi accidental termination.",
        "explanation": "<p>Termination protection ngan chan xoa loi.</p><h4>Enable</h4><pre>aws ec2 modify-instance-attribute --instance-id i-xxx --disable-api-termination Value=true</pre>"
    },
    "How to create Reserve Instance - How to attach multiple NIC - AWS (Hindi)": {
        "summary": "Tao Reserved Instances va cau hinh multiple NICs.",
        "explanation": "<p>Reserved Instances tiet kiem chi phi.</p><h4>Purchase</h4><ol><li>EC2 > Reserved Instances</li><li>Select offering</li></ol>"
    },
    "How to Create Bucket in AWS | Create S3 Bucket | Create First Bucket ( in Hindi)": {
        "summary": "Huong dan tao S3 bucket dau tien.",
        "explanation": "<p>Tao S3 bucket de luu tru files.</p><h4>Tao</h4><pre>aws s3 mb s3://my-bucket</pre>"
    },
    "Host Static Website in S3 -How to host Static Website in S3 ( in Hindi)": {
        "summary": "Host static website tren S3.",
        "explanation": "<p>S3 co the host static websites.</p><h4>Enable</h4><pre>Static website hosting in bucket properties</pre>"
    },
    "S3 Versioning - What is Versioning - Prevent a Object from Deletion ( in Hindi)": {
        "summary": "Su dung S3 Versioning de ngan chan xoa loi.",
        "explanation": "<p>Versioning luu tru nhieu phien ban object.</p><h4>Enable</h4><pre>aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled</pre>"
    },
    "AWS S3 - Storage Classes - Standard - Infrequent - Glacier (In Hindi)": {
        "summary": "Tim hieu cac S3 Storage Classes.",
        "explanation": "<p>Chon dung storage class de toi uu chi phi.</p><h4>Classes</h4><ul><li>Standard: Truy cap thuong xuyen</li><li>IA: Truy cap it</li><li>Glacier: Luu tru lau dai</li></ul>"
    },
    "What is Cloudfront ? Create First Distribution with EC2 Instance": {
        "summary": "Gioi thieu CloudFront CDN.",
        "explanation": "<p>CloudFront la CDN cua AWS.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li></ul>"
    },
    "Route53 Overview | AWS Fully Managed DNS Service": {
        "summary": "Gioi thieu Amazon Route 53 - DNS service.",
        "explanation": "<p>Route 53 la DNS web service.</p><h4>Features</h4><ul><li>Highly available</li><li>DNS management</li><li>Health checks</li></ul>"
    },
    "Route53 Health Check in Action | AWS": {
        "summary": "Cau hinh Health Checks trong Route 53.",
        "explanation": "<p>Health checks monitor endpoints.</p><h4>Create</h4><pre>aws route53 create-health-check</pre>"
    },
    "Amazon DynamoDB - How to Create Table in DynamoDB": {
        "summary": "Tao DynamoDB table dau tien.",
        "explanation": "<p>DynamoDB la fully managed NoSQL database.</p><h4>Create</h4><pre>aws dynamodb create-table --table-name Music --key-schema AttributeName=Artist,KeyType=H</pre>"
    },
    "CloudWatch Service - what/why CloudWatch - Introduction": {
        "summary": "Gioi thieu Amazon CloudWatch.",
        "explanation": "<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>"
    },
    "CloudWatch Service - Trigger Alert - Cloudwatch Alarm": {
        "summary": "Tao CloudWatch Alarm.",
        "explanation": "<p>Alarm thong bao khi metrics vuot nguong.</p><h4>Create</h4><pre>aws cloudwatch put-metric-alarm --alarm-name high-cpu --metric-name CPUUtilization --threshold 80</pre>"
    },
    "What is Serverless & How to Create Your First Function": {
        "summary": "Gioi thieu Serverless va Lambda.",
        "explanation": "<p>Lambda cho phep chay code ma khong can servers.</p><h4>Create Function</h4><pre>aws lambda create-function --function-name my-func --runtime nodejs18.x --handler index.handler</pre>"
    },
    "AWS Lambda Basics in Hindi | Passing Data to Functions with Event Object": {
        "summary": "Hieu ve Lambda event object.",
        "explanation": "<p>Lambda nhan event data tu triggering service.</p><h4>Event</h4><pre>exports.handler = async (event, context) => {\n  console.log(event);\n};</pre>"
    },
    "AWS Lambda - Environment Variables in AWS Lambda": {
        "summary": "Su dung Environment Variables trong Lambda.",
        "explanation": "<p>Environment variables luu tru cau hinh.</p><h4>Set</h4><pre>aws lambda update-function-configuration --function-name my-func --environment Variables={KEY=value}</pre>"
    },
    "AWS Lambda - General Configuration Settings": {
        "summary": "Cau hinh chung cho Lambda function.",
        "explanation": "<p>Cac cau hinh quan trong cua Lambda.</p><h4>Settings</h4><ul><li>Memory: 128-10240 MB</li><li>Timeout: 1-900 seconds</li><li>Runtime</li></ul>"
    },
    "AWS Lambda - Context Object in Function": {
        "summary": "Hieu ve Lambda context object.",
        "explanation": "<p>Context cung cap thong tin ve function execution.</p><h4>Properties</h4><ul><li>functionName</li><li>memoryLimitInMB</li><li>remainingTime()</li></ul>"
    },
    "AWS Lambda - Synchronous vs Asynchronous": {
        "summary": "Su dung Lambda Synchronous va Asynchronous invocations.",
        "explanation": "<p>Lambda co the duoc invoke synchronous hoac asynchronous.</p><h4>Sync</h4><ul><li>API Gateway, ALB</li><li>Return response</li></ul><h4>Async</h4><ul><li>S3, SNS</li><li>Fire and forget</li></ul>"
    },
    "AWS Lambda - Dead Letter Queue in Lamda - Retry attempts": {
        "summary": "Su dung DLQ de xu ly failed invocations.",
        "explanation": "<p>DLQ nhan failed messages de xu ly sau.</p><h4>Setup</h4><pre>SQS queue or SNS topic</pre><h4>Use Cases</h4><ul><li>Retry failed processing</li><li>Manual investigation</li></ul>"
    },
    "AWS Lambda - How to Trigger AWS Lambda on S3 Object Creation": {
        "summary": "Trigger Lambda khi S3 object duoc tao.",
        "explanation": "<p>S3 co the trigger Lambda khi co event.</p><h4>Setup</h4><ol><li>Create Lambda function</li><li>Add S3 trigger</li><li>Configure bucket</li></ol>"
    },
    "API Gateway - What is API Gateway | AWS in Hindi": {
        "summary": "Gioi thieu Amazon API Gateway.",
        "explanation": "<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>"
    },
    "How to Create REST API in API Gateway | AWS Tutorial": {
        "summary": "Tao REST API trong API Gateway.",
        "explanation": "<p>Tao API de expose Lambda functions.</p><h4>Steps</h4><ol><li>Create API</li><li>Create resource</li><li>Create method</li><li>Deploy</li></ol>"
    },
    "API Gateway Integration with Lambda | AWS Tutorial": {
        "summary": "Ket hop API Gateway voi Lambda.",
        "explanation": "<p>API Gateway goi Lambda function.</p><h4>Integration</h4><pre>Integration type: Lambda Function</pre>"
    },
    "How to Deploy API Gateway API | AWS Tutorial": {
        "summary": "Deploy API Gateway API.",
        "explanation": "<p>Deploy de API co the truy cap.</p><h4>Deploy</h4><pre>aws apigateway create-deployment --rest-api-id xxx --stage-name prod</pre>"
    },
    "Cognito - What is Cognito | AWS in Hindi": {
        "summary": "Gioi thieu Amazon Cognito.",
        "explanation": "<p>Cognito cung cap authentication cho apps.</p><h4>User Pools</h4><ul><li>Sign up/in</li><li>JWT tokens</li></ul><h4>Identity Pools</h4><ul><li>Temp AWS credentials</li></ul>"
    },
    "How to Create User Pool in Cognito | AWS Tutorial": {
        "summary": "Tao Cognito User Pool.",
        "explanation": "<p>Tao User Pool de quan ly users.</p><h4>Steps</h4><ol><li>Cognito > User Pools</li><li>Create pool</li><li>Configure attributes</li></ol>"
    },
    "ECS - What is ECS | AWS in Hindi": {
        "summary": "Gioi thieu Amazon ECS.",
        "explanation": "<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2: Quan ly EC2 instances</li><li>Fargate: Serverless</li></ul>"
    },
    "How to Create ECS Cluster | AWS Tutorial": {
        "summary": "Tao ECS Cluster dau tien.",
        "explanation": "<p>Tao cluster de chay containers.</p><h4>Steps</h4><ol><li>ECS > Clusters</li><li>Create cluster</li><li>Choose launch type</li></ol>"
    },
    "Task Definition in ECS | AWS Tutorial": {
        "summary": "Hieu ve Task Definition trong ECS.",
        "explanation": "<p>Task Definition la blueprint cho container.</p><h4>Components</h4><ul><li>Image</li><li>Port mappings</li><li>Environment variables</li><li>CPU/Memory</li></ul>"
    }
}

# Update all lessons
count = 0
for title, data in shorter_lessons.items():
    old_summary = f'summary: "Bài học về {title} trong khóa học AWS."'
    new_summary = f'summary: "{data["summary"]}"'
    
    old_explanation = f'explanation: `<p>Bài học về {title}. Xem video để hiểu chi tiết.</p>`'
    new_explanation = f'explanation: `{data["explanation"]}`'
    
    if old_summary in content:
        content = content.replace(old_summary, new_summary)
        content = content.replace(old_explanation, new_explanation)
        count += 1
        print(f"Updated: {title[:50]}...")

with open('data.js', 'w') as f:
    f.write(content)

print(f"\nTotal updated: {count} lessons")
