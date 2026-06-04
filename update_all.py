#!/usr/bin/env python3
"""Fix and update data.js with detailed lesson content"""

with open('data.js', 'r') as f:
    content = f.read()

# Fix syntax errors - add missing quotes
content = content.replace(
    'tải các dịch vụ AWS chính.,',
    'tải các dịch vụ AWS chính.",'
)
content = content.replace(
    'xây dựng hạ tầng.,',
    'xây dựng hạ tầng.",'
)
content = content.replace(
    'trong mỗi mô hình.,',
    'trong mỗi mô hình.",'
)

# Detailed content for all lessons
all_lessons = {
    "Deployment Model of Clouds - Public Private and Hybrid Cloud": {
        "summary": "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud.",
        "explanation": "<p>Bài học này phân tích 3 deployment models của cloud computing và các use cases phù hợp cho từng loại.</p><h4>1. Public Cloud</h4><ul><li><strong>Khái niệm:</strong> Tài nguyên được chia sẻ giữa nhiều organizations, hosted bởi cloud provider</li><li><strong>Ưu điểm:</strong> Chi phí thấp, scale linh hoạt, high availability built-in</li><li><strong>Nhược điểm:</strong> Less control, security concerns cho sensitive data</li><li><strong>Use cases:</strong> Web applications, dev/test environments, startups</li></ul><h4>2. Private Cloud</h4><ul><li><strong>Khái niệm:</strong> Cloud infrastructure dành riêng cho một organization</li><li><strong>Ưu điểm:</strong> Full control, enhanced security</li><li><strong>Nhược điểm:</strong> Higher upfront costs</li><li><strong>Use cases:</strong> Financial services, healthcare, government</li></ul><h4>3. Hybrid Cloud</h4><ul><li><strong>Khái niệm:</strong> Kết hợp public cloud và private cloud</li><li><strong>Ưu điểm:</strong> Flexibility, cost optimization, security</li><li><strong>Use cases:</strong> Web apps on public cloud + databases on private</li></ul>"
    },
    "How Aws Charge - AWS pricing": {
        "summary": "Giải thích cách AWS tính phí và các mô hình pricing: Pay-as-you-go, Reserved Instances, Savings Plans.",
        "explanation": "<p>AWS sử dụng mô hình pricing linh hoạt pay for what you use.</p><h4>AWS Pricing Philosophy</h4><ul><li><strong>Pay for what you use:</strong> Không phí trả trước</li><li><strong>Pay less when you reserve:</strong> Giảm 30-70% với Reserved Instances</li><li><strong>Pay even less with more:</strong> Volume discounts</li></ul><h4>Main Pricing Models</h4><h5>1. On-Demand</h5><ul><li>Không có commitment, trả theo giờ</li><li>Phù hợp cho: Short-term projects, spike workloads</li></ul><h5>2. Reserved Instances</h5><ul><li>Commitment 1-3 years, giảm 30-72%</li></ul><h5>3. Savings Plans</h5><ul><li>Thay thế linh hoạt hơn cho RIs, giảm đến 72%</li></ul><h5>4. Spot Instances</h5><ul><li>Sử dụng unused capacity, giảm đến 90%</li><li>Phù hợp cho: Batch processing, ML training</li></ul><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda (1M requests), DynamoDB (25GB)</li><li><strong>12 Months Free:</strong> EC2 (750h), S3 (5GB)</li></ul>"
    },
    "What/Why is AWS region | AWS Region Map | AWSGlobal Infrastructure": {
        "summary": "Giới thiệu AWS Regions - các vùng địa lý trên toàn thế giới nơi AWS có data centers.",
        "explanation": "<p>AWS Regions là tập hợp các Availability Zones được đặt tại các vị trí địa lý khác nhau trên thế giới.</p><h4>AWS Global Infrastructure</h4><ul><li><strong>Regions:</strong> 33 geographic locations</li><li><strong>Availability Zones:</strong> 105 data centers riêng biệt</li><li><strong>Edge Locations:</strong> 450+ locations cho CDN và DNS</li><li><strong>Local Zones:</strong> Mở rộng AWS closer to users</li></ul><h4>Cách chọn Region</h4><ul><li><strong>Latency:</strong> Chọn region gần users nhất</li><li><strong>Compliance:</strong> Data phải stay in borders</li><li><strong>Cost:</strong> Giá services khác nhau</li></ul><h4>Popular Regions</h4><ul><li><strong>us-east-1:</strong> US East - Most popular, lowest price</li><li><strong>eu-west-1:</strong> Europe Ireland</li><li><strong>ap-southeast-1:</strong> Asia Pacific Singapore</li></ul>"
    },
    "What/Why is AWS Availability Zones | AWS Global Infrastructure": {
        "summary": "Giải thích Availability Zones (AZs) - các data centers riêng biệt trong một Region.",
        "explanation": "<p>Availability Zones (AZs) là các data centers riêng biệt về mặt vật lý nhưng được kết nối với nhau bằng low-latency networking trong một Region.</p><h4>Cấu trúc của Availability Zone</h4><ul><li><strong>Physical Separation:</strong> AZs cách nhau ít nhất 100km</li><li><strong>Independent Power:</strong> Separate power grids, backup generators</li><li><strong>Independent Networking:</strong> Separate ISPs</li><li><strong>Low Latency:</strong> < 1ms giữa các AZs</li></ul><h4>Tại sao AZs quan trọng?</h4><ul><li>Single AZ failure không ảnh hưởng đến các AZs khác</li><li>99.99% SLA với multi-AZ deployments</li><li>Fault isolation khỏi disasters</li></ul><h4>Best Practices</h4><ul><li>Luôn sử dụng at least 2 AZs cho production</li><li>Enable Multi-AZ cho RDS, ElastiCache</li></ul>"
    },
    "What/Why is Local Zones | Local Zones | AWS Global Infrastructure": {
        "summary": "Giới thiệu AWS Local Zones - mở rộng AWS infrastructure closer to users ở các thành phố lớn.",
        "explanation": "<p>AWS Local Zones là các vị trí compute edge được đặt closer to large population centers.</p><h4>So sánh</h4><ul><li><strong>Regions:</strong> Full services, latency 20-100ms</li><li><strong>AZs:</strong> Part of Region, latency < 1ms</li><li><strong>Local Zones:</strong> Extensions, latency < 10ms</li></ul><h4>Use Cases</h4><ul><li><strong>Ultra-low Latency:</strong> Real-time gaming, AR/VR, video conferencing</li><li><strong>Content Delivery:</strong> Streaming media, live sports</li><li><strong>Data Residency:</strong> Regulatory requirements</li></ul><h4>Available Local Zones</h4><ul><li>US: Los Angeles, Boston, Chicago, Dallas, Houston...</li></ul>"
    },
    "Create AWS Account | Create AWS Free Tier Account": {
        "summary": "Hướng dẫn tạo AWS Account mới và kích hoạt Free Tier.",
        "explanation": "<p>Bài học này hướng dẫn step-by-step cách tạo AWS Account mới.</p><h4>Yêu cầu</h4><ul><li>Email address hợp lệ</li><li>Credit/Debit card</li><li>Phone number để xác minh</li></ul><h4>Các bước tạo Account</h4><ol><li>Truy cập aws.amazon.com</li><li>Nhập email và account name</li><li>Xác minh email</li><li>Nhập credit card (AWS sẽ charge $1 để verify)</li><li>Xác minh phone</li><li>Chọn Support Plan (Basic)</li></ol><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda, DynamoDB, SNS, SQS</li><li><strong>12 Months Free:</strong> EC2 (750h), S3 (5GB)</li></ul><h4>Cách tránh charges</h4><ul><li>Set up Billing Alerts</li><li>Delete unused resources</li></ul>"
    },
    "Create First EC2 Instance | EC2 Instance Creation in AWS": {
        "summary": "Hướng dẫn tạo EC2 instance đầu tiên trên AWS Console.",
        "explanation": "<p>Amazon EC2 cung cấp scalable computing capacity trong AWS cloud.</p><h4>EC2 Creation Steps</h4><h5>1. Chọn AMI</h5><ul><li><strong>Amazon Linux 2:</strong> Free tier, RHEL-based</li><li><strong>Ubuntu:</strong> Popular</li></ul><h5>2. Chọn Instance Type</h5><ul><li><strong>t2.micro:</strong> Free tier, 1GB RAM</li></ul><h5>3. Configure</h5><ul><li>Network: VPC và subnet</li><li>Auto-assign Public IP: Enable</li></ul><h5>4. Security Group</h5><ul><li>SSH (22): Linux access</li><li>HTTP (80): Web traffic</li></ul><h5>5. Launch</h5><ul><li>Chọn key pair</li><li>Click Launch</li></ul><h4>Kết nối</h4><pre>ssh -i key.pem ec2-user@public-ip</pre>"
    },
    "Access EC2 Instance From Windows Machine | EC2 Instance Connect": {
        "summary": "Hướng dẫn kết nối đến EC2 instance từ Windows.",
        "explanation": "<p>Có nhiều cách để kết nối đến EC2 Linux instance từ Windows.</p><h4>1. EC2 Instance Connect (Khuyến nghị)</h4><ul><li>Không cần key pair</li><li>SSH keys managed bởi AWS</li><li>AWS Console > EC2 > Connect</li></ul><h4>2. PuTTY</h4><ul><li>Download PuTTYgen</li><li>Convert .pem to .ppk</li><li>Connect: ec2-user@public-ip</li></ul><h4>3. WSL</h4><ul><li>Enable WSL: wsl --install</li><li>ssh -i key.pem ec2-user@public-ip</li></ul><h4>Security</h4><ul><li>Restrict SSH to your IP</li><li>Use Session Manager</li></ul>"
    },
    "Install Nginx in EC2 Instance | Deploy Sample Application In EC2": {
        "summary": "Hướng dẫn cài đặt Nginx web server trên EC2 instance.",
        "explanation": "<p>Bài học này hướng dẫn cách cài đặt Nginx trên EC2 instance.</p><h4>Cài đặt Nginx (Amazon Linux 2)</h4><pre>sudo yum update -y\nsudo amazon-linux-extras install nginx1 -y\nsudo systemctl start nginx\nsudo systemctl enable nginx</pre><h4>Kiểm tra</h4><ul><li>curl http://localhost</li><li>Access via public IP: http://your-public-ip</li></ul><h4>Cấu hình</h4><ul><li><strong>Config:</strong> /etc/nginx/nginx.conf</li><li><strong>Document root:</strong> /usr/share/nginx/html</li></ul><h4>Deploy Sample App</h4><pre>sudo tee /usr/share/nginx/html/index.html << 'EOF'\n<!DOCTYPE html>\n<html><body><h1>Welcome to AWS!</h1></body></html>\nEOF</pre>"
    },
    "AWS Security Group | Security Group AWS": {
        "summary": "Giải thích Security Groups - virtual firewall cho EC2 instances.",
        "explanation": "<p>AWS Security Group là stateful virtual firewall kiểm soát traffic vào và ra cho EC2.</p><h4>Security Group Fundamentals</h4><ul><li><strong>Stateful:</strong> Inbound allowed = Outbound allowed</li><li><strong>Inbound:</strong> Tất cả denied by default</li><li><strong>Outbound:</strong> Tất cả allowed by default</li></ul><h4>Rule Components</h4><ul><li><strong>Type:</strong> SSH, HTTP, HTTPS</li><li><strong>Protocol:</strong> TCP, UDP, ICMP</li><li><strong>Port Range:</strong> Specific port</li><li><strong>Source:</strong> IP, Security Group</li></ul><h4>Best Practices</h4><ul><li>Chỉ allow ports cần thiết</li><li>Use specific IP ranges</li><li>Separate SG by Function</li></ul>"
    },
    "AWS EC2 Instance Type | Instance Type in AWS": {
        "summary": "Tổng quan về các loại EC2 Instance Types.",
        "explanation": "<p>AWS cung cấp hơn 500 instance types được tối ưu cho các use cases khác nhau.</p><h4>EC2 Instance Families</h4><h5>1. General Purpose (T, M)</h5><ul><li><strong>T-Series:</strong> Burstable performance</li><li><strong>M-Series:</strong> Steady-state</li></ul><h5>2. Compute Optimized (C)</h5><ul><li>Use case: Batch processing, ML inference</li></ul><h5>3. Memory Optimized (R, X)</h5><ul><li>Use case: In-memory databases</li></ul><h5>4. Storage Optimized (I, D)</h5><ul><li>Use case: High I/O, data warehousing</li></ul><h5>5. GPU (P, G)</h5><ul><li>Use case: Machine learning</li></ul><h4>Popular Types</h4><ul><li><strong>t3.micro:</strong> Dev/Test</li><li><strong>m5.large:</strong> App Server</li><li><strong>r5.large:</strong> In-Memory DB</li></ul>"
    }
}

# Update all lessons
for title, data in all_lessons.items():
    old_summary_full = f'summary: "Bài học về {title} trong khóa học AWS."'
    new_summary_full = f'summary: "{data["summary"]}"'
    
    old_explanation = f'explanation: `<p>Bài học về {title}. Xem video để hiểu chi tiết.</p>`'
    new_explanation = f'explanation: `{data["explanation"]}`'
    
    if old_summary_full in content:
        content = content.replace(old_summary_full, new_summary_full)
        content = content.replace(old_explanation, new_explanation)
        print(f"Updated: {title}")

with open('data.js', 'w') as f:
    f.write(content)

print("All done!")
