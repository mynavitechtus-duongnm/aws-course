#!/usr/bin/env python3
"""Update all remaining lessons with generic summaries"""

with open('data.js', 'r') as f:
    content = f.read()

# Generic summaries by keyword
generics = {
    "Auto Scaling": {
        "summary": "Tim hieu Auto Scaling trong AWS.",
        "explanation": "<p>Auto Scaling tu dong dieu chinh so luong instances.</p><h4>Components</h4><ul><li>Launch Template</li><li>Auto Scaling Group</li><li>Scaling Policies</li></ul><h4>Metrics</h4><ul><li>CPU Utilization</li><li>Network</li><li>Custom</li></ul>"
    },
    "Launch Template": {
        "summary": "Tao Launch Template cho EC2 instances.",
        "explanation": "<p>Launch Template dinh nghia cau hinh cho EC2 instances.</p><h4>Components</h4><ul><li>AMI, Instance Type</li><li>Security Groups</li><li>User Data</li></ul>"
    },
    "Termination Protection": {
        "summary": "Bao ve instances khoi accidental termination.",
        "explanation": "<p>Termination protection ngan chan xoa loi instances.</p><h4>Enable</h4><pre>aws ec2 modify-instance-attribute --instance-id i-xxx --disable-api-termination Value=true</pre>"
    },
    "Reserve Instance": {
        "summary": "Su dung Reserved Instances de tiet kiem chi phi.",
        "explanation": "<p>Reserved Instances cung cap discount cho steady-state workloads.</p><h4>Options</h4><ul><li>No Upfront</li><li>Partial Upfront</li><li>All Upfront</li></ul>"
    },
    "S3 Bucket": {
        "summary": "Tao va quan ly S3 bucket.",
        "explanation": "<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>"
    },
    "Static Website": {
        "summary": "Host static website tren S3.",
        "explanation": "<p>S3 co the host static websites.</p><h4>Enable</h4><pre>Static website hosting in bucket properties</pre>"
    },
    "Versioning": {
        "summary": "Su dung S3 Versioning de ngan chan xoa loi.",
        "explanation": "<p>Versioning luu tru nhieu phien ban object.</p><h4>Enable</h4><pre>aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled</pre>"
    },
    "Storage Classes": {
        "summary": "Tim hieu cac S3 Storage Classes.",
        "explanation": "<p>Chon dung storage class de toi uu chi phi.</p><h4>Classes</h4><ul><li>Standard: Truy cap thuong xuyen</li><li>IA: Truy cap it</li><li>Glacier: Luu tru lau dai</li></ul>"
    },
    "CloudFront": {
        "summary": "Su dung CloudFront CDN.",
        "explanation": "<p>CloudFront la CDN cua AWS.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>Caching</li></ul>"
    },
    "Route53": {
        "summary": "Quan ly DNS voi Route 53.",
        "explanation": "<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>"
    },
    "Health Check": {
        "summary": "Cau hinh Health Checks.",
        "explanation": "<p>Health checks monitor endpoints.</p><h4>Use Cases</h4><ul><li>Failover routing</li><li>Auto scaling</li></ul>"
    },
    "DynamoDB": {
        "summary": "Su dung DynamoDB NoSQL database.",
        "explanation": "<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>"
    },
    "CloudWatch": {
        "summary": "Monitoring voi CloudWatch.",
        "explanation": "<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>"
    },
    "Lambda": {
        "summary": "Serverless computing voi Lambda.",
        "explanation": "<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>"
    },
    "API Gateway": {
        "summary": "Tao APIs voi API Gateway.",
        "explanation": "<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>"
    },
    "Cognito": {
        "summary": "Authentication voi Cognito.",
        "explanation": "<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>"
    },
    "ECS": {
        "summary": "Container orchestration voi ECS.",
        "explanation": "<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2</li><li>Fargate</li></ul>"
    },
    "IAM": {
        "summary": "Quan ly truy cap voi IAM.",
        "explanation": "<p>IAM quan ly truy cap AWS resources.</p><h4>Components</h4><ul><li>Users, Groups</li><li>Roles, Policies</li></ul>"
    },
    "EBS": {
        "summary": "Block storage voi EBS.",
        "explanation": "<p>EBS cung cap block storage cho EC2.</p><h4>Types</h4><ul><li>gp3: General purpose</li><li>io2: High performance</li></ul>"
    },
    "Snapshot": {
        "summary": "Backup voi EBS Snapshots.",
        "explanation": "<p>Snapshots la incremental backups.</p><h4>Commands</h4><pre>aws ec2 create-snapshot --volume-id vol-xxx</pre>"
    },
    "AMI": {
        "summary": "Tao AMI tu EC2 instance.",
        "explanation": "<p>AMI la blueprint de launch instances.</p><h4>Commands</h4><pre>aws ec2 create-image --instance-id i-xxx</pre>"
    },
    "Load Balancer": {
        "summary": "Phan phoi traffic voi Load Balancer.",
        "explanation": "<p>Load Balancer phan phoi traffic den instances.</p><h4>Types</h4><ul><li>ALB: HTTP/HTTPS</li><li>NLB: TCP/UDP</li></ul>"
    },
    "VPC": {
        "summary": "Virtual network voi VPC.",
        "explanation": "<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>"
    },
    "RDS": {
        "summary": "Managed database voi RDS.",
        "explanation": "<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>"
    },
    "SNS": {
        "summary": "Messaging voi SNS.",
        "explanation": "<p>SNS la pub/sub messaging service.</p><h4>Components</h4><ul><li>Topics</li><li>Subscriptions</li></ul>"
    },
    "SES": {
        "summary": "Email service voi SES.",
        "explanation": "<p>SES gui email qua SMTP.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing</li></ul>"
    }
}

# Replace all remaining placeholders with generic content
import re

# Find all summaries matching pattern "Bài học về ... trong khóa học AWS."
pattern = r'summary: "Bài học về [^"]+"'
matches = re.findall(pattern, content)

for match in matches:
    # Extract the lesson title
    title_match = re.search(r'Bài học về (.+?) trong khóa học AWS\.', match)
    if title_match:
        lesson_title = title_match.group(1)
        
        # Find best matching generic
        new_summary = None
        new_explanation = None
        
        for keyword, data in generics.items():
            if keyword.lower() in lesson_title.lower():
                new_summary = f'summary: "{data["summary"]}"'
                new_explanation = f'explanation: `{data["explanation"]}`'
                break
        
        if new_summary:
            old_summary = match
            content = content.replace(old_summary, new_summary, 1)
            
            # Also replace explanation
            # Find explanation pattern for this summary
            explanation_pattern = f'explanation: `<p>Bài học về {lesson_title}. Xem video để hiểu chi tiết.</p>`'
            if explanation_pattern in content:
                content = content.replace(explanation_pattern, new_explanation, 1)
                print(f"Updated: {lesson_title[:40]}...")

with open('data.js', 'w') as f:
    f.write(content)

print("\nDone!")
