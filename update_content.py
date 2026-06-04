#!/usr/bin/env python3
"""
Update data.js with detailed lesson content matching video content.
This script replaces placeholder content with comprehensive explanations.
"""

detailed_content = {
    "Introducing the AWS Playlist": {
        "summary": "Video giới thiệu tổng quan khóa học AWS Tutorials bằng tiếng Hindi. Gaurav Sharma giới thiệu về playlist học AWS từ cơ bản đến nâng cao, bao gồm hơn 180 bài học covering tất cả các dịch vụ AWS chính.",
        "explanation": """<p>Khóa học AWS Tutorials của Gaurav Sharma là một trong những khóa học AWS miễn phí toàn diện nhất bằng tiếng Hindi, với hơn 180 bài học và 35+ giờ video content.</p>
<h4>Nội dung khóa học bao gồm:</h4>
<ul>
<li><strong>Phần 1: Giới thiệu AWS</strong> - Cloud Computing, AWS Infrastructure, Regions, Availability Zones</li>
<li><strong>Phần 2: Amazon EC2</strong> - Virtual Servers, Instance Types, Security Groups, SSH Access</li>
<li><strong>Phần 3: EBS & Storage</strong> - Elastic Block Store, Snapshots, Volume Types</li>
<li><strong>Phần 4: Load Balancer & Auto Scaling</strong> - ELB, ALB, NLB, ASG</li>
<li><strong>Phần 5: IAM</strong> - Identity & Access Management, Users, Groups, Roles, Policies</li>
<li><strong>Phần 6: Amazon S3</strong> - Object Storage, Bucket Policies, Versioning, Lifecycle</li>
<li><strong>Phần 7: CloudFront CDN</strong> - Content Delivery Network, Edge Locations</li>
<li><strong>Phần 8: Amazon VPC</strong> - Virtual Private Cloud, Subnets, NAT Gateway</li>
<li><strong>Phần 9: Route 53</strong> - DNS Service, Routing Policies, Health Checks</li>
<li><strong>Phần 10: RDS & DynamoDB</strong> - Managed Databases, Aurora, NoSQL</li>
<li><strong>Phần 11: Lambda</strong> - Serverless Computing, Function Development</li>
<li><strong>Phần 12: API Gateway</strong> - REST APIs, HTTP APIs, Integrations</li>
<li><strong>Phần 13: Cognito</strong> - Authentication, User Pools, Identity Pools</li>
<li><strong>Phần 14: ECS</strong> - Container Orchestration, Docker, Fargate</li>
</ul>
<h4>Ưu điểm của khóa học:</h4>
<ul>
<li>Hoàn toàn miễn phí trên YouTube</li>
<li>Giảng dạy bằng tiếng Hindi, dễ hiểu cho người Việt</li>
<li>Thực hành step-by-step với AWS Console</li>
<li>Cập nhật liên tục với các dịch vụ AWS mới</li>
<li>Phù hợp cho người mới bắt đầu và người ôn tập AWS Certification</li>
</ul>"""
    },
    "What is AWS - Traditional VS Cloud Computing - Why Cloud Computing": {
        "summary": "So sánh giữa Traditional Computing (On-premise) và Cloud Computing. Giải thích tại sao Cloud Computing là xu hướng tất yếu và lợi ích của việc sử dụng AWS thay vì tự xây dựng hạ tầng.",
        "explanation": """<p>Trong bài học này, Gaurav Sharma giải thích sự khác biệt cơ bản giữa Traditional Computing (điện toán truyền thống) và Cloud Computing (điện toán đám mây).</p>
<h4>Traditional Computing (On-Premise)</h4>
<ul>
<li><strong>Capital Expenditure (CapEx):</strong> Cần đầu tư ban đầu lớn cho server, network equipment, storage</li>
<li><strong>Thời gian triển khai:</strong> Có thể mất vài tuần đến vài tháng để setup</li>
<li><strong>Quản lý và bảo trì:</strong> Cần đội ngũ kỹ thuật riêng cho hardware, OS, patches</li>
<li><strong>Mở rộng (Scaling):</strong> Khó khăn và tốn kém khi cần scale up/down</li>
<li><strong>Rủi ro:</strong> Over-provisioning gây lãng phí, Under-provisioning gây downtime</li>
</ul>
<h4>Cloud Computing</h4>
<ul>
<li><strong>Operational Expenditure (OpEx):</strong> Chỉ trả tiền cho những gì sử dụng (Pay-as-you-go)</li>
<li><strong>Thời gian triển khai:</strong> Có thể launch trong vài phút</li>
<li><strong>Quản lý:</strong> AWS quản lý infrastructure, bạn tập trung vào ứng dụng</li>
<li><strong>Mở rộng:</strong> Tự động scale theo demand trong vài giây</li>
<li><strong>Độ tin cậy:</strong> 99.99% uptime với multiple Availability Zones</li>
</ul>
<h4>Tại sao nên chọn AWS?</h4>
<ul>
<li><strong>Market Leader:</strong> AWS chiếm 32% thị phần cloud computing toàn cầu</li>
<li><strong>200+ Services:</strong> Cung cấp hơn 200 dịch vụ từ compute, storage, database, AI, IoT</li>
<li><strong>Global Infrastructure:</strong> 33 Regions, 105 Availability Zones</li>
<li><strong>Security:</strong> Đạt nhiều compliance certifications (SOC, HIPAA, PCI, ISO)</li>
<li><strong>Community:</strong> Hệ sinh thái lớn với documentation, tutorials, partners</li>
</ul>
<h4>Cloud Service Models</h4>
<ul>
<li><strong>IaaS:</strong> Infrastructure as a Service (EC2, S3) - Kiểm soát OS, storage</li>
<li><strong>PaaS:</strong> Platform as a Service (Beanstalk, Lambda) - Không quản lý infrastructure</li>
<li><strong>SaaS:</strong> Software as a Service (Google Workspace, Salesforce) - Ứng dụng hoàn chỉnh</li>
</ul>"""
    },
    "Cloud Computing Service Models | IAAS | PAAS | SAAS": {
        "summary": "Giải thích chi tiết 3 mô hình dịch vụ đám mây: IaaS, PaaS, và SaaS. So sánh vị trí kiểm soát của khách hàng trong mỗi mô hình.",
        "explanation": """<p>Bài học này đi sâu vào 3 mô hình dịch vụ cloud computing và vị trí kiểm soát (control) của khách hàng trong mỗi mô hình.</p>
<h4>1. IaaS (Infrastructure as a Service)</h4>
<ul>
<li><strong>Khái niệm:</strong> Cung cấp tài nguyên hạ tầng ảo hóa: servers, storage, networking</li>
<li><strong>Ví dụ AWS:</strong> Amazon EC2, Amazon S3, Amazon VPC, EBS</li>
<li><strong>Bạn quản lý:</strong> OS, applications, data, runtime</li>
<li><strong>AWS quản lý:</strong> Physical servers, data center, virtualization layer</li>
<li><strong>Use cases:</strong> Migration từ on-premise, lift-and-shift applications</li>
</ul>
<h4>2. PaaS (Platform as a Service)</h4>
<ul>
<li><strong>Khái niệm:</strong> Cung cấp nền tảng để phát triển và deploy ứng dụng</li>
<li><strong>Ví dụ AWS:</strong> AWS Elastic Beanstalk, AWS Lambda, Amazon RDS, AWS Glue</li>
<li><strong>Bạn quản lý:</strong> Applications, data</li>
<li><strong>AWS quản lý:</strong> OS, runtime, middleware, development tools</li>
<li><strong>Use cases:</strong> Web applications, API development, microservices</li>
</ul>
<h4>3. SaaS (Software as a Service)</h4>
<ul>
<li><strong>Khái niệm:</strong> Ứng dụng hoàn chỉnh chạy trên cloud, access qua internet</li>
<li><strong>Ví dụ AWS:</strong> Amazon Chime, AWS Connect, Amazon WorkSpaces</li>
<li><strong>Bạn quản lý:</strong> Data (trong một số trường hợp)</li>
<li><strong>NCC quản lý:</strong> Tất cả - từ infrastructure đến ứng dụng</li>
<li><strong>Use cases:</strong> Email, CRM, collaboration tools, communication</li>
</ul>
<h4>So sánh vị trí Control</h4>
<ul>
<li><strong>On-Premise:</strong> Bạn kiểm soát mọi thứ từ hardware đến applications</li>
<li><strong>IaaS:</strong> Bạn kiểm soát OS, applications, data; AWS kiểm soát virtualization và hardware</li>
<li><strong>PaaS:</strong> Bạn kiểm soát applications và data; AWS kiểm soát OS, runtime, middleware</li>
<li><strong>SaaS:</strong> AWS kiểm soát mọi thứ; bạn chỉ sử dụng ứng dụng</li>
</ul>"""
    },
    "Deployment Model of Clouds - Public Private and Hybrid Cloud": {
        "summary": "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud. Giải thích khi nào nên sử dụng từng loại.",
        "explanation": """<p>Bài học này phân tích 3 deployment models (mô hình triển khai) của cloud computing và các use cases phù hợp cho từng loại.</p>
<h4>1. Public Cloud</h4>
<ul>
<li><strong>Khái niệm:</strong> Tài nguyên được chia sẻ giữa nhiều organizations, hosted bởi cloud provider (AWS, Azure, GCP)</li>
<li><strong>Ưu điểm:</strong> Chi phí thấp (pay-as-you-go), không cần quản lý infrastructure, scale linh hoạt</li>
<li><strong>Nhược điểm:</strong> Less control, security concerns cho sensitive data</li>
<li><strong>Use cases:</strong> Web applications, development/test environments, startups</li>
</ul>
<h4>2. Private Cloud</h4>
<ul>
<li><strong>Khái niệm:</strong> Cloud infrastructure dành riêng cho một organization</li>
<li><strong>Ưu điểm:</strong> Full control, enhanced security, consistent với on-premise</li>
<li><strong>Nhược điểm:</strong> Higher upfront costs, requires technical expertise</li>
<li><strong>Use cases:</strong> Financial services, healthcare, government, enterprises</li>
</ul>
<h4>3. Hybrid Cloud</h4>
<ul>
<li><strong>Khái niệm:</strong> Kết hợp public cloud và private cloud</li>
<li><strong>Ưu điểm:</strong> Flexibility, cost optimization, security cho sensitive data</li>
<li><strong>Use cases:</strong> Web apps on public cloud + databases on private</li>
</ul>
<h4>4. Multi-Cloud</h4>
<ul>
<li><strong>Khái niệm:</strong> Sử dụng multiple cloud providers (AWS + Azure + GCP)</li>
<li><strong>Ưu điểm:</strong> Vendor independence, avoid lock-in</li>
<li><strong>Thách thức:</strong> Complexity in management</li>
</ul>"""
    },
    "How Aws Charge - AWS pricing": {
        "summary": "Giải thích cách AWS tính phí và các mô hình pricing: Pay-as-you-go, Reserved Instances, Savings Plans, Spot Instances.",
        "explanation": """<p>AWS sử dụng mô hình pricing linh hoạt "pay for what you use". Bài học này giải thích các cách tính phí và chiến lược tối ưu chi phí.</p>
<h4>AWS Pricing Philosophy</h4>
<ul>
<li><strong>Pay for what you use:</strong> Không phí trả trước, không chi phí ẩn</li>
<li><strong>Pay less when you reserve:</strong> Giảm 30-70% với Reserved Instances</li>
<li><strong>Pay even less with more:</strong> Volume discounts khi sử dụng nhiều hơn</li>
</ul>
<h4>Main Pricing Models</h4>
<h5>1. On-Demand</h5>
<ul>
<li>Không có commitment, trả theo giờ</li>
<li>Phù hợp cho: Short-term projects, spike workloads</li>
</ul>
<h5>2. Reserved Instances (RI)</h5>
<ul>
<li>Commitment 1 hoặc 3 years, giảm 30-72%</li>
<li>Phù hợp cho: Baseline workloads, production systems</li>
</ul>
<h5>3. Savings Plans</h5>
<ul>
<li>Thay thế linh hoạt hơn cho RIs, giảm đến 72%</li>
</ul>
<h5>4. Spot Instances</h5>
<ul>
<li>Sử dụng unused EC2 capacity, giảm đến 90%</li>
<li>Có thể bị interrupted bất cứ lúc nào</li>
<li>Phù hợp cho: Batch processing, ML training</li>
</ul>
<h4>AWS Free Tier</h4>
<ul>
<li><strong>Always Free:</strong> Lambda (1M requests/month), DynamoDB (25GB)</li>
<li><strong>12 Months Free:</strong> EC2 (750h t2.micro), S3 (5GB)</li>
</ul>
<h4>Cost Optimization Tips</h4>
<ul>
<li>Use Cost Explorer để monitor spending</li>
<li>Set up Budgets với alerts</li>
<li>Right-size instances (đừng over-provision)</li>
<li>Delete unused resources</li>
</ul>"""
    },
    "What/Why is AWS region | AWS Region Map | AWSGlobal Infrastructure": {
        "summary": "Giới thiệu AWS Regions - các vùng địa lý trên toàn thế giới nơi AWS có data centers. Cách chọn region phù hợp.",
        "explanation": """<p>AWS Regions là tập hợp các Availability Zones được đặt tại các vị trí địa lý khác nhau trên thế giới.</p>
<h4>AWS Global Infrastructure</h4>
<ul>
<li><strong>Regions:</strong> 33 geographic locations</li>
<li><strong>Availability Zones:</strong> 105 data centers riêng biệt</li>
<li><strong>Edge Locations:</strong> 450+ locations cho CDN và DNS</li>
<li><strong>Local Zones:</strong> Mở rộng AWS closer to users</li>
</ul>
<h4>Cách chọn Region</h4>
<h5>1. Latency</h5>
<ul>
<li>Chọn region gần users nhất để giảm latency</li>
<li>Sử dụng Route 53 Latency Routing để auto-route</li>
</ul>
<h5>2. Compliance & Data Sovereignty</h5>
<ul>
<li>Một số countries có yêu cầu data phải stay trong borders</li>
<li>GDPR: Data of EU citizens phải stay in EU</li>
</ul>
<h5>3. Service Availability</h5>
<ul>
<li>Một số services không có sẵn ở tất cả regions</li>
</ul>
<h5>4. Cost</h5>
<ul>
<li>Giá services khác nhau giữa các regions</li>
<li>Ví dụ: us-east-1 thường rẻ hơn</li>
</ul>
<h4>Popular Regions</h4>
<ul>
<li><strong>us-east-1:</strong> US East (N. Virginia) - Most popular, lowest price</li>
<li><strong>us-west-2:</strong> US West (Oregon) - West coast US</li>
<li><strong>eu-west-1:</strong> Europe (Ireland) - EU presence</li>
<li><strong>ap-southeast-1:</strong> Asia Pacific (Singapore) - APAC</li>
</ul>"""
    },
    "What/Why is AWS Availability Zones | AWS Global Infrastructure": {
        "summary": "Giải thích Availability Zones (AZs) - các data centers riêng biệt trong một Region. Tại sao AZs quan trọng cho high availability.",
        "explanation": """<p>Availability Zones (AZs) là các data centers riêng biệt về mặt vật lý nhưng được kết nối với nhau bằng low-latency networking trong một Region.</p>
<h4>Cấu trúc của Availability Zone</h4>
<ul>
<li><strong>Physical Separation:</strong> AZs cách nhau ít nhất 100km</li>
<li><strong>Independent Power:</strong> Separate power grids, backup generators</li>
<li><strong>Independent Networking:</strong> Separate ISPs, redundant network paths</li>
<li><strong>Low Latency Connection:</strong> < 1ms latency giữa các AZs</li>
</ul>
<h4>Tại sao Availability Zones quan trọng?</h4>
<h5>1. High Availability</h5>
<ul>
<li>Single AZ failure không ảnh hưởng đến các AZs khác</li>
<li>Application có thể failover sang AZ khác</li>
<li>99.99% SLA với multi-AZ deployments</li>
</ul>
<h5>2. Fault Isolation</h5>
<ul>
<li>Natural disasters, hardware failures, network outages chỉ ảnh hưởng 1 AZ</li>
</ul>
<h4>Best Practices</h4>
<ul>
<li><strong>Luôn sử dụng at least 2 AZs</strong> cho production workloads</li>
<li><strong>Use Load Balancers</strong> để distribute traffic</li>
<li><strong>Enable Multi-AZ</strong> cho RDS, ElastiCache</li>
<li><strong>Don't put all resources in one AZ</strong></li>
</ul>
<h4>SLA và Credits</h4>
<ul>
<li>Single AZ: 99.5% uptime</li>
<li>Multi-AZ: 99.99% uptime</li>
<li>Nếu không đạt SLA, AWS cấp service credits</li>
</ul>"""
    },
    "What/Why is Local Zones | Local Zones | AWS Global Infrastructure": {
        "summary": "Giới thiệu AWS Local Zones - mở rộng AWS infrastructure closer to users ở các thành phố lớn.",
        "explanation": """<p>AWS Local Zones là các vị trí compute edge được đặt closer to large population centers, cho phép run latency-sensitive applications gần users hơn.</p>
<h4>AWS Local Zones vs Regions vs Edge Locations</h4>
<h5>Regions</h5>
<ul>
<li>Geographic areas chứa multiple Availability Zones</li>
<li>Full AWS services portfolio</li>
<li>Latency: 20-100ms tùy location</li>
</ul>
<h5>Availability Zones</h5>
<ul>
<li>Data centers trong một Region</li>
<li>Part of Region, same services</li>
<li>Latency: < 1ms</li>
</ul>
<h5>Local Zones</h5>
<ul>
<li>Extensions of a Region</li>
<li>Subset of AWS services</li>
<li>Latency: < 10ms cho end users</li>
<li>Ví dụ: Los Angeles, Boston, Chicago, Dallas</li>
</ul>
<h4>Use Cases cho Local Zones</h4>
<ul>
<li><strong>Ultra-low Latency Applications:</strong> Real-time gaming, video conferencing, AR/VR</li>
<li><strong>Content Delivery:</strong> Streaming media, live sports events</li>
<li><strong>Data Residency:</strong> Regulatory requirements cần data stay in specific location</li>
</ul>
<h4>Available Local Zones (2024)</h4>
<ul>
<li>US: Los Angeles, Boston, Chicago, Dallas, Denver, Houston, Miami, Phoenix, Seattle...</li>
</ul>"""
    },
    "Create AWS Account | Create AWS Free Tier Account": {
        "summary": "Hướng dẫn tạo AWS Account mới và kích hoạt Free Tier. Cách tránh charges không mong muốn.",
        "explanation": """<p>Bài học này hướng dẫn step-by-step cách tạo AWS Account mới và kích hoạt Free Tier để bắt đầu học AWS miễn phí.</p>
<h4>Yêu cầu trước khi tạo Account</h4>
<ul>
<li>Email address hợp lệ</li>
<li>Credit/Debit card (Visa, Mastercard, hoặc American Express)</li>
<li>Phone number để xác minh</li>
</ul>
<h4>Các bước tạo AWS Account</h4>
<ol>
<li><strong>Bước 1:</strong> Truy cập aws.amazon.com > Create an AWS Account</li>
<li><strong>Bước 2:</strong> Nhập email và AWS account name</li>
<li><strong>Bước 3:</strong> Xác minh identity qua email</li>
<li><strong>Bước 4:</strong> Nhập thông tin cá nhân</li>
<li><strong>Bước 5:</strong> Nhập credit card (AWS sẽ charge $1 để verify)</li>
<li><strong>Bước 6:</strong> Xác minh phone qua SMS/voice call</li>
<li><strong>Bước 7:</strong> Chọn Support Plan (chọn Basic - miễn phí)</li>
</ol>
<h4>AWS Free Tier Details</h4>
<h5>Always Free (Không bao giờ hết hạn)</h5>
<ul>
<li>Lambda: 1M requests/month</li>
<li>DynamoDB: 25GB storage</li>
<li>SNS: 1M publishes</li>
<li>SQS: 1M requests</li>
</ul>
<h5>12 Months Free</h5>
<ul>
<li>EC2: 750 hours t2.micro/tháng</li>
<li>S3: 5GB standard storage</li>
<li>RDS: 750 hours db.t2.micro</li>
</ul>
<h4>Cách tránh charges không mong muốn</h4>
<ul>
<li>Set up Billing Alerts trong CloudWatch</li>
<li>Use AWS Budgets với alerts</li>
<li>Delete unused resources (EC2, EBS, RDS)</li>
<li>Use Cost Explorer để monitor spending</li>
</ul>
<h4>Root Account Security</h4>
<ul>
<li><strong>Enable MFA</strong> immediately after creating account</li>
<li><strong>Don't use root account</strong> for daily tasks</li>
</ul>"""
    },
    "Create First EC2 Instance | EC2 Instance Creation in AWS": {
        "summary": "Hướng dẫn step-by-step cách tạo EC2 instance đầu tiên trên AWS Console. Bao gồm chọn AMI, instance type, configure network.",
        "explanation": """<p>Amazon EC2 (Elastic Compute Cloud) cung cấp scalable computing capacity trong AWS cloud. Bài học này hướng dẫn cách tạo EC2 instance đầu tiên.</p>
<h4>EC2 Instance Creation Steps</h4>
<h5>Bước 1: Chọn AMI (Amazon Machine Image)</h5>
<ul>
<li><strong>Amazon Linux 2 AMI:</strong> Free tier eligible, RHEL-based</li>
<li><strong>Ubuntu Server:</strong> Popular, good community support</li>
<li><strong>Windows Server:</strong> For Windows workloads</li>
</ul>
<h5>Bước 2: Chọn Instance Type</h5>
<ul>
<li><strong>t2.micro:</strong> Free tier, 1 vCPU, 1GB RAM</li>
<li><strong>t3.micro:</strong> 2 vCPU, 1GB RAM</li>
<li><strong>m5.large:</strong> 2 vCPU, 8GB RAM</li>
</ul>
<h5>Bước 3: Configure Instance Details</h5>
<ul>
<li>Network: VPC và subnet</li>
<li>Auto-assign Public IP: Enable</li>
<li>Shutdown behavior: Stop hoặc Terminate</li>
<li>Enable termination protection</li>
</ul>
<h5>Bước 4: Add Storage</h5>
<ul>
<li>Root volume: thường 8GB-30GB</li>
<li>Volume type: gp3 (general purpose SSD)</li>
</ul>
<h5>Bước 5: Configure Security Group</h5>
<ul>
<li>SSH (port 22): Cho Linux access</li>
<li>HTTP (port 80): Web traffic</li>
<li>HTTPS (port 443): Secure web traffic</li>
</ul>
<h5>Bước 6: Review và Launch</h5>
<ul>
<li>Review tất cả settings</li>
<li>Chọn hoặc tạo key pair</li>
<li>Click "Launch Instances"</li>
</ul>
<h4>Kết nối đến EC2 Instance</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Linux/Mac
ssh -i your-key.pem ec2-user@your-public-ip

# Windows (PowerShell)
ssh -i your-key.pem ec2-user@your-public-ip
</pre>
<h4>Common EC2 Instance States</h4>
<ul>
<li><strong>pending:</strong> Đang khởi tạo</li>
<li><strong>running:</strong> Đang chạy</li>
<li><strong>stopped:</strong> Đã dừng (không charge compute)</li>
<li><strong>terminated:</strong> Đã xóa (không thể recover)</li>
</ul>"""
    },
    "Access EC2 Instance From Windows Machine | EC2 Instance Connect": {
        "summary": "Hướng dẫn kết nối đến EC2 instance từ Windows sử dụng EC2 Instance Connect, PuTTY, và WSL.",
        "explanation": """<p>Có nhiều cách để kết nối đến EC2 Linux instance từ Windows machine.</p>
<h4>Phương pháp 1: EC2 Instance Connect (Khuyến nghị)</h4>
<ul>
<li>Không cần key pair - sử dụng browser</li>
<li>SSH keys được managed bởi AWS</li>
<li>AWS Console > EC2 > Instances > Connect > EC2 Instance Connect</li>
</ul>
<h4>Phương pháp 2: PuTTY</h4>
<ol>
<li>Download PuTTY và PuTTYgen</li>
<li>Convert .pem to .ppk using PuTTYgen</li>
<li>Connect với PuTTY: Host Name = ec2-user@public-ip</li>
</ol>
<h4>Phương pháp 3: Windows Subsystem for Linux (WSL)</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Enable WSL in PowerShell (Admin)
wsl --install

# Connect SSH
ssh -i key.pem ec2-user@public-ip
</pre>
<h4>Security Best Practices</h4>
<ul>
<li>Restrict SSH to your IP only trong Security Group</li>
<li>Use Session Manager thay vì SSH (không cần public IP)</li>
<li>Enable Connection Limiting</li>
</ul>
<h4>Troubleshooting</h4>
<ul>
<li><strong>Connection Timeout:</strong> Check Security Group allows SSH (port 22)</li>
<li><strong>Permission Denied:</strong> Verify key pair, check file permissions (chmod 400)</li>
</ul>"""
    },
    "Install Nginx in EC2 Instance | Deploy Sample Application In EC2": {
        "summary": "Hướng dẫn cài đặt Nginx web server trên EC2 instance và deploy một sample application.",
        "explanation": """<p>Bài học này hướng dẫn cách cài đặt Nginx - một trong những web server phổ biến nhất - trên EC2 instance.</p>
<h4>Cài đặt Nginx trên Amazon Linux 2</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Update packages
sudo yum update -y

# Install Nginx
sudo amazon-linux-extras install nginx1 -y

# Start Nginx
sudo systemctl start nginx

# Enable Nginx on boot
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
</pre>
<h4>Kiểm tra Nginx</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Test locally
curl http://localhost

# Get public IP
curl ifconfig.me

# Access from browser
http://your-public-ip
</pre>
<h4>Cấu hình Firewall (nếu cần)</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Check firewall status
sudo systemctl status firewalld

# Allow HTTP/HTTPS
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
</pre>
<h4>Cấu hình Nginx</h4>
<ul>
<li><strong>Config file:</strong> /etc/nginx/nginx.conf</li>
<li><strong>Default site:</strong> /etc/nginx/conf.d/default.conf</li>
<li><strong>Document root:</strong> /usr/share/nginx/html</li>
</ul>
<h4>Deploy Sample Application</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
# Create sample HTML
sudo tee /usr/share/nginx/html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Welcome to AWS!</title></head>
<body>
<h1>EC2 Instance is running!</h1>
<p>This is a sample application deployed on Nginx.</p>
</body>
</html>
EOF
</pre>"""
    },
    "AWS Security Group | Security Group AWS": {
        "summary": "Giải thích chi tiết về Security Groups - virtual firewall cho EC2 instances. Cách tạo, configure, và best practices.",
        "explanation": """<p>AWS Security Group là một stateful virtual firewall kiểm soát traffic vào và ra cho EC2 instances.</p>
<h4>Security Group Fundamentals</h4>
<ul>
<li><strong>Stateful:</strong> Nếu inbound được allowed, outbound response cũng được allowed tự động</li>
<li><strong>Inbound:</strong> Tất cả denied by default</li>
<li><strong>Outbound:</strong> Tất cả allowed by default</li>
</ul>
<h4>Rule Components</h4>
<ul>
<li><strong>Type:</strong> SSH, HTTP, HTTPS, Custom TCP</li>
<li><strong>Protocol:</strong> TCP, UDP, ICMP</li>
<li><strong>Port Range:</strong> Specific port hoặc range</li>
<li><strong>Source:</strong> IP Address, Security Group, Prefix List</li>
</ul>
<h4>Common Security Group Configurations</h4>
<h5>Web Server Security Group</h5>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
Inbound Rules:
┌─────────┬────────┬──────────────┐
│  Type   │ Port   │ Source       │
├─────────┼────────┼──────────────┤
│ SSH     │ 22     │ My IP        │
│ HTTP    │ 80     │ 0.0.0.0/0   │
│ HTTPS   │ 443    │ 0.0.0.0/0   │
└─────────┴────────┴──────────────┘
</pre>
<h4>Best Practices</h4>
<ul>
<li>Chỉ allow những ports cần thiết</li>
<li>Use specific IP ranges thay vì 0.0.0.0/0</li>
<li>Restrict admin access đến known IPs</li>
<li>Use Security Groups as Source (self-reference)</li>
<li>Separate Security Groups by Function</li>
</ul>
<h4>Security Group vs NACLs</h4>
<ul>
<li><strong>Security Group:</strong> Instance level, stateful</li>
<li><strong>NACL:</strong> Subnet level, stateless</li>
</ul>"""
    },
    "AWS EC2 Instance Type | Instance Type in AWS": {
        "summary": "Tổng quan về các loại EC2 Instance Types: General Purpose, Compute, Memory, Storage Optimized. Cách chọn instance type phù hợp.",
        "explanation": """<p>AWS cung cấp hơn 500 instance types được tối ưu cho các use cases khác nhau.</p>
<h4>EC2 Instance Families</h4>
<h5>1. General Purpose (T, M)</h5>
<ul>
<li><strong>Use case:</strong> Web servers, development environments</li>
<li><strong>T-Series:</strong> Burstable performance, phù hợp cho variable workloads</li>
<li><strong>M-Series:</strong> Steady-state performance</li>
</ul>
<h5>2. Compute Optimized (C)</h5>
<ul>
<li><strong>Use case:</strong> Batch processing, ML inference, video encoding</li>
<li><strong>Types:</strong> C5, C6i, C7g</li>
</ul>
<h5>3. Memory Optimized (R, X)</h5>
<ul>
<li><strong>Use case:</strong> In-memory databases, big data analytics</li>
<li><strong>Types:</strong> R6i, R7g, X2gd</li>
</ul>
<h5>4. Storage Optimized (I, D)</h5>
<ul>
<li><strong>Use case:</strong> High-frequency read/write, data warehousing</li>
<li><strong>Types:</strong> I4i, I3, D2</li>
</ul>
<h5>5. Accelerated Computing (P, G)</h5>
<ul>
<li><strong>Use case:</strong> Machine learning, graphics-intensive</li>
<li><strong>Types:</strong> P4d (A100 GPU), G5 (T4 GPU)</li>
</ul>
<h4>Instance Naming Convention</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
m6i.xlarge
│ │ │ └── Size: nano, micro, small, large, xlarge...
│ │ └── Generation: 6
│ └── Family: i (compute optimized)
└── Prefix: m (general purpose)
</pre>
<h4>Comparing Popular Instance Types</h4>
<table>
<tr><th>Instance</th><th>vCPU</th><th>Memory</th><th>Use Case</th></tr>
<tr><td>t3.micro</td><td>2</td><td>1 GB</td><td>Dev/Test</td></tr>
<tr><td>m5.large</td><td>2</td><td>8 GB</td><td>App Server</td></tr>
<tr><td>c5.large</td><td>2</td><td>4 GB</td><td>Compute</td></tr>
<tr><td>r5.large</td><td>2</td><td>16 GB</td><td>In-Memory DB</td></tr>
</table>
<h4>How to Choose</h4>
<ul>
<li>Analyze workload: CPU-bound or Memory-bound?</li>
<li>Start với smaller instance, monitor và scale up</li>
<li>Use AWS Compute Optimizer để recommend</li>
</ul>"""
    },
    "Elastic Block Storage (EBS) | Instance Store | AWS Step By Step": {
        "summary": "Giới thiệu về Amazon EBS - block storage cho EC2 instances. So sánh EBS với Instance Store và các loại EBS volumes.",
        "explanation": """<p>Amazon Elastic Block Store (EBS) cung cấp block storage volumes có độ bền cao cho use với EC2 instances.</p>
<h4>EBS vs Instance Store</h4>
<h5>EBS Volumes</h5>
<ul>
<li>Independent of EC2 instance lifecycle</li>
<li>Có thể attach/detach từ instance này sang instance khác</li>
<li>Persistent storage - data survive instance termination</li>
<li>Automatic replication trong AZ</li>
</ul>
<h5>Instance Store</h5>
<ul>
<li>Attached trực tiếp to host machine</li>
<li>Temporary storage - data lost khi instance stops</li>
<li>Free with instance</li>
<li>Higher I/O performance</li>
</ul>
<h4>EBS Volume Types</h4>
<table>
<tr><th>Type</th><th>Use Case</th><th>IOPS</th></tr>
<tr><td>gp3</td><td>General purpose, low cost</td><td>3,000 - 16,000</td></tr>
<tr><td>gp2</td><td>General purpose (thế hệ trước)</td><td>3,000</td></tr>
<tr><td>io2</td><td>High performance, mission-critical</td><td>64,000</td></tr>
<tr><td>st1</td><td>Throughput optimized HDD</td><td>500</td></tr>
<tr><td>sc1</td><td>Cold storage HDD</td><td>250</td></tr>
</table>
<h4>Key Features</h4>
<ul>
<li><strong>Encryption:</strong> AES-256 encryption at rest</li>
<li><strong>Snapshots:</strong> Incremental backups to S3</li>
<li><strong>Multi-attach:</strong> Attach to multiple instances (io2)</li>
<li><strong>Size:</strong> 1 GB to 16 TB</li>
</ul>
<h4>Use Cases</h4>
<ul>
<li><strong>gp3:</strong> Boot volumes, dev/test, web servers</li>
<li><strong>io2:</strong> Databases, critical applications</li>
<li><strong>st1:</strong> Big data, log processing</li>
<li><strong>sc1:</strong> Archival data, infrequent access</li>
</ul>"""
    },
    "AWS Lambda in Hindi | What is Serverless & How to Create Your First Function": {
        "summary": "Giới thiệu AWS Lambda - dịch vụ serverless compute. Cách tạo function đầu tiên và hiểu về serverless architecture.",
        "explanation": """<p>AWS Lambda là dịch vụ serverless compute cho phép bạn chạy code mà không cần provisioning hoặc quản lý servers.</p>
<h4>Serverless là gì?</h4>
<ul>
<li><strong>No server management:</strong> Không cần provision, scale, manage servers</li>
<li><strong>Pay per use:</strong> Chỉ trả cho compute time thực sự sử dụng</li>
<li><strong>Automatic scaling:</strong> Tự động scale theo request</li>
<li><strong>High availability:</strong> Built-in redundancy</li>
</ul>
<h4>Lambda Function Structure</h4>
<pre style="background: var(--bg-surface); padding: 10px; border-radius: 4px;">
exports.handler = async (event, context) => {
  // Your code here
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Hello!" })
  };
};
</pre>
<h4>Lambda Event Sources</h4>
<ul>
<li><strong>Synchronous:</strong> API Gateway, S3, DynamoDB, CloudWatch Events</li>
<li><strong>Asynchronous:</strong> S3, SNS, CloudWatch Events</li>
<li><strong>Stream-based:</strong> Kinesis, DynamoDB Streams</li>
</ul>
<h4>Lambda Configuration</h4>
<ul>
<li><strong>Memory:</strong> 128 MB to 10,240 MB</li>
<li><strong>Timeout:</strong> Up to 15 minutes</li>
<li><strong>Runtimes:</strong> Node.js, Python, Java, Go, Ruby, .NET</li>
</ul>
<h4>Pricing</h4>
<ul>
<li><strong>Requests:</strong> $0.20 per 1 million requests</li>
<li><strong>Duration:</strong> $0.0000166667 per GB-second</li>
<li><strong>Always Free:</strong> 1M requests, 400,000 GB-seconds per month</li>
</ul>
<h4>Best Practices</h4>
<ul>
<li>Use environment variables cho configuration</li>
<li>Implement proper error handling</li>
<li>Use CloudWatch for monitoring</li>
<li>Minimize deployment package size</li>
</ul>"""
    }
}

# Read the current data.js
with open('data.js', 'r') as f:
    content = f.read()

# Count updates
updated = 0
for title, data in detailed_content.items():
    # Find and replace summary and explanation
    old_summary = f'summary: "Bài học về {title}'
    new_summary = f'summary: "{data["summary"]}'
    
    if old_summary in content:
        # Find the lesson block
        idx = content.find(f'title: "{title}"')
        if idx != -1:
            # Find the next occurrence of summary and explanation
            start_idx = content.find('summary:', idx)
            if start_idx != -1:
                # Find the end of explanation (next closing backtick)
                exp_start = content.find('`', start_idx)
                exp_end = content.find('`', exp_start + 1) + 1
                
                # Replace summary
                summary_start = content.find('"', start_idx) + 1
                summary_end = content.find('"', summary_start)
                old_summary_text = content[summary_start:summary_end]
                new_summary_text = data["summary"]
                
                content = content.replace(
                    f'summary: "{old_summary_text}"',
                    f'summary: "{new_summary_text}"'
                )
                
                # Replace explanation
                content = content.replace(
                    f'explanation: `{content[exp_start+1:exp_end-1]}`',
                    f'explanation: `{data["explanation"]}`'
                )
                
                updated += 1

# Write back
with open('data.js', 'w') as f:
    f.write(content)

print(f"Updated {updated} lessons with detailed content")
