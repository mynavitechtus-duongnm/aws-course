#!/usr/bin/env python3
"""Update all remaining lessons - simplified version"""

with open('data.js', 'r') as f:
    content = f.read()

# Simplified content without special characters
all_lessons = {
    "AWS IAM Service - Identity and Access Management - AWS (Hindi)": {
        "summary": "Gioi thieu AWS IAM - quan ly truy cap an toan.",
        "explanation": "<p>IAM cho phep quan ly truy cap AWS resources.</p><h4>Components</h4><ul><li>Users: Nguoi su dung</li><li>Groups: Nhom nguoi dung</li><li>Roles: Quyen tam thoi</li><li>Policies: Dinh nghia quyen</li></ul><h4>Features</h4><ul><li>Fine-grained permissions</li><li>Multi-factor authentication</li><li>Password policy</li></ul>"
    },
    "AWS IAM Service - Groups in AWS - AWS (Hindi)": {
        "summary": "Su dung IAM Groups de quan ly nhieu users.",
        "explanation": "<p>Groups giup quan ly permissions cho nhieu users.</p><h4>Tao Group</h4><pre>aws iam create-group --group-name Developers</pre><h4>Add User</h4><pre>aws iam add-user-to-group --user-name john --group-name Developers</pre>"
    },
    "AWS IAM Service - Password Policy - AWS (Hindi)": {
        "summary": "Cau hinh IAM Password Policy.",
        "explanation": "<p>Password Policy giup tang bao mat tai khoan.</p><h4>Cau hinh</h4><pre>aws iam update-account-password-policy --minimum-password-length 12</pre><h4>Requirements</h4><ul><li>Minimum 12 characters</li><li>Uppercase, lowercase, numbers, symbols</li></ul>"
    },
    "AWS Multi Factor Authentication - AWS MFA - AWS (Hindi)": {
        "summary": "Kich hoat MFA cho tai khoan AWS.",
        "explanation": "<p>MFA tang cuong bao mat bang cach yeu cau ma thu hai.</p><h4>Enable</h4><ol><li>IAM > Users > Security credentials</li><li>Assign MFA device</li><li>Scan QR code</li></ol><h4>Virtual MFA Apps</h4><ul><li>Google Authenticator</li><li>Authy</li><li>Microsoft Authenticator</li></ul>"
    },
    "How to use AWS CLI - AWS Configure - How to Create AWS Instance Using CLI": {
        "summary": "Huong dan su dung AWS CLI.",
        "explanation": "<p>AWS CLI cho phep tuong tac voi AWS bang command line.</p><h4>Install</h4><pre>pip install awscli</pre><h4>Configure</h4><pre>aws configure</pre><h4>Su dung</h4><pre>aws ec2 describe-instances</pre>"
    },
    "AWS CLI Handle Multiple AWS Accounts - How to use AWS CLI In Linux -AWS(Hindi)": {
        "summary": "Quan ly nhieu AWS accounts voi CLI.",
        "explanation": "<p>Su dung named profiles de quan ly nhieu accounts.</p><h4>Tao Profile</h4><pre>aws configure --profile production</pre><h4>Su dung</h4><pre>aws ec2 describe-instances --profile production</pre>"
    },
    "What is AWS Roles & How to use AWS Cli without Access Id and Secret key - AWS": {
        "summary": "Su dung IAM Roles thay vi Access Keys.",
        "explanation": "<p>IAM Roles cung cap quyen tam thoi ma khong can access keys.</p><h4>Su dung Role</h4><ol><li>Tao IAM Role</li><li>Attach policy</li><li>Assume role</li></ol><h4>Benefits</h4><ul><li>Khong luu credentials</li><li>Auto rotation</li></ul>"
    },
    "What/Why is CloudShell || IAM - Access Advisor || IAM - Credential Report": {
        "summary": "Su dung AWS CloudShell va IAM reports.",
        "explanation": "<p>CloudShell cung cap shell trinh trong browser.</p><h4>CloudShell</h4><ul><li>Pre-authenticated AWS CLI</li><li>Khong can setup</li></ul><h4>Access Advisor</h4><ul><li>Xem service permissions</li><li>Last accessed info</li></ul>"
    },
    "Introduction to Amazon Simple Storage Service (S3) | AWS S3 Service (in Hindi)": {
        "summary": "Gioi thieu Amazon S3 - object storage.",
        "explanation": "<p>S3 cung cap object storage voi do ben cao.</p><h4>Features</h4><ul><li>99.999999999% durability</li><li>Infinite scalability</li><li>Multiple storage classes</li></ul><h4>Components</h4><ul><li>Buckets: Container</li><li>Objects: Files</li><li>Keys: Unique identifier</li></ul>"
    },
    "How to Create Bucket in AWS | Create S3 Bucket | Create First Bucket ( in Hindi)": {
        "summary": "Huong dan tao S3 bucket dau tien.",
        "explanation": "<p>Tao S3 bucket de luu tru files.</p><h4>Tao Bucket</h4><pre>aws s3 mb s3://my-unique-bucket-name</pre><h4>Console</h4><ol><li>S3 > Create bucket</li><li>Choose unique name</li><li>Select region</li></ol><h4>Luu y</h4><ul><li>Bucket name globally unique</li></ul>"
    },
    "Public your Bucket Object | Policy Generator | Allow Object to Public ( in Hindi)": {
        "summary": "Cach lam object tro nen public.",
        "explanation": "<p>Public object bang bucket policy.</p><h4>Bucket Policy</h4><pre>Allow public read access</pre><h4>JSON</h4><pre>{Version, Statement, Effect:Allow, Principal:*, Action:GetObject}</pre><h4>Luu y</h4><ul><li>Public access co the la van de bao mat</li></ul>"
    },
    "S3 Object - S3 Object Properties - S3 Object Metadata - S3 Object Key ( in Hindi)": {
        "summary": "Tim hieu S3 Object, metadata va key.",
        "explanation": "<p>S3 Object bao gom data, key, metadata.</p><h4>Components</h4><ul><li>Key: Unique identifier</li><li>Value: Data content</li><li>Metadata: System or custom</li><li>Version ID</li></ul><h4>URL</h4><pre>https://bucket.s3.region.amazonaws.com/key</pre>"
    },
    "S3 Versioning - What is Versioning - Prevent a Object from Deletion ( in Hindi)": {
        "summary": "Su dung S3 Versioning de ngan chan xoa loi.",
        "explanation": "<p>Versioning luu tru nhieu phien ban cua object.</p><h4>Enable</h4><pre>aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled</pre><h4>Benefits</h4><ul><li>Protect against accidental deletes</li><li>Restore previous versions</li></ul>"
    },
    "Host Static Website in S3 -How to host Static Website in S3 ( in Hindi)": {
        "summary": "Host static website tren S3.",
        "explanation": "<p>S3 co the host static websites.</p><h4>Enable</h4><ol><li>S3 > Bucket > Properties</li><li>Static website hosting</li><li>Index document: index.html</li></ol><h4>Upload</h4><pre>aws s3 sync ./website s3://my-bucket/</pre>"
    },
    "How to Redirect in S3 Static Website From one to another ( in Hindi)": {
        "summary": "Cau hinh redirect trong S3 static website.",
        "explanation": "<p>Redirect requests den URL khac.</p><h4>Enable Redirect</h4><pre>Set x-amz-website-redirect-location metadata</pre><h4>Use Cases</h4><ul><li>Domain redirects</li><li>HTTP to HTTPS</li></ul>"
    },
    "How to Change Prefix in Static Website S3 - Redirect S3 Prefix in S3 (in Hindi)": {
        "summary": "Redirect trong S3 su dung prefix.",
        "explanation": "<p>Redirect requests dua tren prefix.</p><h4>Routing Rules</h4><pre>Condition: KeyPrefixEquals=old/</pre><pre>Redirect: ReplaceKeyPrefixWith=new/</pre>"
    },
    "S3 Accelerated Transfer, How to Enable? How to Use Accelerated Transfer?": {
        "summary": "Su dung S3 Transfer Acceleration.",
        "explanation": "<p>Transfer Acceleration tang toc do upload/download.</p><h4>Enable</h4><pre>aws s3api put-bucket-accelerate-configuration --bucket my-bucket --accelerate-configuration Status=Enabled</pre><h4>Su dung</h4><pre>https://my-bucket.s3-accelerate.amazonaws.com</pre>"
    },
    "Same/Cross Region Replication - What is SRR/CRR - Use of SRR/CRR?": {
        "summary": "Su dung S3 Replication de sao chep data.",
        "explanation": "<p>S3 Replication tu dong sao chep objects.</p><h4>SRR</h4><ul><li>Sao chep trong cung region</li><li>Compliance, backup</li></ul><h4>CRR</h4><ul><li>Sao chep giua regions</li><li>DR, latency</li></ul>"
    },
    "AWS S3 - Configure Logging in S3 Bucket - How to Enable S3 Logging (In Hindi)": {
        "summary": "Kich hoat logging cho S3 bucket.",
        "explanation": "<p>Server access logging ghi lai requests.</p><h4>Enable</h4><pre>aws s3api put-bucket-logging --bucket my-bucket</pre><h4>Config</h4><pre>TargetBucket: my-logs-bucket</pre><pre>TargetPrefix: logs/</pre>"
    },
    "AWS S3 - Storage Classes - Standard - Infrequent - Glacier (In Hindi)": {
        "summary": "Tim hieu cac S3 Storage Classes.",
        "explanation": "<p>Chon dung storage class de toi uu chi phi.</p><h4>Storage Classes</h4><ul><li>S3 Standard: Truy cap thuong xuyen</li><li>S3 IA: Truy cap it</li><li>S3 Glacier: Luu tru lau dai</li><li>S3 Deep Archive: Cheapest</li><li>S3 Intelligent-Tiering: Tu dong</li></ul>"
    },
    "AWS S3 - Storage Classes - Configure Storage Class (In Hindi)": {
        "summary": "Cau hinh storage class cho objects.",
        "explanation": "<p>Dat storage class khi upload hoac sau.</p><h4>Khi Upload</h4><pre>aws s3 cp file.txt s3://my-bucket/ --storage-class STANDARD_IA</pre><h4>Options</h4><ul><li>STANDARD</li><li>STANDARD_IA</li><li>GLACIER</li></ul>"
    },
    "Simplify Data Lifecycle Management with AWS S3 - ( AWS In Hindi )": {
        "summary": "Su dung S3 Lifecycle Policies.",
        "explanation": "<p>Lifecycle policies tu dong chuyen doi hoac xoa objects.</p><h4>Tao Policy</h4><pre>Transitions: Move to Glacier after 30 days</pre><pre>Expiration: Delete after 365 days</pre><h4>Use Cases</h4><ul><li>Auto-archive</li><li>Delete old logs</li></ul>"
    },
    "Cost Efficiency and Performance with AWS Intelligent Tiering for S3 ( In Hindi)": {
        "summary": "Su dung S3 Intelligent-Tiering.",
        "explanation": "<p>Intelligent-Tiering tu dong toi uu chi phi.</p><h4>Tiers</h4><ul><li>Frequent Access</li><li>Infrequent Access</li><li>Archive Instant Access</li></ul><h4>Best For</h4><ul><li>Unknown access patterns</li><li>Cost optimization</li></ul>"
    },
    "What is CORS and How To Enable IT in S3 - ( AWS In Hindi )": {
        "summary": "Cau hinh CORS cho S3 bucket.",
        "explanation": "<p>CORS cho phep web apps tu domain khac truy cap S3.</p><h4>Config</h4><pre>AllowedOrigins: https://mywebsite.com</pre><pre>AllowedMethods: GET, PUT</pre><h4>Use Cases</h4><ul><li>Static websites</li><li>SPAs</li></ul>"
    },
    "What is Presigned URL in S3 - ( AWS In Hindi )": {
        "summary": "Su dung Presigned URL de chia se private objects.",
        "explanation": "<p>Presigned URL cho phep truy cap private objects.</p><h4>Tao</h4><pre>aws s3 presign s3://my-bucket/file.txt --expires-in 3600</pre><h4>Use Cases</h4><ul><li>Share files temporarily</li><li>Upload without credentials</li></ul>"
    },
    "Securing Your AWS S3 Data: At Rest, Server-Side, and Client-Side Encryption": {
        "summary": "Bao mat S3 data voi encryption.",
        "explanation": "<p>S3 cung cap nhieu muc do ma hoa.</p><h4>At Rest</h4><ul><li>SSE-S3: AWS managed keys</li><li>SSE-KMS: KMS keys</li><li>SSE-C: Customer keys</li></ul><h4>Enable SSE-S3</h4><pre>S3 > Properties > Default encryption</pre>"
    },
    "What is Cloudfront ? Create First Distribution with EC2 Instance": {
        "summary": "Gioi thieu CloudFront CDN.",
        "explanation": "<p>CloudFront la CDN giup deliver content nhanh hon.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>SSL support</li></ul><h4>Create Distribution</h4><pre>aws cloudfront create-distribution --origin-domain-name mylb.elb.amazonaws.com</pre>"
    },
    "AWS CloudFront Invalidation - How to Remove Data From CloudFront Edge -In Hindi": {
        "summary": "Invalidate cache trong CloudFront.",
        "explanation": "<p>Invalidation xoa cache tu edge locations.</p><h4>Create</h4><pre>aws cloudfront create-invalidation --distribution-id XXXX --paths \"/images/*\"</pre><h4>Luu y</h4><ul><li>Co phi cho invalidations > 1000 paths</li></ul>"
    },
    "How to make EC2/ALB Instance Accessible from CloudFront Only -In Hindi": {
        "summary": "Bao mat origin chi cho phep CloudFront truy cap.",
        "explanation": "<p>Chi cho phep traffic tu CloudFront den origin.</p><h4>Restrict Access</h4><ul><li>Tao CloudFront key pair</li><li>Whitelist CloudFront IPs</li></ul><h4>Security Groups</h4><ul><li>ALB SG chi tu CloudFront SG</li></ul>"
    },
    "CloudFront with S3 - S3 Private Bucket with CloudFront -S3 Origin - In Hindi": {
        "summary": "Ket hop CloudFront voi S3 private bucket.",
        "explanation": "<p>Su dung CloudFront de access S3 private bucket.</p><h4>Use Cases</h4><ul><li>Protect S3 from direct access</li><li>Use signed URLs</li><li>Custom domain with SSL</li></ul><h4>OAI</h4><ul><li>Origin Access Identity</li></ul>"
    },
    "CloudFront Path Based routing with Mulitple Origin - Behavior - In Hindi": {
        "summary": "Su dung CloudFront path-based routing.",
        "explanation": "<p>CloudFront co the route den different origins theo path.</p><h4>Behaviors</h4><ul><li>/api/* -> API Gateway</li><li>/static/* -> S3</li><li>/* -> ALB</li></ul>"
    },
    "CloudFront Custom Error Page - CloudFront In Hindi - In Hindi": {
        "summary": "Tao custom error pages trong CloudFront.",
        "explanation": "<p>Customize error responses.</p><h4>Error Pages</h4><ol><li>CloudFront > Distributions</li><li>Error Pages tab</li><li>Create custom error response</li></ol><h4>Options</h4><ul><li>Custom message</li><li>Redirect to URL</li></ul>"
    },
    "How to Control Access to Your Content Based on Country - CloudFront In Hindi": {
        "summary": "Kiem soat truy cap theo quoc gia voi CloudFront.",
        "explanation": "<p>Geo-restriction kiem soat ai co the truy cap content.</p><h4>Enable</h4><ol><li>CloudFront > Distributions</li><li>Geographic restrictions</li><li>Whitelist or blacklist countries</li></ol><h4>Use Cases</h4><ul><li>Copyright compliance</li><li>Regional pricing</li></ul>"
    },
    "How to Disable CloudFront Distribution / How to Delete CloudFront Distribution": {
        "summary": "Xoa CloudFront distribution.",
        "explanation": "<p>Cach disable hoac delete CloudFront.</p><h4>Disable</h4><ol><li>CloudFront > Distributions</li><li>Actions > Disable</li></ol><h4>Delete</h4><ol><li>Phai disable truoc</li><li>Wait for deployment</li><li>Actions > Delete</li></ol>"
    }
}

# Update all lessons
count = 0
for title, data in all_lessons.items():
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
