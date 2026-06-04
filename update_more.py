#!/usr/bin/env python3
"""Update data.js with more detailed lesson content"""

with open('data.js', 'r') as f:
    content = f.read()

more_content = {
    "Deployment Model of Clouds - Public Private and Hybrid Cloud": {
        "summary": "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud.",
        "explanation": "<p>Bai hoc nay phan tich 3 deployment models cua cloud computing va cac use cases phu hop cho tung loai.</p><h4>1. Public Cloud</h4><ul><li><strong>Khai niem:</strong> Tai nguyen duoc chia se giua nhieu organizations</li><li><strong>Uu diem:</strong> Chi phi thap, scale linh hoat, high availability</li><li><strong>Nhuoc diem:</strong> Less control, security concerns</li></ul><h4>2. Private Cloud</h4><ul><li><strong>Khai niem:</strong> Cloud infrastructure danh rieng cho mot organization</li><li><strong>Uu diem:</strong> Full control, enhanced security</li><li><strong>Use cases:</strong> Financial services, healthcare, government</li></ul><h4>3. Hybrid Cloud</h4><ul><li><strong>Khai niem:</strong> Ket hop public cloud va private cloud</li><li><strong>Uu diem:</strong> Flexibility, cost optimization</li></ul>"
    },
    "How Aws Charge - AWS pricing": {
        "summary": "Giai thich cach AWS tinh phi va cac mo hinh pricing: Pay-as-you-go, Reserved Instances, Savings Plans.",
        "explanation": "<p>AWS su dung mo hinh pricing linh hoat pay for what you use.</p><h4>AWS Pricing Philosophy</h4><ul><li><strong>Pay for what you use:</strong> Khong phi tra truoc</li><li><strong>Pay less when you reserve:</strong> Giam 30-70% voi Reserved Instances</li></ul><h4>Main Pricing Models</h4><h5>1. On-Demand</h5><ul><li>Khong co commitment, tra theo gio</li></ul><h5>2. Reserved Instances</h5><ul><li>Commitment 1-3 years, giam 30-72%</li></ul><h5>3. Savings Plans</h5><ul><li>Thay the linh hoat hon cho RIs</li></ul><h5>4. Spot Instances</h5><ul><li>Su dung unused capacity, giam den 90%</li></ul><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda, DynamoDB, SNS</li><li><strong>12 Months Free:</strong> EC2, S3</li></ul>"
    },
    "What/Why is AWS region | AWS Region Map | AWSGlobal Infrastructure": {
        "summary": "Gioi thieu AWS Regions - cac vung dia ly tren toan the gioi noi AWS co data centers.",
        "explanation": "<p>AWS Regions la tap hop cac Availability Zones duoc dat tai cac vi tri dia ly khac nhau tren the gioi.</p><h4>AWS Global Infrastructure</h4><ul><li><strong>Regions:</strong> 33 dia diem</li><li><strong>Availability Zones:</strong> 105 data centers</li><li><strong>Edge Locations:</strong> 450+ locations cho CDN</li></ul><h4>Cach chon Region</h4><ul><li><strong>Latency:</strong> Chon region gan users nhat</li><li><strong>Compliance:</strong> Mot so countries yeu cau data stay in borders</li><li><strong>Cost:</strong> Gia services khac nhau giua cac regions</li></ul><h4>Popular Regions</h4><ul><li><strong>us-east-1:</strong> US East - Most popular</li><li><strong>eu-west-1:</strong> Europe Ireland</li></ul>"
    },
    "What/Why is AWS Availability Zones | AWS Global Infrastructure": {
        "summary": "Giai thich Availability Zones (AZs) - cac data centers rieng biet trong mot Region.",
        "explanation": "<p>Availability Zones (AZs) la cac data centers rieng biet ve mat ly nhung duoc ket noi voi nhau bang low-latency networking.</p><h4>Cau truc cua Availability Zone</h4><ul><li><strong>Physical Separation:</strong> AZs cach nhau it nhat 100km</li><li><strong>Independent Power:</strong> Separate power grids</li><li><strong>Independent Networking:</strong> Separate ISPs</li><li><strong>Low Latency:</strong> < 1ms giua cac AZs</li></ul><h4>Tai sao AZs quan trong?</h4><ul><li>Single AZ failure khong anh huong den cac AZs khac</li><li>99.99% SLA voi multi-AZ deployments</li></ul><h4>Best Practices</h4><ul><li>Luon su dung at least 2 AZs</li><li>Enable Multi-AZ cho RDS</li></ul>"
    },
    "What/Why is Local Zones | Local Zones | AWS Global Infrastructure": {
        "summary": "Gioi thieu AWS Local Zones - mo rong AWS infrastructure closer to users.",
        "explanation": "<p>AWS Local Zones la cac vi tri compute edge duoc dat closer to large population centers.</p><h4>So sanh</h4><ul><li><strong>Regions:</strong> Full services, latency 20-100ms</li><li><strong>AZs:</strong> Part of Region, latency < 1ms</li><li><strong>Local Zones:</strong> Extensions, latency < 10ms</li></ul><h4>Use Cases</h4><ul><li><strong>Ultra-low Latency:</strong> Real-time gaming, AR/VR</li><li><strong>Content Delivery:</strong> Streaming media</li><li><strong>Data Residency:</strong> Regulatory requirements</li></ul><h4>Available Local Zones</h4><ul><li>US: Los Angeles, Boston, Chicago, Dallas...</li></ul>"
    },
    "Create AWS Account | Create AWS Free Tier Account": {
        "summary": "Huong dan tao AWS Account moi va kich hoat Free Tier.",
        "explanation": "<p>Bai hoc nay huong dan step-by-step cach tao AWS Account moi.</p><h4>Yeu cau</h4><ul><li>Email address hop le</li><li>Credit/Debit card</li><li>Phone number de xac minh</li></ul><h4>Cac buoc tao Account</h4><ol><li>Truy cap aws.amazon.com</li><li>Nhap email va account name</li><li>Xac minh email</li><li>Nhap credit card</li><li>Xac minh phone</li><li>Chon Support Plan (Basic)</li></ol><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda, DynamoDB, SNS</li><li><strong>12 Months Free:</strong> EC2 (750h), S3 (5GB)</li></ul><h4>Cach tran charges</h4><ul><li>Set up Billing Alerts</li><li>Delete unused resources</li></ul>"
    },
    "Create First EC2 Instance | EC2 Instance Creation in AWS": {
        "summary": "Huong dan tao EC2 instance dau tien tren AWS Console.",
        "explanation": "<p>Amazon EC2 cung cap scalable computing capacity trong AWS cloud.</p><h4>EC2 Creation Steps</h4><h5>1. Chon AMI</h5><ul><li><strong>Amazon Linux 2:</strong> Free tier, RHEL-based</li><li><strong>Ubuntu:</strong> Popular</li></ul><h5>2. Chon Instance Type</h5><ul><li><strong>t2.micro:</strong> Free tier, 1GB RAM</li></ul><h5>3. Configure</h5><ul><li>Network: VPC va subnet</li><li>Auto-assign Public IP: Enable</li></ul><h5>4. Security Group</h5><ul><li>SSH (22): Linux access</li><li>HTTP (80): Web traffic</li></ul><h5>5. Launch</h5><ul><li>Chon key pair</li><li>Click Launch</li></ul><h4>Ket noi</h4><pre>ssh -i key.pem ec2-user@public-ip</pre>"
    },
    "Access EC2 Instance From Windows Machine | EC2 Instance Connect": {
        "summary": "Huong dan ket noi den EC2 instance tu Windows.",
        "explanation": "<p>Co nhieu cach de ket noi den EC2 Linux instance tu Windows.</p><h4>1. EC2 Instance Connect (Khuyen nghi)</h4><ul><li>Khong can key pair</li><li>SSH keys managed boi AWS</li><li>AWS Console > EC2 > Connect</li></ul><h4>2. PuTTY</h4><ul><li>Download PuTTYgen</li><li>Convert .pem to .ppk</li><li>Connect: ec2-user@public-ip</li></ul><h4>3. WSL</h4><ul><li>Enable WSL: wsl --install</li><li>ssh -i key.pem ec2-user@public-ip</li></ul><h4>Security</h4><ul><li>Restrict SSH to your IP</li><li>Use Session Manager</li></ul>"
    },
    "AWS Security Group | Security Group AWS": {
        "summary": "Giai thich ve Security Groups - virtual firewall cho EC2 instances.",
        "explanation": "<p>AWS Security Group la stateful virtual firewall kiem soat traffic vao va ra cho EC2.</p><h4>Security Group Fundamentals</h4><ul><li><strong>Stateful:</strong> Inbound allowed = Outbound allowed</li><li><strong>Inbound:</strong> Tat ca denied by default</li><li><strong>Outbound:</strong> Tat ca allowed by default</li></ul><h4>Rule Components</h4><ul><li><strong>Type:</strong> SSH, HTTP, HTTPS</li><li><strong>Protocol:</strong> TCP, UDP, ICMP</li><li><strong>Port Range:</strong> Specific port</li><li><strong>Source:</strong> IP, Security Group</li></ul><h4>Best Practices</h4><ul><li>Chi allow ports can thiet</li><li>Use specific IP ranges</li><li>Separate SG by Function</li></ul>"
    },
    "AWS EC2 Instance Type | Instance Type in AWS": {
        "summary": "Tong quan ve cac loai EC2 Instance Types.",
        "explanation": "<p>AWS cung cap hon 500 instance types duoc toi uu cho cac use cases khac nhau.</p><h4>EC2 Instance Families</h4><h5>1. General Purpose (T, M)</h5><ul><li><strong>T-Series:</strong> Burstable performance</li><li><strong>M-Series:</strong> Steady-state</li></ul><h5>2. Compute Optimized (C)</h5><ul><li>Use case: Batch processing, ML inference</li></ul><h5>3. Memory Optimized (R, X)</h5><ul><li>Use case: In-memory databases</li></ul><h5>4. Storage Optimized (I, D)</h5><ul><li>Use case: High I/O, data warehousing</li></ul><h5>5. GPU (P, G)</h5><ul><li>Use case: Machine learning</li></ul><h4>Popular Types</h4><ul><li><strong>t3.micro:</strong> Dev/Test</li><li><strong>m5.large:</strong> App Server</li><li><strong>r5.large:</strong> In-Memory DB</li></ul>"
    }
}

for title, data in more_content.items():
    old_summary_full = 'summary: "Bai hoc ve ' + title + ' trong khoa hoc AWS."'
    new_summary_full = 'summary: "' + data["summary"] + '"'
    
    old_explanation = 'explanation: `<p>Bai hoc ve ' + title + '. Xem video de hieu chi tiet.</p>`'
    new_explanation = 'explanation: `' + data["explanation"] + '`'
    
    if old_summary_full in content:
        content = content.replace(old_summary_full, new_summary_full)
        content = content.replace(old_explanation, new_explanation)
        print(f"Updated: {title}")

with open('data.js', 'w') as f:
    f.write(content)

print("Done!")
