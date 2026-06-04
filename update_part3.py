#!/usr/bin/env python3
"""Update remaining lessons - VPC, RDS, DynamoDB, Lambda, etc."""

with open('data.js', 'r') as f:
    content = f.read()

# Simplified content
all_lessons = {
    # VPC lessons
    "Amazon VPC Introduction | What is VPC | AWS VPC Tutorial": {
        "summary": "Gioi thieu Amazon VPC - Virtual Private Cloud.",
        "explanation": "<p>VPC cho phep tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets: Public va Private</li><li>Route Tables: Traffic routing</li><li>Internet Gateway: Internet access</li><li>NAT Gateway: Private to Internet</li></ul><h4>Benefits</h4><ul><li>Isolated network</li><li>Full control</li><li>Secure resources</li></ul>"
    },
    "How to Create VPC in AWS | Create Your First VPC | AWS VPC Tutorial": {
        "summary": "Huong dan tao VPC dau tien.",
        "explanation": "<p>Tao VPC de bat dau xay dung network.</p><h4>Tao VPC</h4><pre>aws ec2 create-vpc --cidr-block 10.0.0.0/16</pre><h4>Console</h4><ol><li>VPC Dashboard > Your VPCs</li><li>Create VPC</li><li>Name va CIDR block</li></ol><h4>Best Practice</h4><ul><li>Use RFC 1918 addresses</li><li>Plan CIDR blocks truoc</li></ul>"
    },
    "How to Create Subnet in AWS | Public and Private Subnet | AWS VPC Tutorial": {
        "summary": "Tao Subnets trong VPC.",
        "explanation": "<p>Subnets phan chia VPC thanh cac mang con.</p><h4>Public Subnet</h4><ul><li>Co route den Internet Gateway</li><li>For resources canh Internet</li></ul><h4>Private Subnet</h4><ul><li>Khong co direct Internet access</li><li>For databases, apps</li></ul><h4>Tao</h4><pre>aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.1.0/24 --availability-zone us-east-1a</pre>"
    },
    "How to Create Internet Gateway in AWS | AWS VPC Tutorial": {
        "summary": "Tao Internet Gateway cho VPC.",
        "explanation": "<p>Internet Gateway cho phep VPC ket noi Internet.</p><h4>Tao</h4><pre>aws ec2 create-internet-gateway</pre><h4>Attach to VPC</h4><pre>aws ec2 attach-internet-gateway --internet-gateway-id igw-xxx --vpc-id vpc-xxx</pre><h4>Route Table</h4><pre>0.0.0.0/0 -> igw-xxx</pre>"
    },
    "How to Create NAT Gateway in AWS | AWS VPC Tutorial": {
        "summary": "Tao NAT Gateway de Private Subnets truy cap Internet.",
        "explanation": "<p>NAT Gateway cho phep Private instances truy cap Internet outbound.</p><h4>Tao</h4><ol><li>Tao NAT Gateway in Public Subnet</li><li>Allocate Elastic IP</li><li>Update Private Subnet Route Table</li></ol><h4>CLI</h4><pre>aws ec2 create-nat-gateway --subnet-id subnet-xxx --allocation-id eip-xxx</pre><h4>Route</h4><pre>0.0.0.0/0 -> nat-xxx</pre>"
    },
    # Route53 lessons
    "Route53 Overview | AWS Fully Managed DNS Service": {
        "summary": "Gioi thieu Amazon Route 53 - DNS service.",
        "explanation": "<p>Route 53 la DNS web service cua AWS.</p><h4>Features</h4><ul><li>Highly available</li><li>Scalable</li><li>DNS management</li><li>Health checks</li><li>Domain registration</li></ul><h4>Record Types</h4><ul><li>A: IPv4 address</li><li>AAAA: IPv6</li><li>CNAME: Alias</li><li>MX: Mail</li></ul>"
    },
    "Route53 Register Your First Domain in Route53 | AWS": {
        "summary": "Dang ky domain voi Route 53.",
        "explanation": "<p>Mua va quan ly domain trong Route 53.</p><h4>Dang ky</h4><ol><li>Route 53 > Registered domains</li><li>Register domain</li><li>Fill info va pay</li></ol><h4>Domain Pricing</h4><ul><li>.com: ~12 USD/year</li><li>.net: ~11 USD/year</li></ul>"
    },
    "Route53 A Name and AAAA Record in Action | AWS": {
        "summary": "Tao A Record va AAAA Record trong Route 53.",
        "explanation": "<p>A Record map domain den IPv4, AAAA den IPv6.</p><h4>A Record</h4><pre>Name: example.com\nType: A\nValue: 1.2.3.4</pre><h4>AAAA Record</h4><pre>Name: example.com\nType: AAAA\nValue: 2001:db8::1</pre><h4>CLI</h4><pre>aws route53 change-resource-record-sets --hosted-zone-id Zxxx --change-batch file://change.json</pre>"
    },
    "Route53 CNAME Record in Action | AWS": {
        "summary": "Tao CNAME Record trong Route 53.",
        "explanation": "<p>CNAME redirect domain den domain khac.</p><h4>CNAME</h4><pre>Name: www.example.com\nType: CNAME\nValue: example.com</pre><h4>Luu y</h4><ul><li>Chi cho subdomain, khong cho apex</li><li>Cho apex, su dung Alias</li></ul>"
    },
    "Route53 Alias in Action | Alias vs CNAME | AWS": {
        "summary": "Su dung Alias Record thay vi CNAME cho AWS resources.",
        "explanation": "<p>Alias Record la AWS-specific, chi phi thap hon CNAME.</p><h4>Alias vs CNAME</h4><ul><li>Alias: Chi cho AWS resources, free</li><li>CNAME: Cho moi domain, co phi</li></ul><h4>Use Alias</h4><pre>Name: example.com\nType: A\nAlias: Yes\nValue: dualstack.myelb.elb.amazonaws.com</pre>"
    },
    "Route53 Health Check in Action | AWS": {
        "summary": "Cau hinh Health Checks trong Route 53.",
        "explanation": "<p>Health checks monitor endpoints va tu dong failover.</p><h4>Tao Health Check</h4><pre>aws route53 create-health-check --caller-reference xxx --health-check-config file://config.json</pre><h4>Config</h4><pre>Endpoint: example.com\nPort: 80\nType: HTTP</pre><h4>Use with Failover Routing</h4><ul><li>Primary: Your app</li><li>Secondary: Backup</li></ul>"
    },
    "Route53 Simple Routing Policy in Action | AWS": {
        "summary": "Su dung Simple Routing Policy.",
        "explanation": "<p>Simple Routing chi tra ve mot record duy nhat.</p><h4>Use Case</h4><ul><li>Single resource</li><li>Simple website</li></ul><h4>Config</h4><pre>Name: example.com\nType: A\nValue: 1.2.3.4</pre>"
    },
    "Route53 Weighted Routing Policy in Action | AWS": {
        "summary": "Su dung Weighted Routing Policy.",
        "explanation": "<p>Weighted Routing phan phoi traffic theo ti le.</p><h4>Example</h4><pre>v1.example.com -> 80%\nv2.example.com -> 20%</pre><h4>Use Cases</h4><ul><li>Blue-green deployment</li><li>A/B testing</li><li>Gradual rollout</li></ul>"
    },
    "Route53 Geolocation Routing Policy in Action | AWS": {
        "summary": "Su dung Geolocation Routing Policy.",
        "explanation": "<p>Geolocation Routing route traffic dua tren vi tri nguoi dung.</p><h4>Example</h4><pre>US users -> us-server.com\nEU users -> eu-server.com\nDefault -> global-server.com</pre><h4>Use Cases</h4><ul><li>Regional content</li><li>Compliance</li><li>Language targeting</li></ul>"
    },
    "Route53 Latency Based Routing Policy in Action | AWS": {
        "summary": "Su dung Latency Routing Policy.",
        "explanation": "<p>Latency Routing route den region co latency thap nhat.</p><h4>How it Works</h4><ul><li>Route 53 do latency tu users</li><li>Automatically route to fastest region</li></ul><h4>Use Case</h4><ul><li>Multi-region deployment</li><li>Global apps</li></ul>"
    },
    "Route53 Failover Routing Policy in Action | AWS": {
        "summary": "Su dung Failover Routing Policy.",
        "explanation": "<p>Failover Routing tu dong chuyen sang backup khi primary fail.</p><h4>Setup</h4><ol><li>Tao Health Check</li><li>Tao Primary Record (associated health check)</li><li>Tao Secondary Record</li></ol><h4>Use Cases</h4><ul><li>DR setup</li><li>High availability</li></ul>"
    },
    # RDS lessons
    "Amazon RDS - Amazon Relational Database Service": {
        "summary": "Gioi thieu Amazon RDS - managed database service.",
        "explanation": "<p>RDS cung cap managed relational databases.</p><h4>Supported Engines</h4><ul><li>MySQL</li><li>PostgreSQL</li><li>MariaDB</li><li>Oracle</li><li>SQL Server</li><li>Aurora</li></ul><h4>Benefits</h4><ul><li>Automated backups</li><li>Multi-AZ</li><li>Read replicas</li><li>Automated patching</li></ul>"
    },
    "Amazon RDS - Create First Database": {
        "summary": "Huong dan tao RDS instance dau tien.",
        "explanation": "<p>Tao RDS database instance.</p><h4>Tao</h4><ol><li>RDS > Create database</li><li>Choose engine (MySQL, PostgreSQL)</li><li>Choose instance size</li><li>Configure VPC, Security Group</li><li>Set master password</li></ol><h4>CLI</h4><pre>aws rds create-db-instance --db-instance-identifier my-db --db-instance-class db.t3.micro --engine mysql</pre>"
    },
    "Amazon RDS - Connect to RDS Instance": {
        "summary": "Ket noi den RDS instance.",
        "explanation": "<p>Ket noi database tu EC2 hoac local machine.</p><h4>Tu EC2</h4><pre>mysql -h my-db.xxxx.us-east-1.rds.amazonaws.com -u admin -p</pre><h4>Security Group</h4><ul><li>Allow port 3306 (MySQL)</li><li>From EC2 SG or specific IP</li></ul><h4>Connection Issues</h4><ul><li>Check SG rules</li><li>Check subnet routing</li><li>Verify credentials</li></ul>"
    },
    "Amazon RDS - What is Read Replica - How to Create Read Replica": {
        "summary": "Su dung Read Replica de giam load.",
        "explanation": "<p>Read Replica tao ban doc-only cua database.</p><h4>Create</h4><pre>aws rds create-db-instance-read-replica --db-instance-identifier my-replica --source-db-instance-identifier my-db</pre><h4>Use Cases</h4><ul><li>Scale read operations</li><li>Cross-region replication</li><li>DR</li></ul><h4>Luu y</h4><ul><li>Async replication</li><li>May have slight lag</li></ul>"
    },
    "Amazon RDS - What is Multi AZ in RDS": {
        "summary": "Cau hinh Multi-AZ cho RDS.",
        "explanation": "<p>Multi-AZ tao standby replica trong AZ khac.</p><h4>How it Works</h4><ul><li>Primary in AZ-1</li><li>Standby in AZ-2</li><li>Sync replication</li><li>Automatic failover</li></ul><h4>Create</h4><ol><li>Modify DB instance</li><li>Enable Multi-AZ</li></ol><h4>Benefits</h4><ul><li>High availability</li><li>Automatic failover</li><li>Zero data loss</li></ul>"
    },
    "Amazon RDS - What is Proxy in RDS": {
        "summary": "Su dung RDS Proxy de quan ly connections.",
        "explanation": "<p>RDS Proxy giam so luong connections den database.</p><h4>Benefits</h4><ul><li>Connection pooling</li><li>Reduced CPU usage</li><li>Better scaling</li></ul><h4>Use Cases</h4><ul><li>Lambda functions</li><li>Serverless apps</li><li>Many short connections</li></ul>"
    },
    "Amazon RDS - AWS Aurora Database - Create First Aurora Instance": {
        "summary": "Gioi thieu Amazon Aurora va cach tao.",
        "explanation": "<p>Aurora la MySQL/PostgreSQL-compatible database.</p><h4>Features</h4><ul><li>Up to 15 read replicas</li><li>Auto-sizing storage (10GB-128TB)</li><li>Multi-master</li><li>Backtrack</li></ul><h4>Create</h4><pre>aws rds create-db-cluster --engine aurora-mysql</pre>"
    },
    "Amazon RDS - Aurora Endpoints - Reader, Writer, Instance, Custom Endpoints": {
        "summary": "Hieu ve cac loai Aurora Endpoints.",
        "explanation": "<p>Aurora co nhieu endpoint types.</p><h4>Endpoints</h4><ul><li>Writer Endpoint: Primary instance</li><li>Reader Endpoint: Load-balanced read replicas</li><li>Instance Endpoint: Specific instance</li><li>Custom Endpoint: Custom group of instances</li></ul>"
    },
    # DynamoDB lessons
    "Amazon DynamoDB - How to Create Table in DynamoDB": {
        "summary": "Tao DynamoDB table dau tien.",
        "explanation": "<p>DynamoDB la fully managed NoSQL database.</p><h4>Create Table</h4><pre>aws dynamodb create-table --table-name Music --attribute-definitions AttributeName=Artist,AttributeType=S --key-schema AttributeName=Artist,KeyType=H --billing-mode PAY_PER_REQUEST</pre><h4>Keys</h4><ul><li>Partition Key (PK): Required</li><li>Sort Key (SK): Optional</li></ul>"
    },
    "Amazon DynamoDB - What is sort key": {
        "summary": "Hieu ve Sort Key trong DynamoDB.",
        "explanation": "<p>Sort Key cho phep tao composite primary key.</p><h4>Composite Key</h4><ul><li>Partition Key: Groups items</li><li>Sort Key: Orders items within group</li></ul><h4>Example</h4><pre>PK: UserID\nSK: Timestamp\nQuery: Get all orders for user, sorted by time</pre>"
    },
    "Amazon DynamoDB - Scan And Query": {
        "summary": "Su dung Query vs Scan trong DynamoDB.",
        "explanation": "<p>Query tim kiem hieu qua hon Scan.</p><h4>Query</h4><ul><li>Tim theo Partition Key</li><li>Co the loc theo Sort Key</li><li>Hieu qua hon Scan</li></ul><h4>Scan</h4><ul><li>Doc toan bo table</li><li>Ton nhieu RCU</li><li>Chi khi Query khong duoc</li></ul><h4>Best Practice</h4><ul><li>Luon su dung Query khi co the</li></ul>"
    },
    "Amazon DynamoDB - Read and Write Capacity Units": {
        "summary": "Hieu ve Capacity Units trong DynamoDB.",
        "explanation": "<p>DynamoDB pricing dua tren read/write capacity.</p><h4>RCU (Read Capacity Unit)</h4><ul><li>1 strongly consistent read: 4KB</li><li>2 eventually consistent reads: 4KB</li></ul><h4>WCU (Write Capacity Unit)</h4><ul><li>1 write: 1KB</li></ul><h4>On-Demand</h4><ul><li>Pay per request</li><li>Khong can capacity planning</li></ul>"
    },
    "Amazon DynamoDB - Global Secondary Index": {
        "summary": "Su dung Global Secondary Index (GSI).",
        "explanation": "<p>GSI cho phep query tren cac thuoc tinh khac.</p><h4>Create GSI</h4><pre>aws dynamodb update-table --table-name Music --attribute-definitions AttributeName=AlbumName,AttributeType=S --global-secondary-index-updates file://gsi.json</pre><h4>Use Cases</h4><ul><li>Query by different attributes</li><li>Alternative access patterns</li></ul>"
    },
    # SNS lessons
    "Simple Notification Service - Send First Notification - (Hindi)": {
        "summary": "Gui notification dau tien voi SNS.",
        "explanation": "<p>SNS la messaging service cho push notifications.</p><h4>Components</h4><ul><li>Topic: Channel de publish</li><li>Subscription: Endpoint nhan messages</li><li>Publisher: Gui message</li></ul><h4>Create Topic</h4><pre>aws sns create-topic --name my-topic</pre><h4>Subscribe</h4><pre>aws sns subscribe --topic-arn arn:aws:sns:xxx --protocol email --endpoint-endpoint you@example.com</pre><h4>Publish</h4><pre>aws sns publish --topic-arn arn:aws:sns:xxx --message \"Hello!\"</pre>"
    },
    "Simple Notification Service - Why should we use SNS - Configurations - (Hindi)": {
        "summary": "Hieu vi sao nen su dung SNS.",
        "explanation": "<p>SNS cho phep fan-out notifications.</p><h4>Use Cases</h4><ul><li>Push notifications</li><li>Email/SMS alerts</li><li>Microservices communication</li><li>Trigger Lambda functions</li></ul><h4>Protocols</h4><ul><li>HTTP/HTTPS</li><li>Email</li><li>SMS</li><li>Lambda</li><li>SQS</li><li>Mobile Push</li></ul>"
    },
    "Simple Notification Service - Send Mobile SMS Notification": {
        "summary": "Gui SMS su dung SNS.",
        "explanation": "<p>SNS co the gui SMS messages.</p><h4>Configure</h4><ol><li>Opt-in phone number</li><li>Create topic</li><li>Subscribe with SMS</li></ol><h4>Costs</h4><ul><li>Co phi cho moi SMS</li><li>Gia thay doi theo quoc gia</li></ul>"
    },
    # SES lessons
    "Amazon Simple Email Service - Where/How we can use it": {
        "summary": "Gioi thieu Amazon SES - email service.",
        "explanation": "<p>SES la email service cho sending/receiving email.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing emails</li><li>Email verification</li></ul><h4>Benefits</h4><ul><li>Cost-effective</li><li>Scalable</li><li>Reliable</li></ul>"
    },
    "Email Service - How Emails End Up in Spam and How to Prevent It": {
        "summary": "Cach ngan chan email di vao Spam.",
        "explanation": "<p>SPF, DKIM, DMARC giup email den inbox.</p><h4>SPF</h4><pre>v=spf1 include:_spf.amazonaws.com ~all</pre><h4>DKIM</h4><ul><li>Add DKIM record to DNS</li><li>AWS generates keys</li></ul><h4>DMARC</h4><pre>_dmarc.example.com TXT v=DMARC1; p=quarantine; rua=mailto:reports@example.com</pre>"
    },
    # CloudWatch lessons
    "CloudWatch Service - what/why CloudWatch - Introduction": {
        "summary": "Gioi thieu Amazon CloudWatch.",
        "explanation": "<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics: System/Application metrics</li><li>Logs: Centralized logging</li><li>Alarms: Reactive notifications</li><li>Dashboards: Custom visualizations</li></ul>"
    },
    "CloudWatch Service - Namespace and Custom Dashboard - Introduction": {
        "summary": "Tao CloudWatch Dashboard.",
        "explanation": "<p>Dashboard hien thi metrics theo cach cua ban.</p><h4>Create Dashboard</h4><ol><li>CloudWatch > Dashboards</li><li>Create dashboard</li><li>Add widgets</li></ol><h4>Widgets</h4><ul><li>Line chart</li><li>Number</li><li>Stacked area</li><li>Text</li></ul>"
    },
    "CloudWatch Service - Trigger Alert - Cloudwatch Alarm": {
        "summary": "Tao CloudWatch Alarm.",
        "explanation": "<p>Alarm thong bao khi metrics vuot nguong.</p><h4>Create Alarm</h4><pre>aws cloudwatch put-metric-alarm --alarm-name high-cpu --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold --evaluation-periods 2</pre><h4>Actions</h4><ul><li>SNS notification</li><li>Auto Scaling</li><li>EC2 action</li></ul>"
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
