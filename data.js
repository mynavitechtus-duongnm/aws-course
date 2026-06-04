// Course Data - AWS Tutorials by Gaurav Sharma
// Complete course with all lessons from the YouTube playlist

const modules = [
    {
        id: 1,
        title: "Giới thiệu AWS",
        description: "Tổng quan về AWS, điện toán đám mây, và cơ sở hạ tầng toàn cầu",
        icon: "cloud",
        lessons: [
            {
                id: "1-1",
                title: "Introducing the AWS Playlist",
                videoId: "rKNSc8RrwxA",
                duration: "12:00",
                summary: "Video giới thiệu tổng quan khóa học AWS Tutorials bằng tiếng Hindi. Gaurav Sharma giới thiệu về playlist học AWS từ cơ bản đến nâng cao, bao gồm hơn 180 bài học covering tất cả các dịch vụ AWS chính.",
                explanation: `<p>Khóa học AWS Tutorials của Gaurav Sharma là một trong những khóa học AWS miễn phí toàn diện nhất bằng tiếng Hindi, với hơn 180 bài học và 35+ giờ video content.</p><h4>Nội dung khóa học bao gồm:</h4><ul><li><strong>Phần 1: Giới thiệu AWS</strong> - Cloud Computing, AWS Infrastructure, Regions, Availability Zones</li><li><strong>Phần 2: Amazon EC2</strong> - Virtual Servers, Instance Types, Security Groups, SSH Access</li><li><strong>Phần 3: EBS & Storage</strong> - Elastic Block Store, Snapshots, Volume Types</li><li><strong>Phần 4: Load Balancer & Auto Scaling</strong> - ELB, ALB, NLB, ASG</li><li><strong>Phần 5: IAM</strong> - Identity & Access Management, Users, Groups, Roles, Policies</li><li><strong>Phần 6: Amazon S3</strong> - Object Storage, Bucket Policies, Versioning, Lifecycle</li><li><strong>Phần 7: CloudFront CDN</strong> - Content Delivery Network, Edge Locations</li><li><strong>Phần 8: Amazon VPC</strong> - Virtual Private Cloud, Subnets, NAT Gateway</li><li><strong>Phần 9: Route 53</strong> - DNS Service, Routing Policies, Health Checks</li><li><strong>Phần 10: RDS & DynamoDB</strong> - Managed Databases, Aurora, NoSQL</li><li><strong>Phần 11: Lambda</strong> - Serverless Computing, Function Development</li><li><strong>Phần 12: API Gateway</strong> - REST APIs, HTTP APIs, Integrations</li><li><strong>Phần 13: Cognito</strong> - Authentication, User Pools, Identity Pools</li><li><strong>Phần 14: ECS</strong> - Container Orchestration, Docker, Fargate</li></ul><h4>Ưu điểm của khóa học:</h4><ul><li>Hoàn toàn miễn phí trên YouTube</li><li>Giảng dạy bằng tiếng Hindi, dễ hiểu cho người Việt</li><li>Thực hành step-by-step với AWS Console</li><li>Cập nhật liên tục với các dịch vụ AWS mới</li><li>Phù hợp cho người mới bắt đầu và người ôn tập AWS Certification</li></ul>`
            },
            {
                id: "1-2",
                title: "What is AWS - Traditional VS Cloud Computing - Why Cloud Computing",
                videoId: "JuE9gKNs5sA",
                duration: "12:00",
                summary: "So sánh giữa Traditional Computing (On-premise) và Cloud Computing. Giải thích tại sao Cloud Computing là xu hướng tất yếu và lợi ích của việc sử dụng AWS thay vì tự xây dựng hạ tầng.",
                explanation: `<p>Trong bài học này, Gaurav Sharma giải thích sự khác biệt cơ bản giữa Traditional Computing (điện toán truyền thống) và Cloud Computing (điện toán đám mây).</p><h4>Traditional Computing (On-Premise)</h4><ul><li><strong>Capital Expenditure (CapEx):</strong> Cần đầu tư ban đầu lớn cho server, network equipment, storage</li><li><strong>Thời gian triển khai:</strong> Có thể mất vài tuần đến vài tháng để setup</li><li><strong>Quản lý và bảo trì:</strong> Cần đội ngũ kỹ thuật riêng cho hardware, OS, patches</li><li><strong>Mở rộng (Scaling):</strong> Khó khăn và tốn kém khi cần scale up/down</li><li><strong>Rủi ro:</strong> Over-provisioning gây lãng phí, Under-provisioning gây downtime</li></ul><h4>Cloud Computing</h4><ul><li><strong>Operational Expenditure (OpEx):</strong> Chỉ trả tiền cho những gì sử dụng (Pay-as-you-go)</li><li><strong>Thời gian triển khai:</strong> Có thể launch trong vài phút</li><li><strong>Quản lý:</strong> AWS quản lý infrastructure, bạn tập trung vào ứng dụng</li><li><strong>Mở rộng:</strong> Tự động scale theo demand trong vài giây</li><li><strong>Độ tin cậy:</strong> 99.99% uptime với multiple Availability Zones</li></ul><h4>Tại sao nên chọn AWS?</h4><ul><li><strong>Market Leader:</strong> AWS chiếm 32% thị phần cloud computing toàn cầu</li><li><strong>200+ Services:</strong> Cung cấp hơn 200 dịch vụ từ compute, storage, database, AI, IoT</li><li><strong>Global Infrastructure:</strong> 33 Regions, 105 Availability Zones</li><li><strong>Security:</strong> Đạt nhiều compliance certifications (SOC, HIPAA, PCI, ISO)</li></ul>`
            },
            {
                id: "1-3",
                title: "Cloud Computing Service Models | IAAS | PAAS | SAAS",
                videoId: "zr48J9Xhaw4",
                duration: "12:00",
                summary: "Giải thích chi tiết 3 mô hình dịch vụ đám mây: IaaS, PaaS, và SaaS. So sánh vị trí kiểm soát của khách hàng trong mỗi mô hình.",
                explanation: `<p>Bài học này đi sâu vào 3 mô hình dịch vụ cloud computing và vị trí kiểm soát (control) của khách hàng trong mỗi mô hình.</p><h4>1. IaaS (Infrastructure as a Service)</h4><ul><li><strong>Khái niệm:</strong> Cung cấp tài nguyên hạ tầng ảo hóa: servers, storage, networking</li><li><strong>Ví dụ AWS:</strong> Amazon EC2, Amazon S3, Amazon VPC, EBS</li><li><strong>Bạn quản lý:</strong> OS, applications, data, runtime</li><li><strong>AWS quản lý:</strong> Physical servers, data center, virtualization layer</li><li><strong>Use cases:</strong> Migration từ on-premise, lift-and-shift applications</li></ul><h4>2. PaaS (Platform as a Service)</h4><ul><li><strong>Khái niệm:</strong> Cung cấp nền tảng để phát triển và deploy ứng dụng</li><li><strong>Ví dụ AWS:</strong> AWS Elastic Beanstalk, AWS Lambda, Amazon RDS</li><li><strong>Bạn quản lý:</strong> Applications, data</li><li><strong>AWS quản lý:</strong> OS, runtime, middleware, development tools</li></ul><h4>3. SaaS (Software as a Service)</h4><ul><li><strong>Khái niệm:</strong> Ứng dụng hoàn chỉnh chạy trên cloud, access qua internet</li><li><strong>Ví dụ AWS:</strong> Amazon Chime, AWS Connect, Amazon WorkSpaces</li><li><strong>NCC quản lý:</strong> Tất cả - từ infrastructure đến ứng dụng</li></ul>`
            },
            {
                id: "1-4",
                title: "Deployment Model of Clouds - Public Private and Hybrid Cloud",
                videoId: "OmfUnOYKxIg",
                duration: "15:00",
                summary: "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud.",
                explanation: `<p>Bài học này phân tích 3 deployment models của cloud computing và các use cases phù hợp cho từng loại.</p><h4>1. Public Cloud</h4><ul><li><strong>Khái niệm:</strong> Tài nguyên được chia sẻ giữa nhiều organizations, hosted bởi cloud provider</li><li><strong>Ưu điểm:</strong> Chi phí thấp, scale linh hoạt, high availability built-in</li><li><strong>Nhược điểm:</strong> Less control, security concerns cho sensitive data</li><li><strong>Use cases:</strong> Web applications, dev/test environments, startups</li></ul><h4>2. Private Cloud</h4><ul><li><strong>Khái niệm:</strong> Cloud infrastructure dành riêng cho một organization</li><li><strong>Ưu điểm:</strong> Full control, enhanced security</li><li><strong>Nhược điểm:</strong> Higher upfront costs</li><li><strong>Use cases:</strong> Financial services, healthcare, government</li></ul><h4>3. Hybrid Cloud</h4><ul><li><strong>Khái niệm:</strong> Kết hợp public cloud và private cloud</li><li><strong>Ưu điểm:</strong> Flexibility, cost optimization, security</li><li><strong>Use cases:</strong> Web apps on public cloud + databases on private</li></ul>`
            },
            {
                id: "1-5",
                title: "How Aws Charge - AWS pricing",
                videoId: "NgI_Jkm7RRE",
                duration: "12:00",
                summary: "Giải thích cách AWS tính phí và các mô hình pricing: Pay-as-you-go, Reserved Instances, Savings Plans.",
                explanation: `<p>AWS sử dụng mô hình pricing linh hoạt pay for what you use.</p><h4>AWS Pricing Philosophy</h4><ul><li><strong>Pay for what you use:</strong> Không phí trả trước</li><li><strong>Pay less when you reserve:</strong> Giảm 30-70% với Reserved Instances</li><li><strong>Pay even less with more:</strong> Volume discounts</li></ul><h4>Main Pricing Models</h4><h5>1. On-Demand</h5><ul><li>Không có commitment, trả theo giờ</li><li>Phù hợp cho: Short-term projects, spike workloads</li></ul><h5>2. Reserved Instances</h5><ul><li>Commitment 1-3 years, giảm 30-72%</li></ul><h5>3. Savings Plans</h5><ul><li>Thay thế linh hoạt hơn cho RIs, giảm đến 72%</li></ul><h5>4. Spot Instances</h5><ul><li>Sử dụng unused capacity, giảm đến 90%</li><li>Phù hợp cho: Batch processing, ML training</li></ul><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda (1M requests), DynamoDB (25GB)</li><li><strong>12 Months Free:</strong> EC2 (750h), S3 (5GB)</li></ul>`
            },
            {
                id: "1-6",
                title: "What/Why is AWS region | AWS Region Map | AWSGlobal Infrastructure",
                videoId: "jRGW4uInhkE",
                duration: "12:00",
                summary: "Giới thiệu AWS Regions - các vùng địa lý trên toàn thế giới nơi AWS có data centers.",
                explanation: `<p>AWS Regions là tập hợp các Availability Zones được đặt tại các vị trí địa lý khác nhau trên thế giới.</p><h4>AWS Global Infrastructure</h4><ul><li><strong>Regions:</strong> 33 geographic locations</li><li><strong>Availability Zones:</strong> 105 data centers riêng biệt</li><li><strong>Edge Locations:</strong> 450+ locations cho CDN và DNS</li><li><strong>Local Zones:</strong> Mở rộng AWS closer to users</li></ul><h4>Cách chọn Region</h4><ul><li><strong>Latency:</strong> Chọn region gần users nhất</li><li><strong>Compliance:</strong> Data phải stay in borders</li><li><strong>Cost:</strong> Giá services khác nhau</li></ul><h4>Popular Regions</h4><ul><li><strong>us-east-1:</strong> US East - Most popular, lowest price</li><li><strong>eu-west-1:</strong> Europe Ireland</li><li><strong>ap-southeast-1:</strong> Asia Pacific Singapore</li></ul>`
            },
            {
                id: "1-7",
                title: "What/Why is AWS Availability Zones | AWS Global Infrastructure",
                videoId: "fH5828qH4_k",
                duration: "12:00",
                summary: "Giải thích Availability Zones (AZs) - các data centers riêng biệt trong một Region.",
                explanation: `<p>Availability Zones (AZs) là các data centers riêng biệt về mặt vật lý nhưng được kết nối với nhau bằng low-latency networking trong một Region.</p><h4>Cấu trúc của Availability Zone</h4><ul><li><strong>Physical Separation:</strong> AZs cách nhau ít nhất 100km</li><li><strong>Independent Power:</strong> Separate power grids, backup generators</li><li><strong>Independent Networking:</strong> Separate ISPs</li><li><strong>Low Latency:</strong> < 1ms giữa các AZs</li></ul><h4>Tại sao AZs quan trọng?</h4><ul><li>Single AZ failure không ảnh hưởng đến các AZs khác</li><li>99.99% SLA với multi-AZ deployments</li><li>Fault isolation khỏi disasters</li></ul><h4>Best Practices</h4><ul><li>Luôn sử dụng at least 2 AZs cho production</li><li>Enable Multi-AZ cho RDS, ElastiCache</li></ul>`
            },
            {
                id: "1-8",
                title: "What/Why is Local Zones | Local Zones | AWS Global Infrastructure",
                videoId: "WF5XS6jOUZ0",
                duration: "12:00",
                summary: "Giới thiệu AWS Local Zones - mở rộng AWS infrastructure closer to users ở các thành phố lớn.",
                explanation: `<p>AWS Local Zones là các vị trí compute edge được đặt closer to large population centers.</p><h4>So sánh</h4><ul><li><strong>Regions:</strong> Full services, latency 20-100ms</li><li><strong>AZs:</strong> Part of Region, latency < 1ms</li><li><strong>Local Zones:</strong> Extensions, latency < 10ms</li></ul><h4>Use Cases</h4><ul><li><strong>Ultra-low Latency:</strong> Real-time gaming, AR/VR, video conferencing</li><li><strong>Content Delivery:</strong> Streaming media, live sports</li><li><strong>Data Residency:</strong> Regulatory requirements</li></ul><h4>Available Local Zones</h4><ul><li>US: Los Angeles, Boston, Chicago, Dallas, Houston...</li></ul>`
            },
            {
                id: "1-9",
                title: "Create AWS Account | Create AWS Free Tier Account",
                videoId: "QDymcZ5xYow",
                duration: "15:00",
                summary: "Hướng dẫn tạo AWS Account mới và kích hoạt Free Tier.",
                explanation: `<p>Bài học này hướng dẫn step-by-step cách tạo AWS Account mới.</p><h4>Yêu cầu</h4><ul><li>Email address hợp lệ</li><li>Credit/Debit card</li><li>Phone number để xác minh</li></ul><h4>Các bước tạo Account</h4><ol><li>Truy cập aws.amazon.com</li><li>Nhập email và account name</li><li>Xác minh email</li><li>Nhập credit card (AWS sẽ charge $1 để verify)</li><li>Xác minh phone</li><li>Chọn Support Plan (Basic)</li></ol><h4>AWS Free Tier</h4><ul><li><strong>Always Free:</strong> Lambda, DynamoDB, SNS, SQS</li><li><strong>12 Months Free:</strong> EC2 (750h), S3 (5GB)</li></ul><h4>Cách tránh charges</h4><ul><li>Set up Billing Alerts</li><li>Delete unused resources</li></ul>`
            },
        ]
    },
    {
        id: 2,
        title: "Amazon EC2",
        description: "Virtual Servers trên AWS - cách tạo, cấu hình và quản lý EC2 instances",
        icon: "server",
        lessons: [
            {
                id: "2-1",
                title: "Create First EC2 Instance | EC2 Instance Creation in AWS",
                videoId: "f-T4xWUZWSk",
                duration: "15:00",
                summary: "Hướng dẫn tạo EC2 instance đầu tiên trên AWS Console.",
                explanation: `<p>Amazon EC2 cung cấp scalable computing capacity trong AWS cloud.</p><h4>EC2 Creation Steps</h4><h5>1. Chọn AMI</h5><ul><li><strong>Amazon Linux 2:</strong> Free tier, RHEL-based</li><li><strong>Ubuntu:</strong> Popular</li></ul><h5>2. Chọn Instance Type</h5><ul><li><strong>t2.micro:</strong> Free tier, 1GB RAM</li></ul><h5>3. Configure</h5><ul><li>Network: VPC và subnet</li><li>Auto-assign Public IP: Enable</li></ul><h5>4. Security Group</h5><ul><li>SSH (22): Linux access</li><li>HTTP (80): Web traffic</li></ul><h5>5. Launch</h5><ul><li>Chọn key pair</li><li>Click Launch</li></ul><h4>Kết nối</h4><pre>ssh -i key.pem ec2-user@public-ip</pre>`
            },
            {
                id: "2-2",
                title: "Access EC2 Instance From Windows Machine | EC2 Instance Connect",
                videoId: "HPrq6kdsEZ0",
                duration: "12:00",
                summary: "Hướng dẫn kết nối đến EC2 instance từ Windows.",
                explanation: `<p>Có nhiều cách để kết nối đến EC2 Linux instance từ Windows.</p><h4>1. EC2 Instance Connect (Khuyến nghị)</h4><ul><li>Không cần key pair</li><li>SSH keys managed bởi AWS</li><li>AWS Console > EC2 > Connect</li></ul><h4>2. PuTTY</h4><ul><li>Download PuTTYgen</li><li>Convert .pem to .ppk</li><li>Connect: ec2-user@public-ip</li></ul><h4>3. WSL</h4><ul><li>Enable WSL: wsl --install</li><li>ssh -i key.pem ec2-user@public-ip</li></ul><h4>Security</h4><ul><li>Restrict SSH to your IP</li><li>Use Session Manager</li></ul>`
            },
            {
                id: "2-3",
                title: "Access EC2 Instance From Linux Machine | EC2 Instance Connect",
                videoId: "8Vuvl4cvdv4",
                duration: "12:00",
                summary: "Huong dan ket noi SSH den EC2 instance tu Linux/Mac.",
                explanation: `<p>SSH la Secure Shell protocol de ket noi secure den EC2 instances. Voi Linux/Mac: <pre>ssh -i key.pem ec2-user@public-ip</pre> Cac loi thuong gap: Permission denied (can chmod 400 key.pem), Connection timeout (check Security Group), Host key changed (ssh-keygen -R ip-address). Sau khi connect, ban co the update system (yum update) va cai dat packages. EC2 Instance Connect la phuong phap thay the - khong can key pair, SSH duoc managed boi AWS.</p><h4>SSH Connection</h4><pre>ssh -i key.pem ec2-user@public-ip</pre><h4>Key Permissions</h4><pre>chmod 400 key.pem</pre><h4>Common Issues</h4><ul><li>Permission denied: chmod 400 key.pem</li><li>Connection timeout: Check security group</li></ul>`
            },
            {
                id: "2-4",
                title: "Install Nginx in EC2 Instance | Deploy Sample Application In EC2",
                videoId: "HaRki0xPPd4",
                duration: "15:00",
                summary: "Hướng dẫn cài đặt Nginx web server trên EC2 instance.",
                explanation: `<p>Bài học này hướng dẫn cách cài đặt Nginx trên EC2 instance.</p><h4>Cài đặt Nginx (Amazon Linux 2)</h4><pre>sudo yum update -y
sudo amazon-linux-extras install nginx1 -y
sudo systemctl start nginx
sudo systemctl enable nginx</pre><h4>Kiểm tra</h4><ul><li>curl http://localhost</li><li>Access via public IP: http://your-public-ip</li></ul><h4>Cấu hình</h4><ul><li><strong>Config:</strong> /etc/nginx/nginx.conf</li><li><strong>Document root:</strong> /usr/share/nginx/html</li></ul><h4>Deploy Sample App</h4><pre>sudo tee /usr/share/nginx/html/index.html << 'EOF'
<!DOCTYPE html>
<html><body><h1>Welcome to AWS!</h1></body></html>
EOF</pre>`
            },
            {
                id: "2-5",
                title: "Bootstrap Script in EC2 Instance | User Data In EC2",
                videoId: "EXs775-J5zE",
                duration: "12:00",
                summary: "Su dung User Data script de tu dong chay commands khi EC2 khoi tao.",
                explanation: `<p>User Data cho phep chay scripts tu dong khi EC2 instance start lan dau. Use cases: Install software (nginx, apache), configure applications, download code tu S3, setup monitoring agents. Example User Data: <pre>#!/bin/bash\nyum update -y\namazon-linux-extras install nginx1 -y\nsystemctl start nginx</pre> Xem logs: <pre>sudo cat /var/log/cloud-init-output.log</pre> User Data duoc chay voi root privileges.</p><h4>Use Cases</h4><ul><li>Install software (nginx, apache)</li><li>Configure applications</li><li>Download code from S3</li></ul><h4>Example User Data</h4><pre>#!/bin/bash
yum update -y
amazon-linux-extras install nginx1 -y
systemctl start nginx</pre>`
            },
            {
                id: "2-6",
                title: "AWS Security Group | Security Group AWS",
                videoId: "poAvpknMDwI",
                duration: "12:00",
                summary: "Giải thích Security Groups - virtual firewall cho EC2 instances.",
                explanation: `<p>AWS Security Group là stateful virtual firewall kiểm soát traffic vào và ra cho EC2.</p><h4>Security Group Fundamentals</h4><ul><li><strong>Stateful:</strong> Inbound allowed = Outbound allowed</li><li><strong>Inbound:</strong> Tất cả denied by default</li><li><strong>Outbound:</strong> Tất cả allowed by default</li></ul><h4>Rule Components</h4><ul><li><strong>Type:</strong> SSH, HTTP, HTTPS</li><li><strong>Protocol:</strong> TCP, UDP, ICMP</li><li><strong>Port Range:</strong> Specific port</li><li><strong>Source:</strong> IP, Security Group</li></ul><h4>Best Practices</h4><ul><li>Chỉ allow ports cần thiết</li><li>Use specific IP ranges</li><li>Separate SG by Function</li></ul>`
            },
            {
                id: "2-7",
                title: "AWS EC2 Instance Type | Instance Type in AWS",
                videoId: "nA96hTiakb8",
                duration: "12:00",
                summary: "Tổng quan về các loại EC2 Instance Types.",
                explanation: `<p>AWS cung cấp hơn 500 instance types được tối ưu cho các use cases khác nhau.</p><h4>EC2 Instance Families</h4><h5>1. General Purpose (T, M)</h5><ul><li><strong>T-Series:</strong> Burstable performance</li><li><strong>M-Series:</strong> Steady-state</li></ul><h5>2. Compute Optimized (C)</h5><ul><li>Use case: Batch processing, ML inference</li></ul><h5>3. Memory Optimized (R, X)</h5><ul><li>Use case: In-memory databases</li></ul><h5>4. Storage Optimized (I, D)</h5><ul><li>Use case: High I/O, data warehousing</li></ul><h5>5. GPU (P, G)</h5><ul><li>Use case: Machine learning</li></ul><h4>Popular Types</h4><ul><li><strong>t3.micro:</strong> Dev/Test</li><li><strong>m5.large:</strong> App Server</li><li><strong>r5.large:</strong> In-Memory DB</li></ul>`
            },
            {
                id: "2-8",
                title: "AWS Pricing | Reserve Instance | Spot Instance | Saving Plan | Dedicated Host",
                videoId: "wFf8Er1tz_0",
                duration: "12:00",
                summary: "Chi tiet ve cac mo hinh pricing: On-Demand, Reserved, Spot, Savings Plans.",
                explanation: `<p>AWS pricing philosophy: Pay for what you use, Pay less when you reserve, Pay even less with more. On-Demand: Khong co commitment, tra theo gio, phu hop cho short-term projects. Reserved Instances: Commitment 1-3 nam, giam 30-72%, co the chon No/Partial/All Upfront. Savings Plans: Thay the linh hoat hon cho RIs, giam den 72%, co Compute va EC2 Instance Savings Plans. Spot Instances: Su dung unused capacity, giam den 90%, co the interrupted bat cu luc nao, phu hop cho batch jobs, ML training. AWS Free Tier: Always Free (Lambda 1M requests, DynamoDB 25GB), 12 Months Free (EC2 750h, S3 5GB).</p><h4>1. On-Demand</h4><ul><li>Tra theo gio</li><li>Khong co commitment</li></ul><h4>2. Reserved Instances</h4><ul><li>Commitment 1-3 nam</li><li>Giam 30-72%</li></ul><h4>3. Savings Plans</h4><ul><li>Thay the linh hoat cho RIs</li><li>Giam den 72%</li></ul><h4>4. Spot Instances</h4><ul><li>Unused capacity</li><li>Giam den 90%</li><li>Co the interrupted</li></ul>`
            },
            {
                id: "2-9",
                title: "Create Windows Instance In AWS | AWS tutorials | AWS Step By Step",
                videoId: "CEyj_YGNvNM",
                duration: "15:00",
                summary: "Huong dan tao Windows EC2 instance tren AWS.",
                explanation: `<p>Tao Windows Server EC2 instance de chay cac ung dung Windows. Chon AMI: Windows Server 2022 Base, Windows Server 2019 Base. Tao Instance: Chon Windows AMI, chon instance type (t3.micro free tier), configure network, add Storage (50GB thuong du), configure Security Group: RDP (port 3389), launch voi key pair. Ket noi Windows: Tai RDP file tu AWS Console, get password su dung key pair, connect qua Remote Desktop. Su dung PuTTY hoac Remmina tu Linux de ket noi Windows instances.</p><h4>Chon AMI</h4><ul><li>Windows Server 2022 Base</li><li>Windows Server 2019 Base</li></ul><h4>Tao Instance</h4><ol><li>Chon Windows AMI</li><li>Chon instance type</li><li>Configure Security Group: RDP (port 3389)</li><li>Launch voi key pair</li></ol><h4>Ket noi Windows</h4><ol><li>Download RDP file</li><li>Get password</li><li>Connect qua Remote Desktop</li></ol>`
            },
            {
                id: "2-10",
                title: "Access Windows Instance From Linux Machine | AWS tutorials | AWS Step By Step",
                videoId: "TEUAsbB9bwU",
                duration: "18:00",
                summary: "Huong dan ket noi Windows EC2 instance tu Linux.",
                explanation: `<p>Co nhieu cach ket noi Windows tu Linux. Su dung Remmina: <pre>sudo apt install remmina remmina-plugin-rdp\nremmina</pre> Su dung xrdp: <pre>sudo apt install xrdp\nsudo systemctl enable xrdp</pre> Thong tin can thiet: Windows IP address, Username: Administrator, Password: Da lay tu AWS Console. Security Group: Mo port 3389 (RDP) tu IP cua ban. Thuc hien ket noi va nhap thong tin dang nhap de truy cap Windows desktop.</p><h4>Su dung Remmina</h4><pre>sudo apt install remmina remmina-plugin-rdp</pre><h4>Thong tin can thiet</h4><ul><li>Windows IP address</li><li>Username: Administrator</li><li>Password: Da lay tu AWS Console</li></ul>`
            },
            {
                id: "2-11",
                title: "Instance Metadata With UserData | AWS tutorials | AWS Step By Step",
                videoId: "KP6XRtyVVX4",
                duration: "18:00",
                summary: "Tim hieu EC2 Instance Metadata - cach lay thong tin instance.",
                explanation: `<p>Instance Metadata cung cap thong tin ve instance ma khong can su dung AWS CLI. Metadata URL: <pre>curl http://169.254.169.254/latest/meta-data/</pre> Thong tin co san: ami-id (AMI ID), instance-id (Instance ID), instance-type (Instance type), local-ipv4 (Private IP), public-ipv4 (Public IP), security-groups (Security groups). User Data: <pre>curl http://169.254.169.254/latest/user-data/</pre> Luu y bao mat: Metadata accessible tu trong instance, su dung IAM roles thay vi access keys, enable IMDSv2 de prevent hijacking.</p><h4>Metadata URL</h4><pre>curl http://169.254.169.254/latest/meta-data/</pre><h4>Thong tin co san</h4><ul><li>ami-id: AMI ID</li><li>instance-id: Instance ID</li><li>instance-type: Instance type</li><li>public-ipv4: Public IP</li></ul><h4>User Data</h4><pre>curl http://169.254.169.254/latest/user-data/</pre>`
            },
            {
                id: "2-12",
                title: "Attach Elastic/Static IP to an EC2 Instance | AWS tutorials | AWS Step By Step",
                videoId: "5oZEJMZpZDs",
                duration: "18:00",
                summary: "Cach gan Elastic IP address cho EC2 instance.",
                explanation: `<p>Elastic IP la static public IPv4 address co the gan cho instances. Tao: EC2 Dashboard > Elastic IPs > Allocate new address. Gán: Actions > Associate Elastic IP address. CLI: <pre>aws ec2 associate-address --instance-id i-xxx --public-ip x.x.x.x</pre> Use cases: Static IP cho website, whitelist IP in firewall, point DNS records. Chi phi: Free neu associated voi running instance, $0.005/gio neu not associated hoac instance stopped. Best practice: Khong nen rely hoan toan vao EIP, consider Route 53 cho DNS-based failover.</p><h4>Tao Elastic IP</h4><ol><li>EC2 Dashboard > Elastic IPs</li><li>Allocate new address</li><li>Associate voi instance</li></ol><h4>CLI</h4><pre>aws ec2 allocate-address
aws ec2 associate-address --instance-id i-xxx --public-ip x.x.x.x</pre><h4>Chi phi</h4><ul><li>Free neu associated</li><li>$0.005/gio neu khong su dung</li></ul>`
            },
            {
                id: "2-13",
                title: "Detach Elastic/Static IP | Release EIP | AWS tutorials | AWS Step By Step",
                videoId: "Wgyp3yWRWTU",
                duration: "18:00",
                summary: "Cach giai phong Elastic IP address.",
                explanation: `<p>Detach va release Elastic IP khi khong can nua de tranh charges. Disassociate: <pre>aws ec2 disassociate-address --public-ip x.x.x.x</pre> Release: <pre>aws ec2 release-address --allocation-id eipalloc-xxx</pre> Chi phi: $0.005/gio cho EIP khong associated. Best Practices: Release EIP khi khong can, use Route 53 thay vi EIP cho most use cases, automate cleanup voi Lambda hoac budget alerts. Qua trinh: Disassociate truoc, sau do release.</p><h4>Disassociate</h4><pre>aws ec2 disassociate-address --public-ip x.x.x.x</pre><h4>Release</h4><pre>aws ec2 release-address --allocation-id eipalloc-xxx</pre><h4>Chi phi</h4><ul><li>$0.005/gio cho EIP khong associated</li><li>Release khi khong can</li></ul>`
            },
        ]
    },
    {
        id: 3,
        title: "EBS & Storage",
        description: "Elastic Block Storage - lưu trữ block-level cho EC2, snapshots, và các loại volumes",
        icon: "database",
        lessons: [
            {
                id: "3-1",
                title: "Elastic Block Storage (EBS) | Instance Store | AWS Step By Step",
                videoId: "9OpRBa0CNRw",
                duration: "18:00",
                summary: "Tong quan ve EBS volumes va Instance Store.",
                explanation: `<p>EBS vs Instance Store: EBS la network-attached storage, persist independently of instance lifecycle, co the attach/detach. Instance Store la attached directly to host, data lost when instance stops, free voi instance, higher I/O performance. EBS Volume Types: gp3 (3000-16000 IOPS, $0.08/GB), gp2 (legacy), io2 (64000 IOPS, 99.999% durability), st1 (throughput optimized HDD), sc1 (cold storage HDD). EBS volumes tu dong replicated trong AZ de protect khoi component failure.</p><h4>EBS Volumes</h4><ul><li>Network-attached storage</li><li>Independent of instance lifecycle</li><li>Persist after termination</li></ul><h4>Instance Store</h4><ul><li>Attached to host</li><li>Data lost when stopped</li><li>Higher I/O performance</li></ul><h4>Volume Types</h4><ul><li>gp3: General purpose SSD</li><li>io2: High performance SSD</li><li>st1: Throughput optimized HDD</li></ul>`
            },
            {
                id: "3-2",
                title: "Create First Elastic Block Storage Vol | Mount EBS in Linux | AWS Step By Step",
                videoId: "1eUU1SybgQg",
                duration: "15:00",
                summary: "Huong dan tao EBS volume va mount vao EC2 Linux.",
                explanation: `<p>Tao EBS volume va mount tren Linux instance. Tao Volume: EC2 > Volumes > Create Volume, chon size, type (gp3), AZ. Attach: Actions > Attach Volume, chon instance trong cung AZ. Mount tren Linux: <pre>lsblk</pre> de check available disks, <pre>sudo mkfs -t xfs /dev/xvdf</pre> de format, <pre>sudo mkdir /mnt/data && sudo mount /dev/xvdf /mnt/data</pre> de mount. Add to /etc/fstab for auto-mount: <pre>/dev/xvdf /mnt/data xfs defaults,nofail 0 2</pre> Verify: <pre>df -h</pre></p><h4>Tao Volume</h4><ol><li>EC2 > Volumes > Create Volume</li><li>Chon size, type, AZ</li><li>Attach to instance</li></ol><h4>Mount tren Linux</h4><pre>lsblk
sudo mkfs -t xfs /dev/xvdf
sudo mkdir /mnt/data
sudo mount /dev/xvdf /mnt/data</pre><h4>Auto-mount</h4><pre>/dev/xvdf /mnt/data xfs defaults,nofail 0 2</pre>`
            },
            {
                id: "3-3",
                title: "Detach an EBS volume from one EC2 Instance and Attach it Another One",
                videoId: "d6c6S_vICvs",
                duration: "12:00",
                summary: "Cach detach EBS volume va attach vao instance khac.",
                explanation: `<p>Detach EBS volume tu instance nay va attach sang instance khac. Detach: <pre>aws ec2 detach-volume --volume-id vol-xxx</pre> Hoac qua Console: Volumes > Select > Actions > Detach Volume. Attach: <pre>aws ec2 attach-volume --volume-id vol-xxx --instance-id i-xxx --device /dev/sdf</pre> Luu y: Instance phai cung AZ, umount truoc khi detach, force detach neu can: <pre>aws ec2 detach-volume --volume-id vol-xxx --force</pre>.</p><h4>Detach</h4><pre>aws ec2 detach-volume --volume-id vol-xxx</pre><h4>Attach</h4><pre>aws ec2 attach-volume --volume-id vol-xxx --instance-id i-xxx --device /dev/sdf</pre><h4>Luu y</h4><ul><li>Instance phai cung AZ</li><li>Umount truoc khi detach</li></ul>`
            },
            {
                id: "3-4",
                title: "Resize EBS Volume and Resize the File System",
                videoId: "JwEyueilFb4",
                duration: "12:00",
                summary: "Cach mo rong EBS volume va file system.",
                explanation: `<p>Mo rong EBS volume khi can them storage. Buoc 1: Modify Volume - Volumes > Modify Volume > Change size. Buoc 2: Extend Partition - <pre>sudo growpart /dev/xvda 1</pre> Buoc 3: Extend File System - XFS: <pre>sudo xfs_growfs /mnt/data</pre>, ext4: <pre>sudo resize2fs /dev/xvdf</pre> Verify: <pre>df -h && lsblk</pre> Luu y: Chi co the increase size, khong decrease. Volume phai be attached. File system phai match type.</p><h4>Modify Volume</h4><ol><li>Volumes > Modify Volume</li><li>Change size</li></ol><h4>Extend</h4><pre>sudo growpart /dev/xvda 1
sudo xfs_growfs /mnt/data</pre><h4>Verify</h4><pre>df -h</pre><h4>Luu y</h4><ul><li>Chi co the increase, khong decrease</li></ul>`
            },
            {
                id: "3-5",
                title: "How to Resize ROOT EBS Volume",
                videoId: "a2MTjl3KAdA",
                duration: "15:00",
                summary: "Huong dan resize root EBS volume.",
                explanation: `<p>Resize root EBS volume de co them space cho OS. Cach don gian: Modify root volume size in console, reboot instance, extend file system. Extend Root Partition: <pre>sudo growpart /dev/xvda 1</pre> Extend File System: XFS: <pre>sudo xfs_growfs /</pre>, ext4: <pre>sudo resize2fs /dev/xvda1</pre> Kiem tra: <pre>df -h && lsblk</pre> Hoac tao snapshot, tao volume lon hon tu snapshot, attach.</p><h4>Cach don gian</h4><ol><li>Modify root volume size in console</li><li>Reboot instance</li><li>Extend file system</li></ol><h4>Extend</h4><pre>sudo growpart /dev/xvda 1
sudo resize2fs /dev/xvda1</pre>`
            },
            {
                id: "3-6",
                title: "Attach One EBS Volume to Multiple EC2 Instance",
                videoId: "aFhwZ75aTKI",
                duration: "12:00",
                summary: "Tim hieu EBS Multi-Attach - gan mot volume cho nhieu instances.",
                explanation: `<p>Multi-Attach cho phep attach cung mot EBS volume cho nhieu instances trong cung AZ. Yeu cau: Volume type phai la io2 hoac io2 Block Express, file system phai support concurrent access (XFS, GFS2), instances phai cung AZ. Benefits: Clustered applications, applications can shared storage, improved availability. Cai dat: Enable Multi-Attach khi tao volume, attach den multiple instances. Canh bao: Can proper locking de tranh data corruption.</p><h4>Yeu cau</h4><ul><li>Volume type: io2</li><li>File system support concurrent access</li><li>Instances cung AZ</li></ul><h4>Use Cases</h4><ul><li>Clustered applications</li><li>Shared storage</li></ul>`
            },
            {
                id: "3-7",
                title: "Type of EBS Volumes - Which EBS Volume should I use ?",
                videoId: "ZJ5V2cSfbpc",
                duration: "12:00",
                summary: "So sanh cac loai EBS volumes va cach chon phu hop.",
                explanation: `<p>Chon dung EBS volume type cho workload cua ban. SSD-backed: gp3 (3000-16000 IOPS, best value, $0.08/GB), io2 (64000 IOPS, highest durability 99.999%, $0.125/GB). HDD-backed: st1 (throughput optimized HDD, $0.045/GB), sc1 (cold storage, cheapest, $0.015/GB). Chon dung: Boot volumes -> gp3, Web servers/dev -> gp3, Databases -> io2, Big data/log processing -> st1, Archival -> sc1. Upgrade: Co the upgrade tu gp2/gp3, io1/io2 nhung khong downgrade.</p><h4>SSD-backed</h4><ul><li>gp3: 3000-16000 IOPS, Best value</li><li>io2: 64000 IOPS, highest durability</li></ul><h4>HDD-backed</h4><ul><li>st1: Throughput optimized</li><li>sc1: Cold storage, cheapest</li></ul><h4>Chon dung</h4><ul><li>Boot volumes: gp3</li><li>Databases: io2</li><li>Big data: st1</li></ul>`
            },
            {
                id: "3-8",
                title: "Snapshot Overview - AWS Snapshot - EBS Snapshot",
                videoId: "3Ys2SjowSts",
                duration: "12:00",
                summary: "Tong quan ve EBS Snapshots - incremental backups.",
                explanation: `<p>EBS Snapshots la incremental backups duoc luu trong S3. Dac diem: Incremental - chi backup thay doi, stored in S3 (managed by AWS), can copy across regions, can share voi other accounts. Tinh incremental: First snapshot la full copy, subsequent chi save changes, deleting snapshot chi xoa unique data. Benefits: Disaster recovery, volume migration, AMI creation, compliance backup. Encryption: Snapshots from encrypted volumes tu dong encrypted.</p><h4>Dac diem</h4><ul><li>Incremental: Chi backup thay doi</li><li>Stored in S3</li><li>Can copy across regions</li></ul><h4>Benefits</h4><ul><li>Disaster recovery</li><li>Volume migration</li><li>AMI creation</li></ul>`
            },
            {
                id: "3-9",
                title: "Create First Snapshot - EBS Backup",
                videoId: "Fuzzr2HvBRk",
                duration: "15:00",
                summary: "Huong dan tao EBS snapshot de backup volume.",
                explanation: `<p>Tao snapshot de backup EBS volume.</p><h4>Tao Snapshot</h4><pre>aws ec2 create-snapshot --volume-id vol-xxx --description Backup</pre><h4>Best Practices</h4><ul><li>Create snapshots regularly</li><li>Use lifecycle policies</li><li>Test restore</li></ul>`
            },
            {
                id: "3-10",
                title: "Automate EBS Volume Backup - EBS Lifecycle Manager - EBS Backup",
                videoId: "s3gMJU9Nc7U",
                duration: "12:00",
                summary: "S3 Lifecycle policies tu dong chuyen doi hoac xoa objects theo thoi gian. Tao Policy: S3 > Bucket > Management > Lifecycle rule. Actions: Transition (chuyen sang storage class: Standard IA sau 30 ngay, Glacier sau 90 ngay), Expiration (xoa sau X ngay, xoa incomplete uploads). Use cases: Auto-archive to Glacier, delete old logs, reduce storage costs. Example: Move to IA after 30 days, Glacier after 90 days, Delete after 365 days. Cost savings co the rat lon.",
                explanation: `<p>Su dung EBS Lifecycle Manager.</p><h4>Tao Policy</h4><ol><li>EC2 > Lifecycle Manager</li><li>Create lifecycle policy</li><li>Configure schedule va retention</li></ol><h4>Benefits</h4><ul><li>Automated backups</li><li>Automatic cleanup</li><li>Cost optimization</li></ul>`
            },
            {
                id: "3-11",
                title: "Snapshot and AMI Recycle Bin - Recycle Bin for Snapshot and AMI AWS",
                videoId: "x2T5egBIdQg",
                duration: "12:00",
                summary: "Su dung Recycle Bin de bao ve snapshots va AMIs.",
                explanation: `<p>Recycle Bin bao ve snapshots khoi vo tinh xoa.</p><h4>Tinh nang</h4><ul><li>Soft delete: Khong xoa ngay</li><li>Recovery: Co the khoi phuc</li><li>Automatic cleanup</li></ul><h4>Recovery</h4><ol><li>Select snapshot in Recycle Bin</li><li>Actions > Restore</li></ol>`
            },
            {
                id: "3-12",
                title: "Copy Snapshot From One Region to Another- Copy Snapshot Cross Region/Account",
                videoId: "UJvKOo00xvU",
                duration: "12:00",
                summary: "Copy EBS snapshot sang region khac.",
                explanation: `<p>Copy snapshot de migrate hoac DR.</p><h4>Copy Across Regions</h4><pre>aws ec2 copy-snapshot --source-region us-east-1 --region us-west-2 --source-snapshot-id snap-xxx</pre><h4>Share with Account</h4><pre>aws ec2 modify-snapshot-attribute --snapshot-id snap-xxx --attribute createVolumePermission --operation-type add --user-ids 123456789012</pre>`
            },
            {
                id: "3-13",
                title: "Encrypt the EBS Volume - What will happen when we encrypt the EBS volume",
                videoId: "0MltSofWHTs",
                duration: "12:00",
                summary: "Ma hoa EBS volume su dung AES-256.",
                explanation: `<p>EBS encryption su dung AES-256.</p><h4>Tu dong Encryption</h4><ul><li>Enable by default trong region</li><li>All new volumes encrypted</li></ul><h4>Ma hoa Volume moi</h4><ul><li>Tao volume voi Encrypted: true</li></ul><h4>Ma hoa Existing</h4><ol><li>Create snapshot</li><li>Copy snapshot voi encryption</li><li>Create volume tu encrypted snapshot</li></ol>`
            },
            {
                id: "3-14",
                title: "Delete EBS Snapshot - Cleanup Snapshot",
                videoId: "xGsAgxO9vyg",
                duration: "8:00",
                summary: "Cach xoa EBS snapshots de tiet kiem chi phi.",
                explanation: `<p>Xoa snapshots khong can thiet.</p><h4>Xoa Snapshot</h4><pre>aws ec2 delete-snapshot --snapshot-id snap-xxx</pre><h4>Kiem tra truoc</h4><pre>aws ec2 describe-snapshots --snapshot-ids snap-xxx</pre><h4>Chi phi</h4><ul><li>$0.05/GB-month</li><li>Delete unused snapshots</li></ul>`
            },
            {
                id: "3-15",
                title: "AWS AMI - Amazon Machine Image - Create your Own AMI",
                videoId: "MVllpg49EQM",
                duration: "15:00",
                summary: "Tao custom AMI tu EC2 instance.",
                explanation: `<p>AMI la blueprint de launch instances.</p><h4>Tao AMI</h4><pre>aws ec2 create-image --instance-id i-xxx --name My-AMI --description Web-server</pre><h4>Components</h4><ul><li>Root volume snapshot</li><li>Launch permissions</li><li>Block device mappings</li></ul><h4>Use Cases</h4><ul><li>Pre-configured instances</li><li>Consistent deployments</li></ul>`
            },
            {
                id: "3-16",
                title: "Share Your AMI with other AWS account - Delete Your AWS AMI",
                videoId: "ykiVl1F5bd8",
                duration: "8:00",
                summary: "Share AMI voi AWS account khac va cach xoa AMI.",
                explanation: `<p>Share AMIs de collaborate.</p><h4>Share AMI</h4><pre>aws ec2 modify-image-attribute --image-id ami-xxx --attribute launchPermission --operation-type add --user-ids 123456789012</pre><h4>Xoa AMI</h4><pre>aws ec2 deregister-image --image-id ami-xxx</pre>`
            },
        ]
    },
    {
        id: 4,
        title: "Load Balancer & Auto Scaling",
        description: "ELB, ALB, NLB, Classic LB và Auto Scaling Groups",
        icon: "activity",
        lessons: [
            {
                id: "4-1",
                title: "Elastic Load Balancer in AWS (ELB) - Classic Load Balancer(CLB)",
                videoId: "tBhoVGT7a18",
                duration: "12:00",
                summary: "ELB phan phoi incoming traffic den multiple targets nhu EC2 instances, containers, IP addresses. Load Balancer Types: Application LB (ALB) - Layer 7, HTTP/HTTPS, advanced routing (path-based, host-based). Network LB (NLB) - Layer 4, TCP/UDP, static IP per AZ, ultra-low latency. Gateway LB - Layer 3, virtual appliances. Classic LB (CLB) - legacy (deprecated). ELB features: High availability, health checks, SSL termination, sticky sessions, CloudWatch monitoring, integrated with Auto Scaling.",
                explanation: `<p>ELB phan phoi traffic den multiple targets.</p><h4>Load Balancer Types</h4><ul><li>Application LB: Layer 7, HTTP/HTTPS</li><li>Network LB: Layer 4, TCP/UDP</li><li>Gateway LB: Layer 3</li><li>Classic LB: Legacy</li></ul><h4>Features</h4><ul><li>High availability</li><li>Health checks</li><li>SSL termination</li><li>CloudWatch monitoring</li></ul>`
            },
            {
                id: "4-2",
                title: "EC2 Instance Accessible by LoadBalancer Only | Access Webserver via LoadBalancer",
                videoId: "tqiHn3zNo4U",
                duration: "12:00",
                summary: "Bao mat EC2 instances bang cach chi cho phep traffic qua Load Balancer. Security Group Configuration: Load Balancer SG - Inbound 0.0.0.0/0 (HTTP/HTTPS), Outbound to EC2 SG (port 80/443). EC2 Instance SG - Inbound chi from LB SG (port 80/443), Outbound anywhere. Benefits: Hide instances from direct access, single entry point, easier to manage security, better DDoS protection. Setup: Create ALB, configure instance SG de allow from ALB SG, register instances voi target group, update route53 record den ALB.",
                explanation: `<p>Bao mat EC2 bang cach chi cho phep traffic qua LB.</p><h4>Security Groups</h4><h5>LB SG: Inbound 0.0.0.0, Outbound to EC2 SG</h5><h5>EC2 SG: Inbound from LB SG only</h5><h4>Benefits</h4><ul><li>Hide instances</li><li>Single entry point</li><li>Better DDoS protection</li></ul>`
            },
            {
                id: "4-3",
                title: "Delete Classic Load Balancer",
                videoId: "wOg4sWFZS98",
                duration: "8:00",
                summary: "Xoa CLB khi khong can thiet de tien ich chi phi. Xoa: EC2 > Load Balancers > Select CLB > Actions > Delete. CLI: <pre>aws elb delete-load-balancer --load-balancer-name my-clb</pre> Luu y: CLB deletion khong affect instances, associated IAM roles duoc cleaned up, CloudWatch metrics duoc removed, DNS records can update rieng. Best Practice: Update DNS truoc khi xoa, verify no traffic den CLB, consider migration to ALB.",
                explanation: `<p>Xoa CLB khi khong can thiet.</p><h4>Xoa</h4><pre>aws elb delete-load-balancer --load-balancer-name my-clb</pre><h4>Luu y</h4><ul><li>CLB deletion khong affect instances</li><li>DNS records can update</li></ul>`
            },
            {
                id: "4-4",
                title: "Application Load Balancer | Layer 7 Load Balancer",
                videoId: "IUK7OXXVQFM",
                duration: "12:00",
                summary: "ALB hoat dong o Layer 7 (HTTP/HTTPS), cung cap advanced routing. Features: Path-based routing (/api/* -> API targets), Host-based routing, Query string routing, Header-based routing, HTTP/2 va WebSocket support. Components: Load Balancer (entry point), Listeners (port va protocol), Target Groups (group of targets), Rules (route traffic). ALB is ideal cho microservices architecture, multiple services on same port, blue-green va canary deployments. ALB co the authenticate users voi Cognito hoac IAM.",
                explanation: `<p>ALB hoat dong o Layer 7.</p><h4>Features</h4><ul><li>Path-based routing</li><li>Host-based routing</li><li>HTTP/2, WebSocket support</li></ul><h4>Components</h4><ul><li>Load Balancer</li><li>Listeners</li><li>Target Groups</li><li>Rules</li></ul><h4>Create ALB</h4><pre>aws elbv2 create-load-balancer --name my-alb --type application --subnets subnet-xxx --security-groups sg-xxx</pre>`
            },
            {
                id: "4-5",
                title: "Path Base Routing in Application Load Balancer | Application Load Balancer",
                videoId: "rk-WLPjV09U",
                duration: "12:00",
                summary: "Su dung path-based routing de route traffic.",
                explanation: `<p>ALB co the route traffic dua tren URL path den different target groups. Vi du Routing: /api/* -> API Target Group, /images/* -> Static Content Target Group, /* -> Default Target Group. Tao Rules: ALB > Listeners > View/edit rules > Add rule. Conditions: If path pattern: /api/*, Then: Forward to api-target-group. CLI: <pre>aws elbv2 create-rule --listener-arn arn:aws:... --conditions Field=path-pattern,Values='/api/*' --priority 100 --actions Type=forward,TargetGroupArn=arn:aws:...</pre> Benefits: Multiple apps on same domain, easier microservices, cost optimization.</p><h4>Vi du Routing</h4><pre>/api/* -> API Target Group
/images/* -> Static Content
/* -> Default</pre><h4>Create Rule</h4><pre>aws elbv2 create-rule --listener-arn arn:aws:... --conditions Field=path-pattern,Values=/api/* --priority 100 --actions Type=forward,TargetGroupArn=arn:aws:...</pre>`
            },
            {
                id: "4-6",
                title: "How Get Client IP address on Application Server | Application Load Balancer",
                videoId: "h4nSFaCfR-w",
                duration: "12:00",
                summary: "Cach lay client IP khi su dung ALB.",
                explanation: `<p>Khi su dung ALB, client IP duoc forward trong headers. Client IP Headers: X-Forwarded-For (original client IP), X-Forwarded-Port (client port), X-Forwarded-Proto (HTTP/HTTPS). Example Node.js: <pre>const clientIP = req.headers['x-forwarded-for']</pre> Example Nginx: <pre>set_real_ip_from 10.0.0.0/8;\nreal_ip_header X-Forwarded-For;</pre> Example Apache: <pre>LogFormat '%h %l %u %t \"%r\" %>s %b \"%{X-Forwarded-For}i\"' combined</pre> Note: ALB terminates HTTP va creates new connection to targets, targets see ALB IP as source.</p><h4>Headers</h4><ul><li>X-Forwarded-For: Client IP</li><li>X-Forwarded-Port: Client port</li><li>X-Forwarded-Proto: HTTP/HTTPS</li></ul><h4>Example (Node.js)</h4><pre>const clientIP = req.headers['x-forwarded-for'];</pre><h4>Example (Nginx)</h4><pre>set_real_ip_from 10.0.0.0/8;
real_ip_header X-Forwarded-For;</pre>`
            },
            {
                id: "4-7",
                title: "Stickiness And Custom Page Routing in Application Load Balancer",
                videoId: "qUfqpNb1SLA",
                duration: "12:00",
                summary: "Cau hinh sticky sessions trong ALB.",
                explanation: `<p>Sticky sessions (session affinity) dam bao requests tu same client duoc gui den same target. How it Works: ALB creates LB cookie, cookie identifies target, subsequent requests routed to same target. Enable: Target Group > Attributes > Enable stickiness > Set duration (1 second to 7 days). CLI: <pre>aws elbv2 modify-target-group-attributes --target-group-arn arn:aws:... --attributes Key=stickiness.enabled,Value=true Key=stickiness.lb_cookie.duration_seconds,Value=86400</pre> Use Cases: Session-based applications, applications with user state, caching benefits. Considerations: Co the cause uneven load distribution.</p><h4>Enable</h4><pre>aws elbv2 modify-target-group-attributes --target-group-arn arn:aws:... --attributes Key=stickiness.enabled,Value=true Key=stickiness.lb_cookie.duration_seconds,Value=86400</pre><h4>Use Cases</h4><ul><li>Session-based applications</li><li>User state</li></ul>`
            },
            {
                id: "4-8",
                title: "Network Load Balancer | Layer 4 Load Balancer | AWS Tutorials",
                videoId: "eQi-BD9uyDI",
                duration: "12:00",
                summary: "Gioi thieu Network Load Balancer.",
                explanation: `<p>Network Load Balancer hoat dong o Layer 4 (TCP/UDP/TLS), cung cap ultra-low latency. Features: Layer 4 (TCP/UDP/TLS), Static IP per AZ, Preserve client IP, Handle millions of requests/second, 99.99% SLA. vs ALB: NLB cung cap static IP va ultra-low latency; ALB cung cap HTTP-level routing. Use Cases: High performance applications, gaming servers, IoT protocols, non-HTTP applications. NLB is best khi ban can static IP addresses hoac very high performance. Create: <pre>aws elbv2 create-load-balancer --name my-nlb --type network --subnets subnet-xxx</pre></p><h4>Features</h4><ul><li>Layer 4 (TCP/UDP/TLS)</li><li>Static IP per AZ</li><li>Preserve client IP</li><li>Handle millions requests/second</li></ul><h4>vs ALB</h4><ul><li>NLB: Static IP, Layer 4</li><li>ALB: Dynamic IP, Layer 7</li></ul>`
            },
            {
                id: "4-9",
                title: "AWS Launch Template - Auto Scaling Group ( ASG ) - AWS",
                videoId: "jkK29xGhQZo",
                duration: "12:00",
                summary: "Auto Scaling tu dong dieu chinh so luong EC2 instances theo demand. Components: Launch Template (AMI, type, SG, user data), Auto Scaling Group (min/max/desired), Scaling Policies. Policies: Target tracking (keep CPU at 50%), Step scaling, Simple scaling. Metrics: CPUUtilization, Network, Custom CloudWatch. Cooldown: Thoi gian cho sau scaling action de tranh oscillation. Lifecycle hooks: Actions at scale-out/scale-in events. Health checks: ELB or EC2.",
                explanation: `<p>Auto Scaling tu dong dieu chinh so luong instances.</p><h4>Components</h4><ul><li>Launch Template</li><li>Auto Scaling Group</li><li>Scaling Policies</li></ul><h4>Metrics</h4><ul><li>CPU Utilization</li><li>Network</li><li>Custom</li></ul>`
            },
            {
                id: "4-10",
                title: "Auto Scaling in Action - How to Enable Automatic Scaling - AWS",
                videoId: "E2I4GT-AqHY",
                duration: "15:00",
                summary: "Tim hieu Auto Scaling trong AWS.",
                explanation: `<p>Auto Scaling tu dong dieu chinh so luong instances.</p><h4>Components</h4><ul><li>Launch Template</li><li>Auto Scaling Group</li><li>Scaling Policies</li></ul><h4>Metrics</h4><ul><li>CPU Utilization</li><li>Network</li><li>Custom</li></ul>`
            },
            {
                id: "4-11",
                title: "Auto Scaling With Load Balancer - Load Balancer with Auto Scaling - AWS",
                videoId: "9XWuCyf5F4c",
                duration: "12:00",
                summary: "Tim hieu Auto Scaling trong AWS.",
                explanation: `<p>Auto Scaling tu dong dieu chinh so luong instances.</p><h4>Components</h4><ul><li>Launch Template</li><li>Auto Scaling Group</li><li>Scaling Policies</li></ul><h4>Metrics</h4><ul><li>CPU Utilization</li><li>Network</li><li>Custom</li></ul>`
            },
            {
                id: "4-12",
                title: "Enable Termination Protection - Hibernet vs PowerOff - AWS",
                videoId: "Nbk6EGVzNL8",
                duration: "12:00",
                summary: "Bao ve instances khoi accidental termination.",
                explanation: `<p>Termination protection ngan chan xoa loi instances.</p><h4>Enable</h4><pre>aws ec2 modify-instance-attribute --instance-id i-xxx --disable-api-termination Value=true</pre>`
            },
            {
                id: "4-13",
                title: "How to create Reserve Instace - How to attach multiple NIC - AWS",
                videoId: "lcPkk8araGI",
                duration: "15:00",
                summary: "Multiple ENIs.",
                explanation: `<p>Multiple ENIs. Xem video de hieu chi tiet.</p>`
            },
        ]
    },
    {
        id: 5,
        title: "IAM - Identity & Access Management",
        description: "Quản lý users, groups, roles và policies để kiểm soát truy cập AWS resources",
        icon: "shield",
        lessons: [
            {
                id: "5-1",
                title: "AWS IAM Service - Identity and Access Management - AWS",
                videoId: "B1PpTEfVDw4",
                duration: "12:00",
                summary: "Quan ly truy cap voi IAM.",
                explanation: `<p>IAM quan ly truy cap AWS resources.</p><h4>Components</h4><ul><li>Users, Groups</li><li>Roles, Policies</li></ul>`
            },
            {
                id: "5-2",
                title: "AWS IAM Service - Groups in AWS - AWS",
                videoId: "3UAjLVGr-xg",
                duration: "12:00",
                summary: "Quan ly truy cap voi IAM.",
                explanation: `<p>IAM quan ly truy cap AWS resources.</p><h4>Components</h4><ul><li>Users, Groups</li><li>Roles, Policies</li></ul>`
            },
            {
                id: "5-3",
                title: "AWS IAM Service - Password Policy - AWS",
                videoId: "vVIgGvp1Xbg",
                duration: "12:00",
                summary: "Quan ly truy cap voi IAM.",
                explanation: `<p>IAM quan ly truy cap AWS resources.</p><h4>Components</h4><ul><li>Users, Groups</li><li>Roles, Policies</li></ul>`
            },
            {
                id: "5-4",
                title: "AWS Multi Factor Authentication - AWS MFA - AWS",
                videoId: "A2Bc5dOwx_c",
                duration: "12:00",
                summary: "Kich hoat MFA.",
                explanation: `<p>Kich hoat MFA. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "5-5",
                title: "How to use AWS CLI - AWS Configure - How to Create AWS Instance Using CLI - AWS",
                videoId: "nooY45x12Qw",
                duration: "15:00",
                summary: "Su dung AWS CLI.",
                explanation: `<p>Su dung AWS CLI. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "5-6",
                title: "AWS CLI Handle Multiple AWS Accounts - How to use AWS CLI In Linux -AWS",
                videoId: "tcQFWVcWBTY",
                duration: "15:00",
                summary: "Su dung AWS CLI.",
                explanation: `<p>Su dung AWS CLI. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "5-7",
                title: "What is AWS Roles & How to use AWS Cli without Access Id and Secret key - AWS",
                videoId: "OaoHJ0mb2ZE",
                duration: "15:00",
                summary: "Su dung IAM Roles thay vi Access Keys.",
                explanation: `<p>IAM Roles cung cap quyen tam thoi ma khong can access keys.</p><h4>Su dung Role</h4><ol><li>Tao IAM Role</li><li>Attach policy</li><li>Assume role</li></ol><h4>Benefits</h4><ul><li>Khong luu credentials</li><li>Auto rotation</li></ul>`
            },
            {
                id: "5-8",
                title: "What/Why is CloudShell || IAM - Access Advisor || IAM - Credential Report",
                videoId: "GdlAcq3Ek_s",
                duration: "12:00",
                summary: "Su dung AWS CloudShell va IAM reports.",
                explanation: `<p>CloudShell cung cap shell trinh trong browser.</p><h4>CloudShell</h4><ul><li>Pre-authenticated AWS CLI</li><li>Khong can setup</li></ul><h4>Access Advisor</h4><ul><li>Xem service permissions</li><li>Last accessed info</li></ul>`
            },
        ]
    },
    {
        id: 6,
        title: "Amazon S3",
        description: "Object storage - lưu trữ và quản lý files với các storage classes khác nhau",
        icon: "box",
        lessons: [
            {
                id: "6-1",
                title: "Introduction to Amazon Simple Storage Service (S3) | AWS S3 Service",
                videoId: "rrUA7jY_Cw8",
                duration: "12:00",
                summary: "Gioi thieu S3 object storage.",
                explanation: `<p>Gioi thieu S3 object storage. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "6-2",
                title: "AWS Tutorials - 60 How to Create Bucket in AWS | Create S3 Bucket | Create First Bucket",
                videoId: "MwFH65uTMXw",
                duration: "15:00",
                summary: "Tao va quan ly S3 bucket.",
                explanation: `<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>`
            },
            {
                id: "6-3",
                title: "AWS Tutorials - 61 Public your Bucket Object | Policy Generator | Allow Object to Public",
                videoId: "sWOkwp4Kd_I",
                duration: "12:00",
                summary: "Lam object public trong S3.",
                explanation: `<p>Lam object public trong S3. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "6-4",
                title: "AWS Tutorials - 62 S3 Object - S3 Object Properties - S3 Object Metadata - S3 Object Key",
                videoId: "Y6infh4tL_Q",
                duration: "12:00",
                summary: "Tim hieu S3 Object.",
                explanation: `<p>Tim hieu S3 Object. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "6-5",
                title: "S3 Versioning - What is Versioning - Prevent a Object from Deletion",
                videoId: "nzEsMgAfo6U",
                duration: "12:00",
                summary: "Su dung S3 Versioning de ngan chan xoa loi.",
                explanation: `<p>Versioning luu tru nhieu phien ban object.</p><h4>Enable</h4><pre>aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled</pre>`
            },
            {
                id: "6-6",
                title: "Host Static Website in S3 -How to host Static Website in S3",
                videoId: "cm626PlpSn8",
                duration: "15:00",
                summary: "Host static website tren S3.",
                explanation: `<p>S3 co the host static websites.</p><h4>Enable</h4><pre>Static website hosting in bucket properties</pre>`
            },
            {
                id: "6-7",
                title: "How to Redirect in S3 Static Website From one to another",
                videoId: "nRqzzzG_yfw",
                duration: "15:00",
                summary: "Host static website tren S3.",
                explanation: `<p>S3 co the host static websites.</p><h4>Enable</h4><pre>Static website hosting in bucket properties</pre>`
            },
            {
                id: "6-8",
                title: "How to Change Prefix in Static Website S3 - Redirect S3 Prefix in S3",
                videoId: "x6jdfAAZwU8",
                duration: "15:00",
                summary: "Host static website tren S3.",
                explanation: `<p>S3 co the host static websites.</p><h4>Enable</h4><pre>Static website hosting in bucket properties</pre>`
            },
            {
                id: "6-9",
                title: "S3 Accelerated Transfer, How to Enable? How to Use Accelerated Transfer?",
                videoId: "ATU9wfCqoNU",
                duration: "15:00",
                summary: "Su dung S3 Transfer Acceleration.",
                explanation: `<p>Transfer Acceleration tang toc do upload/download.</p><h4>Enable</h4><pre>aws s3api put-bucket-accelerate-configuration --bucket my-bucket --accelerate-configuration Status=Enabled</pre><h4>Su dung</h4><pre>https://my-bucket.s3-accelerate.amazonaws.com</pre>`
            },
            {
                id: "6-10",
                title: "Same/Cross Region Replication - What is SRR/CRR - Use of SRR/CRR?",
                videoId: "S2_Uuhl7768",
                duration: "12:00",
                summary: "Su dung S3 Replication de sao chep data.",
                explanation: `<p>S3 Replication tu dong sao chep objects.</p><h4>SRR</h4><ul><li>Sao chep trong cung region</li><li>Compliance, backup</li></ul><h4>CRR</h4><ul><li>Sao chep giua regions</li><li>DR, latency</li></ul>`
            },
            {
                id: "6-11",
                title: "AWS S3 - Configure Logging in S3 Bucket - How to Enable S3 Logging",
                videoId: "qJZ8PukZ0gY",
                duration: "15:00",
                summary: "Tao va quan ly S3 bucket.",
                explanation: `<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>`
            },
            {
                id: "6-12",
                title: "AWS S3 - Storage Classes - Standard - Infrequent - Glacier",
                videoId: "KoKBhXhQe60",
                duration: "12:00",
                summary: "Tim hieu cac S3 Storage Classes.",
                explanation: `<p>Chon dung storage class de toi uu chi phi.</p><h4>Classes</h4><ul><li>Standard: Truy cap thuong xuyen</li><li>IA: Truy cap it</li><li>Glacier: Luu tru lau dai</li></ul>`
            },
            {
                id: "6-13",
                title: "AWS S3 - Storage Classes - Configure Storage Class",
                videoId: "XrwIhGqN_NI",
                duration: "12:00",
                summary: "Tim hieu cac S3 Storage Classes.",
                explanation: `<p>Chon dung storage class de toi uu chi phi.</p><h4>Classes</h4><ul><li>Standard: Truy cap thuong xuyen</li><li>IA: Truy cap it</li><li>Glacier: Luu tru lau dai</li></ul>`
            },
            {
                id: "6-14",
                title: "Simplify Data Lifecycle Management with AWS S3 - ( AWS In Hindi )",
                videoId: "jfKz1IAe7Ws",
                duration: "12:00",
                summary: "Su dung S3 Lifecycle Policies.",
                explanation: `<p>Lifecycle policies tu dong chuyen doi hoac xoa objects.</p><h4>Tao Policy</h4><pre>Transitions: Move to Glacier after 30 days</pre><pre>Expiration: Delete after 365 days</pre><h4>Use Cases</h4><ul><li>Auto-archive</li><li>Delete old logs</li></ul>`
            },
            {
                id: "6-15",
                title: "Cost Efficiency and Performance with AWS Intelligent Tiering for S3",
                videoId: "2bVD29sC_lw",
                duration: "12:00",
                summary: "S3 Intelligent-Tiering.",
                explanation: `<p>S3 Intelligent-Tiering. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "6-16",
                title: "What is CORS and How To Enable IT in S3 - ( AWS In Hindi )",
                videoId: "5e4FlaHUPgY",
                duration: "15:00",
                summary: "Cau hinh CORS cho S3 bucket.",
                explanation: `<p>CORS cho phep web apps tu domain khac truy cap S3.</p><h4>Config</h4><pre>AllowedOrigins: https://mywebsite.com</pre><pre>AllowedMethods: GET, PUT</pre><h4>Use Cases</h4><ul><li>Static websites</li><li>SPAs</li></ul>`
            },
            {
                id: "6-17",
                title: "What is Presigned URL in S3 - ( AWS In Hindi )",
                videoId: "MQ9uPWq1TAk",
                duration: "12:00",
                summary: "Su dung Presigned URL de chia se private objects.",
                explanation: `<p>Presigned URL cho phep truy cap private objects.</p><h4>Tao</h4><pre>aws s3 presign s3://my-bucket/file.txt --expires-in 3600</pre><h4>Use Cases</h4><ul><li>Share files temporarily</li><li>Upload without credentials</li></ul>`
            },
            {
                id: "6-18",
                title: "Securing Your AWS S3 Data: At Rest, Server-Side, and Client-Side Encryption",
                videoId: "0ikAN6d5ZZ0",
                duration: "12:00",
                summary: "Bao mat S3 data voi encryption.",
                explanation: `<p>S3 cung cap nhieu muc do ma hoa.</p><h4>At Rest</h4><ul><li>SSE-S3: AWS managed keys</li><li>SSE-KMS: KMS keys</li><li>SSE-C: Customer keys</li></ul><h4>Enable SSE-S3</h4><pre>S3 > Properties > Default encryption</pre>`
            },
        ]
    },
    {
        id: 7,
        title: "CloudFront CDN",
        description: "Content Delivery Network - phân phối content toàn cầu với latency thấp",
        icon: "globe",
        lessons: [
            {
                id: "7-1",
                title: "What is Cloudfront ? Create First Distribution with EC2 Instance",
                videoId: "AjlUFYnScBk",
                duration: "15:00",
                summary: "Gioi thieu CloudFront CDN.",
                explanation: `<p>CloudFront la CDN giup deliver content nhanh hon.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>SSL support</li></ul><h4>Create Distribution</h4><pre>aws cloudfront create-distribution --origin-domain-name mylb.elb.amazonaws.com</pre>`
            },
            {
                id: "7-2",
                title: "AWS CloudFront Invalidation - How to Remove Data From CloudFront Edge -In Hindi",
                videoId: "vL1Eix6s_Pg",
                duration: "15:00",
                summary: "Invalidate cache trong CloudFront.",
                explanation: `<p>Invalidation xoa cache tu edge locations.</p><h4>Create</h4><pre>aws cloudfront create-invalidation --distribution-id XXXX --paths "/images/*"</pre><h4>Luu y</h4><ul><li>Co phi cho invalidations > 1000 paths</li></ul>`
            },
            {
                id: "7-3",
                title: "How to make EC2/ALB Instance Accessible from CloudFront Only -In Hindi",
                videoId: "rtuoqTslXbU",
                duration: "15:00",
                summary: "Bao mat origin chi cho phep CloudFront truy cap.",
                explanation: `<p>Chi cho phep traffic tu CloudFront den origin.</p><h4>Restrict Access</h4><ul><li>Tao CloudFront key pair</li><li>Whitelist CloudFront IPs</li></ul><h4>Security Groups</h4><ul><li>ALB SG chi tu CloudFront SG</li></ul>`
            },
            {
                id: "7-4",
                title: "CloudFront with S3 - S3 Private Bucket with CloudFront -S3 Origin - In Hindi",
                videoId: "R-BiyXJumr8",
                duration: "12:00",
                summary: "Ket hop CloudFront voi S3 private bucket.",
                explanation: `<p>Su dung CloudFront de access S3 private bucket.</p><h4>Use Cases</h4><ul><li>Protect S3 from direct access</li><li>Use signed URLs</li><li>Custom domain with SSL</li></ul><h4>OAI</h4><ul><li>Origin Access Identity</li></ul>`
            },
            {
                id: "7-5",
                title: "CloudFront Path Based routing with Mulitple Origin - Behavior - In Hindi",
                videoId: "NI6d5d7ycvY",
                duration: "12:00",
                summary: "Su dung CloudFront path-based routing.",
                explanation: `<p>CloudFront co the route den different origins theo path.</p><h4>Behaviors</h4><ul><li>/api/* -> API Gateway</li><li>/static/* -> S3</li><li>/* -> ALB</li></ul>`
            },
            {
                id: "7-6",
                title: "CloudFront Custom Error Page - CloudFront In Hindi - In Hindi",
                videoId: "yRcC31-5s5M",
                duration: "12:00",
                summary: "Tao custom error pages trong CloudFront.",
                explanation: `<p>Customize error responses.</p><h4>Error Pages</h4><ol><li>CloudFront > Distributions</li><li>Error Pages tab</li><li>Create custom error response</li></ol><h4>Options</h4><ul><li>Custom message</li><li>Redirect to URL</li></ul>`
            },
            {
                id: "7-7",
                title: "How to Control Access to Your Content Based on Country - CloudFront In Hindi",
                videoId: "a6Jhw1n55Mo",
                duration: "15:00",
                summary: "Kiem soat truy cap theo quoc gia voi CloudFront.",
                explanation: `<p>Geo-restriction kiem soat ai co the truy cap content.</p><h4>Enable</h4><ol><li>CloudFront > Distributions</li><li>Geographic restrictions</li><li>Whitelist or blacklist countries</li></ol><h4>Use Cases</h4><ul><li>Copyright compliance</li><li>Regional pricing</li></ul>`
            },
            {
                id: "7-8",
                title: "How to Disable CloudFront Distribution / How to Delete CloudFront Distribution",
                videoId: "zfj9nB1e20k",
                duration: "15:00",
                summary: "Xoa CloudFront distribution.",
                explanation: `<p>Cach disable hoac delete CloudFront.</p><h4>Disable</h4><ol><li>CloudFront > Distributions</li><li>Actions > Disable</li></ol><h4>Delete</h4><ol><li>Phai disable truoc</li><li>Wait for deployment</li><li>Actions > Delete</li></ol>`
            },
            {
                id: "7-9",
                title: "CloudFront Project Part - 1 - Setup Project Prerequisites - Deploy API Server",
                videoId: "Ji8oT2QI9Z8",
                duration: "15:00",
                summary: "Su dung CloudFront CDN.",
                explanation: `<p>CloudFront la CDN cua AWS.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>Caching</li></ul>`
            },
            {
                id: "7-10",
                title: "CloudFront Project Part - 2 - Cache Expire and Custom Header in Action",
                videoId: "lwo1YnFqyso",
                duration: "15:00",
                summary: "Su dung CloudFront CDN.",
                explanation: `<p>CloudFront la CDN cua AWS.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>Caching</li></ul>`
            },
            {
                id: "7-11",
                title: "CloudFront Project Part - 3 - Cache Key In Action - Query Params in CloudFront",
                videoId: "czw19xdJnU8",
                duration: "15:00",
                summary: "Su dung CloudFront CDN.",
                explanation: `<p>CloudFront la CDN cua AWS.</p><h4>Features</h4><ul><li>Global edge locations</li><li>Low latency</li><li>Caching</li></ul>`
            },
        ]
    },
    {
        id: 8,
        title: "Amazon VPC",
        description: "Virtual Private Cloud - tạo private network trong AWS với subnets, routing, NAT",
        icon: "shield",
        lessons: [
            {
                id: "8-1",
                title: "AWS VPC (Virtual Private Cloud )- Create First VPC - In Hindi",
                videoId: "N1KHVI_5s0o",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-2",
                title: "AWS VPC (Virtual Private Cloud )- Create First Subnet - In Hindi",
                videoId: "GETj1PdFVYs",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-3",
                title: "AWS VPC (Virtual Private Cloud)- Custom VPC and Subnet without IGW and Route Table",
                videoId: "5QrzHRwNWJg",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-4",
                title: "AWS VPC (Virtual Private Cloud)- Internet Gateway (IGW) and Route Table",
                videoId: "AkQKC-3COl4",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-5",
                title: "AWS VPC (Virtual Private Cloud) - Public and Private Subnet",
                videoId: "CPQlJBAhewk",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-6",
                title: "AWS VPC - How to Access Private Instance in AWS using bastion host",
                videoId: "KznYKBE1aig",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-7",
                title: "AWS VPC - How to access internet in Private Instance - NAT Instance",
                videoId: "_ySG_W5UinM",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-8",
                title: "AWS VPC - How to Access Internet in Private Instance - NAT Gateway",
                videoId: "bSL-SMfjMJU",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-9",
                title: "AWS VPC - NACL - Network Access Control List - What is NACL in AWS ? NACL vs SG",
                videoId: "O9AQE57PMAE",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-10",
                title: "AWS VPC - NACL - Create Network Access Control List",
                videoId: "v76TrfEhqO4",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-11",
                title: "AWS VPC - Cleanup",
                videoId: "2p29eceT8yg",
                duration: "8:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-12",
                title: "AWS VPC - VPC Peering and It's related Questions",
                videoId: "zU_8uNV7Mgs",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-13",
                title: "AWS VPC - Transit Gateway and Transit Gateway Attachments",
                videoId: "aMeFBGSNtpw",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-14",
                title: "AWS VPC - Transit Gateway and Transit Gateway Attachments - Part -2",
                videoId: "6G3YdtZByNM",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-15",
                title: "AWS VPC - Delete Transis Gateway - Clean up VPC",
                videoId: "_CRxj0VmrB8",
                duration: "8:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-16",
                title: "AWS VPC - VPC Flow Log - What is VPC Flow Log - AWS VPC Flow Logs",
                videoId: "5prSZdGcSQc",
                duration: "12:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-17",
                title: "What is VPC Endpoint - How to use VPC Endpoint - Gateway Endpoint",
                videoId: "xYX28OxSE_8",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
            {
                id: "8-18",
                title: "What is VPC Interface Endpoint - How to use VPC Endpoint - Interface Endpoint",
                videoId: "9naqQEJRuic",
                duration: "15:00",
                summary: "Virtual network voi VPC.",
                explanation: `<p>VPC tao virtual network trong AWS.</p><h4>Components</h4><ul><li>Subnets</li><li>Route Tables</li><li>Internet Gateway</li></ul>`
            },
        ]
    },
    {
        id: 9,
        title: "Amazon Route 53",
        description: "DNS service - quản lý domain, routing policies và health checks",
        icon: "globe",
        lessons: [
            {
                id: "9-1",
                title: "What is Site to Site VPN in AWS - Virtual Private Gateway",
                videoId: "MTEi0x5XcVw",
                duration: "12:00",
                summary: "Site-to-Site VPN ket noi your on-premises network den VPC over Internet. Components: Virtual Private Gateway (VGW), Customer Gateway (CGW), VPN Connection. How it works: Encrypted tunnel over Internet, Static hoac dynamic (BGP) routing. Performance: 1.25 Gbps per tunnel, Multiple tunnels supported. Use cases: Hybrid architectures, Extend on-premises to cloud. AWS VPN: Managed service, easy to setup.",
                explanation: `<p>Site-to-Site VPN ket noi on-prem voi AWS. Xem video de hieu them.</p>`
            },
            {
                id: "9-2",
                title: "Site to Site VPN in AWS - Virtual Private Gateway - Demo by @NetworkEvolution",
                videoId: "WgJc5LiXuCw",
                duration: "12:00",
                summary: "Site-to-Site VPN ket noi on-prem voi AWS.",
                explanation: `<p>Site-to-Site VPN ket noi on-prem voi AWS. Xem video de hieu them.</p>`
            },
            {
                id: "9-3",
                title: "Egress Only Internet Gateway in AWS - AWS in Hindi",
                videoId: "YCB6yL8VFgI",
                duration: "12:00",
                summary: "Egress Only Internet Gateway cho IPv6.",
                explanation: `<p>Egress Only Internet Gateway cho IPv6. Xem video de hieu them.</p>`
            },
            {
                id: "9-4",
                title: "Route53 - Overview - AWS Fully Managed DNS Service",
                videoId: "8gTFnNsgls8",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-5",
                title: "Route53 - Register Your First Domain in Route53 - AWS",
                videoId: "MfQrHeO-L8c",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-6",
                title: "Route53 - A Name and AAAA Record in Action - AWS",
                videoId: "wKQmYGe0BFw",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-7",
                title: "Route53 - CName Record in Action - AWS",
                videoId: "YctYXF63aZk",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-8",
                title: "Route53 - Alias in Action - Alias vs CNAME - AWS",
                videoId: "dwEi2ZgHFw0",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-9",
                title: "Route53 - TXT Record in Action - AWS",
                videoId: "Z3c7Sfe6XgY",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-10",
                title: "Route53 - Create Health Check in Route53 - AWS",
                videoId: "hfa7deY4ezw",
                duration: "15:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-11",
                title: "Route53 - Parent Health Check in Route53 in Action - AWS",
                videoId: "AZbirXdGmI4",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-12",
                title: "Route53 - Simple Routing Policy in Action - AWS",
                videoId: "OSB52J4FnAA",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-13",
                title: "Route53 - Weightage Routing Policy in Action - AWS",
                videoId: "0coIZfV4y4c",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-14",
                title: "Route53 - Geolocation Routing Policy in Action - AWS",
                videoId: "a-GZWSI5HLE",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-15",
                title: "Route53 - Latency Based Routing Policy in Action - AWS",
                videoId: "DKlSaceTHRc",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-16",
                title: "Route53 - Failover Routing Policy in Action - AWS",
                videoId: "4hFS0wIQzL8",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-17",
                title: "Route53 - Multivalue Answer Routing Policy in Action - AWS",
                videoId: "Dwwd2YHr2Qs",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-18",
                title: "Route53 - IP Based Routing Policy in Action - AWS",
                videoId: "vOO9aTF1-Dg",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-19",
                title: "Route53 - Cleanup - AWS",
                videoId: "mv4nOW2UBJw",
                duration: "8:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-20",
                title: "Route53 - Traffic Policy - AWS",
                videoId: "U5ixJmjJNxM",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-21",
                title: "Route53 - Logging - AWS",
                videoId: "DO9Uv9eyVG4",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-22",
                title: "Route53 - DNS Firewall - Block Websites/ Allow Websites - AWS",
                videoId: "lcj_GOE16U4",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-23",
                title: "Route53 - Private Hosted Zone - AWS",
                videoId: "8T5B-VszRbQ",
                duration: "12:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "9-24",
                title: "Hybrid DNS - DNS Inbound EndPoints - AWS",
                videoId: "1wa-qSlRiFE",
                duration: "12:00",
                summary: "Hybrid DNS cho phep DNS resolution giua on-premises va Route 53. Components: Inbound Endpoints (Route 53 receives queries), Outbound Endpoints (forward queries to on-premises), Resolver rules. Architecture: On-premises DNS <-> Inbound Endpoint <-> Route 53 Resolver <-> VPC. Use cases: Hybrid applications, Migration scenarios, Split-horizon DNS. Rules: Route queries based on domain names.",
                explanation: `<p>Hybrid DNS cau hinh on-prem va AWS. Xem video de hieu them.</p>`
            },
            {
                id: "9-25",
                title: "Hybrid DNS - DNS Outbound EndPoints - AWS",
                videoId: "lrGAd_PMIkY",
                duration: "12:00",
                summary: "Hybrid DNS cau hinh on-prem va AWS.",
                explanation: `<p>Hybrid DNS cau hinh on-prem va AWS. Xem video de hieu them.</p>`
            },
        ]
    },
    {
        id: 10,
        title: "Amazon RDS",
        description: "Managed database service - MySQL, PostgreSQL, Oracle, MariaDB, Aurora",
        icon: "database",
        lessons: [
            {
                id: "10-1",
                title: "Route53 - Cleanup - Delete Inbount and Outbound Endpoint - Delete Hosted Zone",
                videoId: "v5Mz6SL4UP0",
                duration: "8:00",
                summary: "Quan ly DNS voi Route 53.",
                explanation: `<p>Route 53 la DNS service cua AWS.</p><h4>Record Types</h4><ul><li>A, AAAA, CNAME</li><li>Alias, MX, TXT</li></ul>`
            },
            {
                id: "10-2",
                title: "Amazon RDS - Amazon Relational Database Service",
                videoId: "o98frpNl6cs",
                duration: "12:00",
                summary: "Gioi thieu Amazon RDS - managed database service.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Supported Engines</h4><ul><li>MySQL</li><li>PostgreSQL</li><li>MariaDB</li><li>Oracle</li><li>SQL Server</li><li>Aurora</li></ul><h4>Benefits</h4><ul><li>Automated backups</li><li>Multi-AZ</li><li>Read replicas</li><li>Automated patching</li></ul>`
            },
            {
                id: "10-3",
                title: "Amazon RDS - Create First Database",
                videoId: "syddeX5h1NM",
                duration: "15:00",
                summary: "Huong dan tao RDS instance dau tien.",
                explanation: `<p>Tao RDS database instance.</p><h4>Tao</h4><ol><li>RDS > Create database</li><li>Choose engine (MySQL, PostgreSQL)</li><li>Choose instance size</li><li>Configure VPC, Security Group</li><li>Set master password</li></ol><h4>CLI</h4><pre>aws rds create-db-instance --db-instance-identifier my-db --db-instance-class db.t3.micro --engine mysql</pre>`
            },
            {
                id: "10-4",
                title: "Amazon RDS - Connect to RDS Instance",
                videoId: "AcM8KQWR3S4",
                duration: "12:00",
                summary: "Ket noi den RDS instance.",
                explanation: `<p>Ket noi database tu EC2 hoac local machine.</p><h4>Tu EC2</h4><pre>mysql -h my-db.xxxx.us-east-1.rds.amazonaws.com -u admin -p</pre><h4>Security Group</h4><ul><li>Allow port 3306 (MySQL)</li><li>From EC2 SG or specific IP</li></ul><h4>Connection Issues</h4><ul><li>Check SG rules</li><li>Check subnet routing</li><li>Verify credentials</li></ul>`
            },
            {
                id: "10-5",
                title: "Amazon RDS - What is Read Replica - How to Create Read Replica",
                videoId: "G8bGuQ2vPZ0",
                duration: "15:00",
                summary: "Su dung Read Replica de giam load.",
                explanation: `<p>Read Replica tao ban doc-only cua database.</p><h4>Create</h4><pre>aws rds create-db-instance-read-replica --db-instance-identifier my-replica --source-db-instance-identifier my-db</pre><h4>Use Cases</h4><ul><li>Scale read operations</li><li>Cross-region replication</li><li>DR</li></ul><h4>Luu y</h4><ul><li>Async replication</li><li>May have slight lag</li></ul>`
            },
            {
                id: "10-6",
                title: "Amazon RDS - What is Multi AZ in RDS",
                videoId: "MPglvFh-l7M",
                duration: "12:00",
                summary: "Cau hinh Multi-AZ cho RDS.",
                explanation: `<p>Multi-AZ tao standby replica trong AZ khac.</p><h4>How it Works</h4><ul><li>Primary in AZ-1</li><li>Standby in AZ-2</li><li>Sync replication</li><li>Automatic failover</li></ul><h4>Create</h4><ol><li>Modify DB instance</li><li>Enable Multi-AZ</li></ol><h4>Benefits</h4><ul><li>High availability</li><li>Automatic failover</li><li>Zero data loss</li></ul>`
            },
            {
                id: "10-7",
                title: "Amazon RDS - What is Proxy in RDS",
                videoId: "LETUsRKEgNA",
                duration: "12:00",
                summary: "Su dung RDS Proxy de quan ly connections.",
                explanation: `<p>RDS Proxy giam so luong connections den database.</p><h4>Benefits</h4><ul><li>Connection pooling</li><li>Reduced CPU usage</li><li>Better scaling</li></ul><h4>Use Cases</h4><ul><li>Lambda functions</li><li>Serverless apps</li><li>Many short connections</li></ul>`
            },
            {
                id: "10-8",
                title: "Amazon RDS - Delete RDS, ReadReplica and Proxy in RDS",
                videoId: "xcOwOQgFvwQ",
                duration: "8:00",
                summary: "Managed database voi RDS.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>`
            },
            {
                id: "10-9",
                title: "Amazon RDS - AWS Aurora Database - Create First Aurora Instance",
                videoId: "C27KFj051z4",
                duration: "15:00",
                summary: "Gioi thieu Amazon Aurora va cach tao.",
                explanation: `<p>Aurora la MySQL/PostgreSQL-compatible database.</p><h4>Features</h4><ul><li>Up to 15 read replicas</li><li>Auto-sizing storage (10GB-128TB)</li><li>Multi-master</li><li>Backtrack</li></ul><h4>Create</h4><pre>aws rds create-db-cluster --engine aurora-mysql</pre>`
            },
            {
                id: "10-10",
                title: "Amazon RDS - Aurora Endpoints - Reader, Writer, Instance, Custom Endpoints",
                videoId: "D0rpISp9vVQ",
                duration: "12:00",
                summary: "Hieu ve cac loai Aurora Endpoints.",
                explanation: `<p>Aurora co nhieu endpoint types.</p><h4>Endpoints</h4><ul><li>Writer Endpoint: Primary instance</li><li>Reader Endpoint: Load-balanced read replicas</li><li>Instance Endpoint: Specific instance</li><li>Custom Endpoint: Custom group of instances</li></ul>`
            },
            {
                id: "10-11",
                title: "Amazon RDS - Aurora Endpoints - Read Replica",
                videoId: "DW78xSYuFKk",
                duration: "12:00",
                summary: "Managed database voi RDS.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>`
            },
            {
                id: "10-12",
                title: "Amazon RDS - Delete Aurora Database - Delete Aurora Read Replica",
                videoId: "ir319vFNWqU",
                duration: "8:00",
                summary: "Managed database voi RDS.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>`
            },
            {
                id: "10-13",
                title: "Amazon RDS - Cross Region Read Replica - Promote Read Replica",
                videoId: "nF4KDYLRojw",
                duration: "12:00",
                summary: "Managed database voi RDS.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>`
            },
            {
                id: "10-14",
                title: "Amazon RDS - Parameter Groups - How to change RDS Configurations",
                videoId: "FdUC6d2yffg",
                duration: "15:00",
                summary: "Managed database voi RDS.",
                explanation: `<p>RDS cung cap managed relational databases.</p><h4>Engines</h4><ul><li>MySQL, PostgreSQL</li><li>Aurora, Oracle</li></ul>`
            },
        ]
    },
    {
        id: 11,
        title: "Amazon DynamoDB",
        description: "NoSQL database - serverless, fully managed, single-digit millisecond latency",
        icon: "database",
        lessons: [
            {
                id: "11-1",
                title: "Amazon DynamoDB - How to Create Table in DynamoDB - How Partition Key Works",
                videoId: "PoJ2I2NAe34",
                duration: "15:00",
                summary: "Amazon DynamoDB la fully managed NoSQL database voi single-digit millisecond latency. Tables, Items, Attributes. Primary Key: Partition Key (required) + Sort Key (optional). Capacity modes: Provisioned va On-demand. Features: TTL, Streams, Global Tables, DAX (in-memory cache). Query: Tim items theo Partition Key, efficient. Scan: Doc toan bo table, tranh su dung trong production. Partitioning: Auto-scales based on data size va provisioned throughput.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-2",
                title: "Amazon DynamoDB - What is sort key - what is the use of sort key",
                videoId: "79xTeOtqsY8",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-3",
                title: "Amazon DynamoDB - Where I am utilizing DynamoDB. and what is Scan And Query",
                videoId: "Io1cNaIDHeo",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-4",
                title: "Amazon DynamoDB - Read and Write Capacity Units DynamoDB",
                videoId: "r2Cun-8wv8g",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-5",
                title: "Amazon DynamoDB - What is Local Secondary Index in DynamoDB",
                videoId: "1IJtgCn6jsg",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-6",
                title: "Amazon DynamoDB - What is Global Secondary Index in DynamoDB",
                videoId: "8ThDeWyLnXo",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-7",
                title: "Amazon DynamoDB - Point in Time Recovery and Backup in DynamoDB",
                videoId: "iIhPlHTLNOQ",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-8",
                title: "Amazon DynamoDB - DynamoDB Global Tables: Multi-Region Replication",
                videoId: "U8-oHjxcukg",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "11-9",
                title: "Amazon DynamoDB - Export DynamoDB Data to S3 Bucket",
                videoId: "J4Qxmx8YKfo",
                duration: "12:00",
                summary: "Tao va quan ly S3 bucket.",
                explanation: `<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>`
            },
            {
                id: "11-10",
                title: "Amazon DynamoDB - Import Data in DynamoDB From S3 Bucket",
                videoId: "1ixaFRlRgIs",
                duration: "12:00",
                summary: "Tao va quan ly S3 bucket.",
                explanation: `<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>`
            },
            {
                id: "11-11",
                title: "Amazon DynamoDB - How to Delete table from DynamoDb - Cleanup",
                videoId: "f2Gt1tPK-OY",
                duration: "15:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
        ]
    },
    {
        id: 12,
        title: "Amazon SES & SNS",
        description: "Notifications và Email - Simple Notification Service và Simple Email Service",
        icon: "mail",
        lessons: [
            {
                id: "12-1",
                title: "Amazon Simple Email Service - Where/How we can use it",
                videoId: "N39IEMQu7nw",
                duration: "12:00",
                summary: "Gioi thieu Amazon SES - email service.",
                explanation: `<p>SES la email service cho sending/receiving email.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing emails</li><li>Email verification</li></ul><h4>Benefits</h4><ul><li>Cost-effective</li><li>Scalable</li><li>Reliable</li></ul>`
            },
            {
                id: "12-2",
                title: "Amazon Simple Email Service - How to Verify Domain in Amazon SES",
                videoId: "O8lzXZ_WlEc",
                duration: "15:00",
                summary: "Email service voi SES.",
                explanation: `<p>SES gui email qua SMTP.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing</li></ul>`
            },
            {
                id: "12-3",
                title: "Email Service - How Emails End Up in Spam and How to Prevent It",
                videoId: "67udYWJ7TAE",
                duration: "15:00",
                summary: "Cach ngan chan email di vao Spam.",
                explanation: `<p>SPF, DKIM, DMARC giup email den inbox.</p><h4>SPF</h4><pre>v=spf1 include:_spf.amazonaws.com ~all</pre><h4>DKIM</h4><ul><li>Add DKIM record to DNS</li><li>AWS generates keys</li></ul><h4>DMARC</h4><pre>_dmarc.example.com TXT v=DMARC1; p=quarantine; rua=mailto:reports@example.com</pre>`
            },
            {
                id: "12-4",
                title: "Email Service - How to Customize Your Mail-From Domain in AWS SES",
                videoId: "kSLzjy6nj7o",
                duration: "15:00",
                summary: "Email service voi SES.",
                explanation: `<p>SES gui email qua SMTP.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing</li></ul>`
            },
            {
                id: "12-5",
                title: "Simple Notification Service - Send First Notification",
                videoId: "-rJUfbas8bA",
                duration: "12:00",
                summary: "Gui notification dau tien voi SNS.",
                explanation: `<p>Gui notification dau tien voi SNS. Xem video de hieu chi tiet.</p>`
            },
            {
                id: "12-6",
                title: "Simple Notification Service - Why should we use SNS - Configurations",
                videoId: "gz0dphCEK2s",
                duration: "12:00",
                summary: "Messaging voi SNS.",
                explanation: `<p>SNS la pub/sub messaging service.</p><h4>Components</h4><ul><li>Topics</li><li>Subscriptions</li></ul>`
            },
            {
                id: "12-7",
                title: "Simple Notification Service - Send Mobile SMS Notification",
                videoId: "e_JaORLCrZI",
                duration: "12:00",
                summary: "Gui SMS su dung SNS.",
                explanation: `<p>SNS co the gui SMS messages.</p><h4>Configure</h4><ol><li>Opt-in phone number</li><li>Create topic</li><li>Subscribe with SMS</li></ol><h4>Costs</h4><ul><li>Co phi cho moi SMS</li><li>Gia thay doi theo quoc gia</li></ul>`
            },
            {
                id: "12-8",
                title: "Simple Notification Service - Http/Https Endpoint Notification",
                videoId: "zm_AD_Qy8Sc",
                duration: "12:00",
                summary: "VPC Endpoints cho phep connect to AWS services ma khong can Internet gateway, NAT device, hoac VPN. Gateway Endpoints: S3, DynamoDB. Interface Endpoints: Other AWS services (private link). Benefits: More secure, Lower latency, No charges for gateway endpoints. Create: VPC > Endpoints > Create Endpoint. Routing: Traffic automatically routed through VPC endpoint.",
                explanation: `<p>VPC Endpoints de truy cap AWS services. Xem video de hieu them.</p>`
            },
        ]
    },
    {
        id: 13,
        title: "CloudWatch",
        description: "Monitoring và observability - metrics, logs, alarms, dashboards",
        icon: "activity",
        lessons: [
            {
                id: "13-1",
                title: "Cloud Watch Service - what/why CloudWatch - Introduction",
                videoId: "DD21R8SB9vk",
                duration: "12:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-2",
                title: "Email Service - Got SES Production Access",
                videoId: "KfrghyE7J3E",
                duration: "12:00",
                summary: "Email service voi SES.",
                explanation: `<p>SES gui email qua SMTP.</p><h4>Use Cases</h4><ul><li>Transactional emails</li><li>Marketing</li></ul>`
            },
            {
                id: "13-3",
                title: "Cloud Watch Service - Namespace and Custom Dashboard - Introduction",
                videoId: "16lPXx3SO3g",
                duration: "12:00",
                summary: "CloudWatch Dashboard hien thi metrics.",
                explanation: `<p>CloudWatch Dashboard hien thi metrics. Xem video de hieu them.</p>`
            },
            {
                id: "13-4",
                title: "Cloud Watch Service - Trigger Alert - Cloudwatch Alarm",
                videoId: "A63XO1D0qz4",
                duration: "12:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-5",
                title: "Cloud Watch Service - How to Create Billing Alarm - Cloudwatch Alarm",
                videoId: "z4uArBgRKR0",
                duration: "15:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-6",
                title: "Cloud Watch Service - Cloudwatch Composite Alarms - Cloudwatch Alarm",
                videoId: "z4RL_qzSje8",
                duration: "12:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-7",
                title: "Cloud Watch Service - Cloudwatch Agent Installation/Configure - Use",
                videoId: "tB_7cG7CAME",
                duration: "12:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-8",
                title: "AWS Cloud Watch Log - How to send application logs to Cloud watch - (InHindi)",
                videoId: "9xT0rCq2gCs",
                duration: "15:00",
                summary: "CloudWatch Logs de centralize logging.",
                explanation: `<p>CloudWatch Logs de centralize logging. Xem video de hieu them.</p>`
            },
            {
                id: "13-9",
                title: "AWS Cloud Watch Log Insights- Execute query on logs - (InHindi)",
                videoId: "LN1quwfxDxw",
                duration: "12:00",
                summary: "CloudWatch Logs de centralize logging.",
                explanation: `<p>CloudWatch Logs de centralize logging. Xem video de hieu them.</p>`
            },
            {
                id: "13-10",
                title: "How to Setup Alert Based on Cloudwatch Log - (InHindi)",
                videoId: "JMCr0HB3faU",
                duration: "15:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-11",
                title: "CloudWatch Create Custom Metrics from CLI - AWS in Hindi",
                videoId: "ssT8_zDQFyg",
                duration: "15:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
            {
                id: "13-12",
                title: "CloudWatch Cleanup - How to delete Resource from Cloudwatch - AWS in Hindi",
                videoId: "ZJD-1gbqp7g",
                duration: "15:00",
                summary: "Monitoring voi CloudWatch.",
                explanation: `<p>CloudWatch la monitoring service.</p><h4>Features</h4><ul><li>Metrics</li><li>Logs</li><li>Alarms</li></ul>`
            },
        ]
    },
    {
        id: 14,
        title: "AWS Lambda",
        description: "Serverless compute - chạy code không cần servers, trả tiền theo execution",
        icon: "zap",
        lessons: [
            {
                id: "14-1",
                title: "AWS Tutorial 172 - AWS Lambda in Hindi | What is Serverless & How to Create Your First Function",
                videoId: "lKSCAVp_vNg",
                duration: "15:00",
                summary: "AWS Lambda la serverless compute service cho phep chay code ma khong can servers. Features: Pay per invocation (never pay for idle), Auto scaling, Multiple runtimes (Node.js, Python, Java, Go, Ruby, .NET). Lambda cho phep upload code, chon runtime, va set memory/timeout. Execution time limit: 15 minutes. IAM execution role can be configured. Concurrency: 1000 default, can request increase. Layers: Share dependencies across functions.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-2",
                title: "AWS Tutorial 173 - AWS Lambda Basics in Hindi | Passing Data to Functions with Event Object",
                videoId: "3tt2vuguZqU",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-3",
                title: "AWS Tutorial 174 - How to Create and Test AWS Lambda Function URLs Using Postman - AWS Lambda",
                videoId: "PzlK6B6dEGU",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-4",
                title: "AWS Tutorial 175 - Events in AWS lambda - how to pass values - AWS Lambda",
                videoId: "GQ3lqMJMYpw",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-5",
                title: "AWS Tutorial 176 - AWS Lambda Hot Start vs Cold Start Explained | Practical Tips to Reduce Bill/Time",
                videoId: "VdVQEOfsnLk",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-6",
                title: "AWS Tutorial 177 - AWS Lambda Hot Start vs Cold Start Explained - Part 2",
                videoId: "gTWsuYsJ3x8",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-7",
                title: "AWS Tutorial 178 - AWS Lambda - General Configuration Settings - AWS in hindi",
                videoId: "nS1CedAntRY",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-8",
                title: "AWS Tutorial 179 - AWS Lambda - Context Object in Function - AWS in hindi",
                videoId: "JrfpFbYwmII",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-9",
                title: "AWS Tutorial 180 - AWS Lambda - Synchronous vs Asynchronous",
                videoId: "ynhyOGO4fUg",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-10",
                title: "AWS Tutorial 180 - AWS Lambda - Synchronous vs Asynchronous",
                videoId: "iMT9kWg5F5w",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-11",
                title: "AWS Tutorial 181.2 - AWS Lambda - Dead Latter Queue in Lamda - How to use it",
                videoId: "G5eWvxK6POk",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-12",
                title: "AWS Tutorial 182 - AWS Lambda - How to Trigger AWS Lambda on S3 Object Creation and Updates",
                videoId: "69NwOxAJOEw",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-13",
                title: "AWS Tutorial 182 - AWS Lambda - How to Trigger AWS Lambda From AWS Application Load Balancer",
                videoId: "WdaSaNzFID4",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-14",
                title: "AWS Tutorial 194 - AWS Lambda - Easily Create Events and Test AWS Lambda Functions",
                videoId: "UIQ-ZfXMEJE",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-15",
                title: "AWS Tutorial 203 - AWS Lambda - Reserved Concurrency and Provisioned Concurrency",
                videoId: "DK5U3HtE9qo",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-16",
                title: "186 - How to Write, Upload, and Use AWS Lambda Code from an S3 Bucket",
                videoId: "ojuXSWJ3Fxc",
                duration: "15:00",
                summary: "Tao va quan ly S3 bucket.",
                explanation: `<p>S3 bucket la container cho object storage.</p><h4>Commands</h4><pre>aws s3 mb s3://bucket-name</pre>`
            },
            {
                id: "14-17",
                title: "187 - How to use external libraries in Lambda Function - Install external library without layers",
                videoId: "3hJ63n-MgY0",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-18",
                title: "188 - How to use layers in Lambda Function - Install external library in layers",
                videoId: "7r1r3M7ZCvo",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-19",
                title: "AWS Tutorial 189 - AWS Lambda - Share your own library - Share your functions as Lambda Layers",
                videoId: "KDcm8ZTBhbA",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-20",
                title: "AWS Tutorial 190 - AWS Lambda - What is Version in AWS Lambda - How to use Lambda Version",
                videoId: "eeudeLjILR0",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-21",
                title: "AWS Tutorial 191 - AWS Lambda - What is Alias in AWS Lambda - How to use Alias in AWS Lambda",
                videoId: "BA3Lcghuq6I",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-22",
                title: "AWS Tutorial 192 - AWS Lambda - Resource Policy and IAM Role in AWS Lambda",
                videoId: "ceUWawKFzz0",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-23",
                title: "AWS Tutorial 193 - AWS Lambda - Lambda in VPC",
                videoId: "oePH3k0NI-w",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-24",
                title: "AWS Tutorial 195 - AWS Lambda - Easily Create Events & Test AWS Lambda Functions",
                videoId: "0Jfd-YfObV8",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-25",
                title: "AWS Tutorial 196 - How to Establish a Connection Between AWS Lambda and RDS | Step-by-Step Guide",
                videoId: "V9c2_d2fED4",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "14-26",
                title: "AWS Tutorial 197 - What is Reserved Concurrency and Provisioned Concurrency",
                videoId: "SgJFIdPj2Gs",
                duration: "12:00",
                summary: "Lambda Concurrency controls so luong functions co the run dong thoi. Reserved Concurrency: Guarantee maximum, Prevents function from using others. Provisioned Concurrency: Pre-warmed instances, Consistent latency, No cold starts. Use cases: Critical functions need guaranteed capacity, Predictable workloads, Latency-sensitive APIs. Auto Scaling: Configure provisioned concurrency with target tracking. Pricing: Reserved free, Provisioned charged per minute.",
                explanation: `<p>Lambda reserved va provisioned concurrency. Xem video de hieu them.</p>`
            },
        ]
    },
    {
        id: 15,
        title: "Amazon API Gateway",
        description: "Tạo, deploy và quản lý APIs - REST, HTTP, WebSocket",
        icon: "globe",
        lessons: [
            {
                id: "15-1",
                title: "AWS Lambda Destinations: What They Are & How They Enhance Your Serverless Architecture - 198",
                videoId: "ZQeNdTAD-Ak",
                duration: "14:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-2",
                title: "What's the REAL Purpose of API Gateway in AWS?",
                videoId: "E2hoC7Qf5T0",
                duration: "12:00",
                summary: "Amazon API Gateway la service de create, deploy, va manage APIs. Types: REST API (full features), HTTP API (lightweight), WebSocket API. Features: TLS/SSL termination, DDoS protection, throttling, Caching, Authorizers, API keys. Integrations: Lambda functions, HTTP backends. Deployment: APIs can be deployed to stages (dev, prod). CORS: Cross-origin resource sharing can be configured. Custom domain: Map your domain to API Gateway endpoints.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-3",
                title: "AWS API Gateway with HTTP Integrations - AWS Tutorials - AWS Beginner Guide",
                videoId: "G_OJz_lvoJ8",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-4",
                title: "AWS API Gateway Rest API Integrations with HTTP Server- AWS Tutorials - AWS Beginner Guide",
                videoId: "SA8rm7tfY_0",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-5",
                title: "AWS API Gateway - Rest API - Resource and Method - AWS tutorials for beginenrs - Http Server",
                videoId: "p19KqAQx_nY",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-6",
                title: "How to Integrate AWS API Gateway with AWS Lambda | Serverless API with AWS Lambda and API Gateway",
                videoId: "9Rsf_APUaGc",
                duration: "15:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-7",
                title: "Create Dummy APIs with API Gateway | API Gateway Mock Integration | No Backend Needed",
                videoId: "oShopYnhi-w",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-8",
                title: "API Gateway + DynamoDB Direct Integration | No Lambda Needed | Fast & Serverless",
                videoId: "SA7vHuxmqmo",
                duration: "12:00",
                summary: "Su dung DynamoDB NoSQL database.",
                explanation: `<p>DynamoDB la fully managed NoSQL database.</p><h4>Features</h4><ul><li>Single-digit ms latency</li><li>Auto scaling</li><li>Serverless</li></ul>`
            },
            {
                id: "15-9",
                title: "Path & Query String Parameters in API Gateway | AWS Tutorial in Hindi - AWS Tutorials Beginners",
                videoId: "QyvD3BxyPE4",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-10",
                title: "Headers in AWS API Gateway | AWS tutorials for beginners | AWS in Hindi | Amazon web service",
                videoId: "grEMR8zkGMU",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-11",
                title: "How Add Validation on API Gateway Level Using request method - AWS API Gateway - AWS API Gateway",
                videoId: "0RVRqbEFK4k",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-12",
                title: "Modify Requests Before Reach the Backend | Transform Request | AWS API Gateway | Request Integration",
                videoId: "ygBSnngJ9Kc",
                duration: "12:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-13",
                title: "How to modify Request Body Before Reach Backend | Integration Response | API Gateway | AWS Tutorial",
                videoId: "B8sk2w5OVjw",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-14",
                title: "Integration Request in API Gateway with AWS Lambda | API Gateway | AWS Tutorials | AWS tutorials",
                videoId: "BDq0zOUMaV4",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-15",
                title: "Your Lambda Works… But API Gateway Breaks It? Here's Why! | AWS API Gateway Method Response - Hindi",
                videoId: "3NPCLPpN7Ts",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-16",
                title: "Transform Lambda Responses in API Gateway (Without Changing Code!) | AWS API Gateway Tutorials",
                videoId: "hkjFy-8YAg0",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-17",
                title: "How to Authenticate API Gateway Using IAM Roles | Step-by-Step AWS Guide",
                videoId: "EMgiQAg_hw8",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-18",
                title: "How to Protect API Gateway Using API Keys | Full Setup & Demo in AWS",
                videoId: "fUnJC2fq5t4",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-19",
                title: "AWS Custom Authorizer Tutorial in Hindi | Secure APIs with Lambda & JWT | Custom Authorizer",
                videoId: "8tfaqHTKeMQ",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-20",
                title: "Pass User Info from Custom Authorizer to Lambda | Send Roles, IDs, Claims from Authorizer to Lambda",
                videoId: "8_SGd7jgJxs",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
            {
                id: "15-21",
                title: "Zero Downtime API Updates with AWS Lambda Alias & Versioning & Stage Variables",
                videoId: "GxizDg6DcNc",
                duration: "12:00",
                summary: "Su dung S3 Versioning de ngan chan xoa loi.",
                explanation: `<p>Versioning luu tru nhieu phien ban object.</p><h4>Enable</h4><pre>aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled</pre>`
            },
            {
                id: "15-22",
                title: "AWS API Gateway Canary Deployment | Zero Downtime Release Strategy",
                videoId: "JxLRpWL6xDk",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
            {
                id: "15-23",
                title: "How to Map Custom Domain to AWS API Gateway | Step-by-Step Guide",
                videoId: "Wn_v3qt6cuQ",
                duration: "15:00",
                summary: "Tao APIs voi API Gateway.",
                explanation: `<p>API Gateway tao va quan ly APIs.</p><h4>Types</h4><ul><li>REST API</li><li>HTTP API</li><li>WebSocket</li></ul>`
            },
        ]
    },
    {
        id: 16,
        title: "Amazon Cognito",
        description: "User authentication và authorization - user pools, identity pools, hosted UI",
        icon: "user",
        lessons: [
            {
                id: "16-1",
                title: "AWS Cognito | User Pool and App Setup – Say Goodbye to User Management Headaches! | AWS in Hindi",
                videoId: "pxtKDujnZnU",
                duration: "15:00",
                summary: "Authentication voi Cognito.",
                explanation: `<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>`
            },
            {
                id: "16-2",
                title: "AWS Cognito Token Flow Explained | ID, Access, Refresh Tokens, JWT Decode & Implicit Grant | Cognito",
                videoId: "gsojv1uH92s",
                duration: "12:00",
                summary: "Authentication voi Cognito.",
                explanation: `<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>`
            },
            {
                id: "16-3",
                title: "Customize AWS Cognito Hosted UI with CSS | Login & Signup UI Customization | AWS in Hindi By Gaurav",
                videoId: "ZIWUhtPL4Po",
                duration: "12:00",
                summary: "Authentication voi Cognito.",
                explanation: `<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>`
            },
            {
                id: "16-4",
                title: "Move AWS Cognito Hosted UI to Custom Domain Using Route 53 | AWS Cognito In hindi | AWS By Gaurav",
                videoId: "ODf1pNkAp4A",
                duration: "12:00",
                summary: "Authentication voi Cognito.",
                explanation: `<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>`
            },
            {
                id: "16-5",
                title: "AWS Cognito: User Profiles, Groups & Passwordless Login | AWS Cognito In Hindi By Gaurav | AWS Hindi",
                videoId: "X1enLKKT_qk",
                duration: "12:00",
                summary: "Authentication voi Cognito.",
                explanation: `<p>Cognito cung cap authentication cho apps.</p><h4>Features</h4><ul><li>User Pools</li><li>Identity Pools</li><li>Social login</li></ul>`
            },
            {
                id: "16-6",
                title: "Send Emails from Custom Domain using AWS Cognito + SES | Cognito, API Gateway & Lambda Explained",
                videoId: "4GS2jERqT8o",
                duration: "12:00",
                summary: "Serverless computing voi Lambda.",
                explanation: `<p>Lambda cho phep chay code ma khong can servers.</p><h4>Features</h4><ul><li>Pay per use</li><li>Auto scaling</li><li>Multiple runtimes</li></ul>`
            },
        ]
    },
    {
        id: 17,
        title: "AWS ECS",
        description: "Elastic Container Service - container orchestration, Fargate, EKS",
        icon: "server",
        lessons: [
            {
                id: "17-1",
                title: "AWS ECS Tutorial for Beginners | Create Your First ECS Cluster | AWS Tutorials in Hindi By Gaurav",
                videoId: "_4RvUXy2qjI",
                duration: "15:00",
                summary: "Container orchestration voi ECS.",
                explanation: `<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2</li><li>Fargate</li></ul>`
            },
            {
                id: "17-2",
                title: "How to Create ECS Cluster with Managed Instance | Step-by-Step Guide",
                videoId: "Hu4jep_43Zk",
                duration: "15:00",
                summary: "Container orchestration voi ECS.",
                explanation: `<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2</li><li>Fargate</li></ul>`
            },
            {
                id: "17-3",
                title: "AWS ECS Tutorial for Beginners | Task Definition, Tasks vs Service Explained Step-by-Step",
                videoId: "ombHxh34QJo",
                duration: "12:00",
                summary: "Container orchestration voi ECS.",
                explanation: `<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2</li><li>Fargate</li></ul>`
            },
            {
                id: "17-4",
                title: "How To Create a Service on ECS Cluster with Managed Node Instance | AWS Elastic Container Service",
                videoId: "zqQ3MaCjkQs",
                duration: "15:00",
                summary: "Container orchestration voi ECS.",
                explanation: `<p>ECS la container orchestration service.</p><h4>Launch Types</h4><ul><li>EC2</li><li>Fargate</li></ul>`
            },
        ]
    }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = modules;
}