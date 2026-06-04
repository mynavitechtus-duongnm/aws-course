#!/usr/bin/env python3
"""Update all lessons with comprehensive detailed content"""

with open('data.js', 'r') as f:
    content = f.read()

# Comprehensive content for all AWS topics
detailed_content = {
    # Module 1: Introduction
    "Introducing the AWS Playlist": {
        "summary": "Video giới thiệu tổng quan khóa học AWS Tutorials bằng tiếng Hindi. Gaurav Sharma giới thiệu về playlist học AWS từ cơ bản đến nâng cao, bao gồm hơn 180 bài học covering tất cả các dịch vụ AWS chính.",
        "explanation": "Khóa học AWS Tutorials của Gaurav Sharma là một trong những khóa học AWS miễn phí toàn diện nhất bằng tiếng Hindi, với hơn 180 bài học và 35+ giờ video content. Khóa học bao gồm: Phần 1: Giới thiệu AWS - Cloud Computing, AWS Infrastructure, Regions, Availability Zones. Phần 2: Amazon EC2 - Virtual Servers, Instance Types, Security Groups, SSH Access. Phần 3: EBS & Storage - Elastic Block Store, Snapshots, Volume Types. Phần 4: Load Balancer & Auto Scaling - ELB, ALB, NLB, ASG. Phần 5: IAM - Identity & Access Management, Users, Groups, Roles, Policies. Phần 6: Amazon S3 - Object Storage, Bucket Policies, Versioning, Lifecycle. Phần 7: CloudFront CDN - Content Delivery Network, Edge Locations. Phần 8: Amazon VPC - Virtual Private Cloud, Subnets, NAT Gateway. Phần 9: Route 53 - DNS Service, Routing Policies, Health Checks. Phần 10: RDS & DynamoDB - Managed Databases, Aurora, NoSQL. Phần 11: Lambda - Serverless Computing, Function Development. Phần 12: API Gateway - REST APIs, HTTP APIs, Integrations. Phần 13: Cognito - Authentication, User Pools, Identity Pools. Phần 14: ECS - Container Orchestration, Docker, Fargate."
    },
    "Traditional VS Cloud Computing": {
        "summary": "So sánh giữa Traditional Computing (On-premise) và Cloud Computing. Giải thích tại sao Cloud Computing là xu hướng tất yếu và lợi ích của việc sử dụng AWS thay vì tự xây dựng hạ tầng.",
        "explanation": "Trong bài học này, Gaurav Sharma giải thích sự khác biệt cơ bản giữa Traditional Computing (điện toán truyền thống) và Cloud Computing (điện toán đám mây). Traditional Computing đòi hỏi Capital Expenditure lớn, thời gian triển khai vài tuần đến vài tháng, cần đội ngũ kỹ thuật riêng, và khó khăn trong việc mở rộng. Cloud Computing cho phép Pay-as-you-go, triển khai trong vài phút, AWS quản lý infrastructure, và tự động scale theo demand. AWS chiếm 32% thị phần cloud computing toàn cầu với hơn 200 dịch vụ và 33 Regions trên toàn thế giới."
    },
    "Cloud Computing Service Models": {
        "summary": "Giải thích chi tiết 3 mô hình dịch vụ đám mây: IaaS, PaaS, và SaaS. So sánh vị trí kiểm soát của khách hàng trong mỗi mô hình.",
        "explanation": "Bài học này đi sâu vào 3 mô hình dịch vụ cloud computing. IaaS (Infrastructure as a Service) cung cấp tài nguyên hạ tầng ảo hóa như servers, storage, networking. AWS quản lý physical servers, data center, virtualization layer; bạn quản lý OS, applications, data, runtime. Ví dụ: EC2, S3, VPC. PaaS (Platform as a Service) cung cấp nền tảng để phát triển và deploy ứng dụng. AWS quản lý OS, runtime, middleware; bạn chỉ quản lý applications và data. Ví dụ: Lambda, Elastic Beanstalk, RDS. SaaS (Software as a Service) cung cấp ứng dụng hoàn chỉnh chạy trên cloud. AWS quản lý tất cả từ infrastructure đến ứng dụng. Ví dụ: Chime, WorkSpaces, Connect."
    },
    "Deployment Model": {
        "summary": "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud.",
        "explanation": "Bài học phân tích 3 deployment models. Public Cloud: tài nguyên được chia sẻ giữa nhiều organizations, hosted bởi AWS, chi phí thấp, scale linh hoạt. Private Cloud: cloud infrastructure dành riêng cho một organization, full control, enhanced security, phù hợp cho financial services, healthcare. Hybrid Cloud: kết hợp public cloud và private cloud, flexibility, cost optimization, web apps trên public cloud + databases trên private."
    },
    "AWS pricing": {
        "summary": "Giải thích cách AWS tính phí và các mô hình pricing: Pay-as-you-go, Reserved Instances, Savings Plans.",
        "explanation": "AWS sử dụng mô hình pricing linh hoạt: Pay for what you use, Pay less when you reserve, Pay even less with more. On-Demand: không commitment, trả theo giờ, phù hợp cho short-term projects. Reserved Instances: commitment 1-3 năm, giảm 30-72%. Savings Plans: thay thế linh hoạt hơn cho RIs, giảm đến 72%. Spot Instances: sử dụng unused capacity, giảm đến 90%, phù hợp cho batch processing, ML training. AWS Free Tier: Always Free (Lambda 1M requests, DynamoDB 25GB), 12 Months Free (EC2 750h, S3 5GB)."
    },
    # EC2 Lessons
    "EC2": {
        "summary": "Tìm hiểu Amazon EC2 - Virtual Servers trên AWS.",
        "explanation": "Amazon EC2 cung cấp scalable computing capacity trong AWS cloud. EC2 cho phép bạn tạo virtual machines (instances) với various instance types được tối ưu cho different use cases. Instance types bao gồm: General Purpose (T3, M5), Compute Optimized (C5), Memory Optimized (R5, X1E), Storage Optimized (D2, H3, I3), GPU instances (P4, G4). Bạn có thể chọn OS (Linux, Windows, macOS), configure networking, add storage, và secure với Security Groups."
    },
    "SSH": {
        "summary": "Hướng dẫn kết nối đến EC2 instance qua SSH.",
        "explanation": "SSH (Secure Shell) là protocol để kết nối secure đến EC2 instances. Với Linux/Mac: ssh -i key.pem ec2-user@public-ip. Quan trọng: chmod 400 key.pem để set correct permissions. Các lỗi thường gặp: Permission denied (cần chmod 400), Connection timeout (check Security Group allow port 22), Host key changed (ssh-keygen -R ip-address). Sau khi connect, bạn có thể update system (yum update hoặc apt update) và cài đặt packages."
    },
    "Windows": {
        "summary": "Hướng dẫn kết nối đến EC2 Windows instance qua RDP.",
        "explanation": "Để kết nối Windows instance, bạn cần Remote Desktop Protocol (RDP). Từ AWS Console: Tải RDP file, lấy password sử dụng key pair. Từ Linux: Sử dụng Remmina hoặc rdesktop (sudo apt install remmina remmina-plugin-rdp). Security Group cần mở port 3389 (RDP) từ IP của bạn. Username mặc định là Administrator."
    },
    "Nginx": {
        "summary": "Hướng dẫn cài đặt Nginx web server trên EC2 instance.",
        "explanation": "Nginx là high-performance web server và reverse proxy. Cài đặt trên Amazon Linux: sudo yum update -y && sudo amazon-linux-extras install nginx1 && sudo systemctl start nginx && sudo systemctl enable nginx. Cài đặt trên Ubuntu: sudo apt update && sudo apt install nginx. Sau khi cài đặt, nginx listen on port 80. Cần mở port 80 trong Security Group. Configuration files nằm trong /etc/nginx/. Default document root: /usr/share/nginx/html/."
    },
    "User Data": {
        "summary": "Hướng dẫn sử dụng User Data script để tự động chạy commands khi EC2 instance khởi tạo.",
        "explanation": "User Data cho phép chạy scripts tự động khi EC2 instance start lần đầu. Use cases: Install software (nginx, apache), configure applications, download code từ S3, setup monitoring agents. Example User Data: #!/bin/bash followed by commands như yum update -y, amazon-linux-extras install nginx1 -y, systemctl start nginx. Để xem logs: sudo cat /var/log/cloud-init-output.log. User Data được chạy với root privileges."
    },
    "Security Groups": {
        "summary": "Giải thích Security Groups - virtual firewall cho EC2 instances.",
        "explanation": "AWS Security Group là stateful virtual firewall kiểm soát traffic vào và ra của EC2 instances. Stateful: Nếu bạn allow inbound traffic, outbound traffic được tự động allowed. Mỗi instance có thể có nhiều Security Groups. Rules bao gồm: Protocol (TCP, UDP, ICMP, All), Port range, Source/Destination (IP address, CIDR, hoặc Security Group khác). Best practice: Chỉ allow những ports cần thiết, use specific IP ranges thay vì 0.0.0.0/0."
    },
    "Instance Types": {
        "summary": "Tổng quan về các loại EC2 Instance Types.",
        "explanation": "AWS cung cấp hơn 500 instance types được tối ưu cho các use cases khác nhau. Instance families: General Purpose (T3, M5, M6i) - balanced compute/memory/storage, phù hợp cho web servers, dev environments. Compute Optimized (C5, C6i) - high performance processors, phù hợp cho batch processing, scientific modeling. Memory Optimized (R5, R6i, X1E) - large memory footprint, phù hợp cho databases, in-memory caches. Storage Optimized (D2, H3, I3) - high disk throughput, phù hợp cho data warehousing, log processing. GPU instances (P4, G4, Inf1) - machine learning, graphics rendering."
    },
    "Elastic IP": {
        "summary": "Cách gán Elastic IP address cho EC2 instance.",
        "explanation": "Elastic IP là static public IPv4 address có thể gán cho instances. Tạo: EC2 Dashboard > Elastic IPs > Allocate. Gán: Actions > Associate Elastic IP address. CLI: aws ec2 associate-address --instance-id i-xxx --public-ip x.x.x.x. Use cases: Static IP cho website, whitelist IP in firewall, point DNS records. Chi phí: Free nếu associated với running instance, $0.005/giờ nếu not associated. Best practice: Không nên rely hoàn toàn vào EIP, consider Route 53 cho DNS-based failover."
    },
    # EBS Lessons
    "EBS": {
        "summary": "Tìm hiểu EBS volumes - block storage cho EC2.",
        "explanation": "Amazon Elastic Block Store (EBS) cung cấp block storage volumes cho EC2 instances. EBS volumes là network-attached storage, persist independently of instance lifecycle. Volume types: gp3 (general purpose SSD, 3000-16000 IOPS, $0.08/GB), gp2 (legacy gp), io2 (high performance SSD, 64000 IOPS, 99.999% durability), st1 (throughput optimized HDD), sc1 (cold storage HDD). EBS volumes được automatically replicated trong AZ để protect khỏi component failure."
    },
    "Mount EBS": {
        "summary": "Hướng dẫn tạo EBS volume và mount vào EC2 Linux.",
        "explanation": "Tạo volume: EC2 > Volumes > Create Volume, chọn size, type (gp3), AZ. Attach: Actions > Attach Volume, chọn instance trong cùng AZ. Mount trên Linux: lsblk để check available disks, sudo mkfs -t xfs /dev/xvdf để format, sudo mkdir /mnt/data && sudo mount /dev/xvdf /mnt/data để mount. Add to /etc/fstab for auto-mount: /dev/xvdf /mnt/data xfs defaults,nofail 0 2."
    },
    "EBS Snapshot": {
        "summary": "Hướng dẫn tạo EBS snapshot để backup volume.",
        "explanation": "EBS Snapshots là incremental backups được lưu trong S3. Tạo: Select volume > Actions > Create Snapshot. CLI: aws ec2 create-snapshot --volume-id vol-xxx. Snapshots are incremental: chỉ changes được saved, deleting a snapshot chỉ xóa unique data. Benefits: disaster recovery, volume migration, AMI creation, compliance backup. Encrypted volumes tạo ra encrypted snapshots automatically. Có thể copy snapshots across regions hoặc share với other AWS accounts."
    },
    "Lifecycle Manager": {
        "summary": "Tự động hóa backup EBS volumes sử dụng Data Lifecycle Manager.",
        "explanation": "EBS Lifecycle Manager tự động hóa snapshot creation và retention. Tạo policy: EC2 > Lifecycle Manager > Create lifecycle policy. Configure: Resource type (Volume), Target with tags, Schedule (daily, weekly), Retention count. Options: Frequency (hourly, daily, weekly), Retention (số snapshots giữ lại), Copy tags to snapshots, Cross-region copies. Benefits: Automated backups, consistent scheduling, automatic cleanup old snapshots, cost optimization."
    },
    "AMI": {
        "summary": "Tạo custom AMI từ EC2 instance.",
        "explanation": "Amazon Machine Image (AMI) là blueprint để launch instances với pre-configured software. Tạo: Select instance > Actions > Image > Create image. CLI: aws ec2 create-image --instance-id i-xxx --name My-AMI. AMI components: Root volume snapshot, Launch permissions, Block device mappings. Use cases: Pre-configured instances, consistent deployments, faster instance launch, version control for configurations. Có thể share AMIs với other AWS accounts hoặc make public."
    },
    # Load Balancer Lessons
    "Load Balancer": {
        "summary": "Giới thiệu Elastic Load Balancing - phân phối traffic.",
        "explanation": "Elastic Load Balancer (ELB) phân phối incoming traffic đến multiple targets như EC2 instances, containers, IP addresses. Load balancer types: Application LB (ALB) - Layer 7, HTTP/HTTPS, advanced routing (path-based, host-based). Network LB (NLB) - Layer 4, TCP/UDP, static IP per AZ, ultra-low latency. Gateway LB - Layer 3, virtual appliances. Classic LB (CLB) - legacy, both layers (deprecated). ELB features: High availability, health checks, SSL termination, sticky sessions, CloudWatch monitoring."
    },
    "ALB": {
        "summary": "Tìm hiểu Application Load Balancer - Layer 7 LB.",
        "explanation": "Application Load Balancer hoạt động ở Layer 7 (HTTP/HTTPS). Features: Path-based routing (/api/* → API targets, /images/* → S3), Host-based routing, Query string routing, Header-based routing, HTTP/2 và WebSocket support. Components: Load Balancer (entry point), Listeners (port và protocol), Target Groups (group of targets), Rules (route traffic). ALB is ideal cho microservices architecture, multiple services on same port, blue-green và canary deployments."
    },
    "NLB": {
        "summary": "Tìm hiểu Network Load Balancer - Layer 4 LB.",
        "explanation": "Network Load Balancer hoạt động ở Layer 4 (TCP/UDP/TLS). Features: Static IP per AZ, Preserve client IP, Handle millions of requests/second, 99.99% SLA. vs ALB: NLB cung cấp static IP và ultra-low latency; ALB cung cấp HTTP-level routing và content-based routing. Use cases: High performance applications, gaming servers, IoT protocols, non-HTTP applications. NLB is best khi bạn cần static IP addresses hoặc very high performance."
    },
    # Auto Scaling Lessons
    "Auto Scaling": {
        "summary": "Tìm hiểu Auto Scaling - tự động điều chỉnh số lượng instances.",
        "explanation": "Auto Scaling tự động điều chỉnh số lượng EC2 instances theo demand. Components: Launch Template (AMI, instance type, SG, user data), Auto Scaling Group (min/max/desired capacity, network config), Scaling Policies (when to scale). Scaling policies types: Target tracking (keep CPU at 50%), Step scaling (add 2 instances when CPU > 70%), Simple scaling (add when > 80%, wait 300s). Metrics: CPUUtilization, NetworkIn/Out, RequestCountPerTarget, Custom CloudWatch metrics. Cooldown: thời gian chờ sau scaling action để prevent oscillation."
    },
    # IAM Lessons
    "IAM": {
        "summary": "Tìm hiểu AWS IAM - Identity and Access Management.",
        "explanation": "IAM cho phép bạn quản lý truy cập an toàn đến AWS services và resources. Components: Users (individual people), Groups (collection of users with shared permissions), Roles (quyền tạm thời cho services/users), Policies (JSON documents defining permissions). Features: Fine-grained permissions, Multi-factor authentication (MFA), Password policy (minimum length, complexity), Access keys rotation. IAM Best Practices: Enable MFA for all users, use groups instead of individual users, follow principle of least privilege, regular review permissions."
    },
    "MFA": {
        "summary": "Kích hoạt MFA cho tài khoản AWS.",
        "explanation": "Multi-Factor Authentication (MFA) tăng cường bảo mật bằng cách yêu cầu second form of authentication. Loại MFA devices: Virtual (Google Authenticator, Authy, Microsoft Authenticator), Hardware (YubiKey, Gemalto), SMS (deprecated for root). Enable MFA: IAM > Users > Security credentials > Assign MFA device, scan QR code with authenticator app, enter 2 consecutive codes. Best practice: Enable MFA cho tất cả users, đặc biệt là root account và admin users."
    },
    "CLI": {
        "summary": "Hướng dẫn cài đặt và sử dụng AWS CLI.",
        "explanation": "AWS Command Line Interface (CLI) cho phép bạn tương tác với AWS services bằng commands. Cài đặt: pip install awscli hoặc brew install awscli. Configure: aws configure (AWS Access Key ID, Secret Access Key, Default region, Output format). Sử dụng profiles: aws configure --profile production. Common commands: aws ec2 describe-instances, aws s3 ls, aws lambda invoke. CLI có thể handle multiple AWS accounts bằng cách sử dụng named profiles và environment variable AWS_PROFILE."
    },
    # S3 Lessons
    "S3": {
        "summary": "Tìm hiểu Amazon S3 - Object Storage.",
        "explanation": "Amazon S3 (Simple Storage Service) cung cấp object storage với 99.999999999% durability. Components: Buckets (container for objects, globally unique name), Objects (files with metadata, identified by key), Keys (unique identifier: bucket name + object key). Features: Multiple storage classes, Versioning, Lifecycle policies, Encryption, Access control. Storage classes: Standard (frequent access), IA (infrequent access), Glacier (long-term archive, retrieval minutes to hours), Deep Archive (cheapest, retrieval 12 hours), Intelligent-Tiering (auto-tiering)."
    },
    "S3 Bucket": {
        "summary": "Tạo và quản lý S3 buckets.",
        "explanation": "S3 Bucket là container để lưu trữ objects. Tạo bucket: S3 > Create bucket (name phải globally unique, chọn region). CLI: aws s3 mb s3://my-unique-bucket-name. Bucket naming: 3-63 characters, lowercase letters/numbers/dots/hyphens, không được là IP address. Permissions: Block all public access (recommended for most cases). Versioning: Enable để track object versions. Tags: Dùng tags để organize và filter buckets."
    },
    "S3 Versioning": {
        "summary": "Sử dụng S3 Versioning để lưu nhiều phiên bản object.",
        "explanation": "S3 Versioning lưu trữ tất cả versions của một object khi bạn overwrite hoặc delete nó. Enable: aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled. Benefits: Protect against accidental deletes (delete marker được thêm, object vẫn còn), Restore previous versions, Audit changes. Storage: Mỗi version tốn storage space và phí. Pricing: Bạn trả tiền cho tất cả versions được lưu."
    },
    "S3 Lifecycle": {
        "summary": "Sử dụng S3 Lifecycle Policies để tự động quản lý objects.",
        "explanation": "Lifecycle policies tự động chuyển đổi hoặc xóa objects theo thời gian. Tạo policy: S3 > Bucket > Management > Lifecycle rule. Actions: Transition (chuyển sang storage class khác: Standard IA sau 30 ngày, Glacier sau 90 ngày), Expiration (xóa sau X ngày, xóa incomplete uploads). Use cases: Auto-archive to Glacier, Delete old logs, Reduce storage costs. Example: Move to IA after 30 days, Glacier after 90 days, Delete after 365 days."
    },
    "S3 Encryption": {
        "summary": "Mã hóa S3 data - SSE-S3, SSE-KMS, SSE-C.",
        "explanation": "S3 cung cấp nhiều options để encrypt data at rest. SSE-S3: AWS quản lý keys, sử dụng AES-256, enable bằng bucket settings. SSE-KMS: Sử dụng AWS KMS keys, cung cấp audit trail cho key usage, có thể tạo custom keys. SSE-C: Customer-provided keys, AWS không lưu keys. Client-side: Encrypt trước khi upload, bạn quản lý keys hoàn toàn. Best practice: Enable default encryption cho buckets, sử dụng SSE-KMS cho sensitive data."
    },
    "S3 Presigned URL": {
        "summary": "Sử dụng Presigned URLs để chia sẻ private objects.",
        "explanation": "Presigned URL cho phép bạn cấp quyền truy cập tạm thời đến objects mà không cần thay đổi bucket permissions. Tạo: aws s3 presign s3://my-bucket/private-file.txt --expires-in 3600. URL có query parameters chứa signature và expiration. Use cases: Share files temporarily, Upload without credentials, Time-limited access. Expiration: 1 minute to 7 days. Best practice: Sử dụng short expiration cho sensitive data."
    },
    # CloudFront Lessons
    "CloudFront": {
        "summary": "Tìm hiểu CloudFront CDN - Content Delivery Network.",
        "explanation": "Amazon CloudFront là Content Delivery Network (CDN) giúp deliver content với low latency và high transfer speeds. How it works: User requests content → CloudFront edge location → Origin (S3/ALB/EC2) → Cache → Return to user. Features: Global edge locations (400+ locations), Cache behavior, SSL/TLS support, Signed URLs/Cookies, Geo-restriction, CloudFront Functions. Distributions: Web distributions (websites, APIs) và RTMP (streaming media, deprecated). Invalidation: Xóa cache trước khi expiration."
    },
    # VPC Lessons
    "VPC": {
        "summary": "Tìm hiểu Amazon VPC - Virtual Private Cloud.",
        "explanation": "Amazon VPC cho phép bạn tạo virtual network riêng trong AWS cloud. Components: VPC (10.0.0.0/16 default), Subnets (public và private), Route Tables (routing rules), Internet Gateway (Internet access), NAT Gateway (private subnet to Internet), Security Groups và NACLs (firewall). Architecture: Public subnets cho resources cần Internet access (web servers, NAT Gateway), Private subnets cho databases, app servers. VPC CIDR: Use RFC 1918 addresses (10.0.0.0/16, 172.16.0.0/12, 192.168.0.0/16)."
    },
    "Internet Gateway": {
        "summary": "Tạo và cấu hình Internet Gateway.",
        "explanation": "Internet Gateway cho phép VPC kết nối Internet. Tạo: aws ec2 create-internet-gateway. Attach to VPC: aws ec2 attach-internet-gateway --vpc-id vpc-xxx. Route Table: Thêm route 0.0.0.0/0 → igw-xxx. Subnets cần route đến IGW được gọi là Public Subnets. Resources in public subnets có thể access Internet (nếu có Elastic IP) và receive connections từ Internet."
    },
    "NAT Gateway": {
        "summary": "Cấu hình NAT Gateway để Private Subnets truy cập Internet.",
        "explanation": "NAT Gateway cho phép instances in private subnets truy cập Internet outbound mà không cho phép inbound connections. Tạo: NAT Gateway in public subnet, allocate Elastic IP. Update Route Table của private subnet: Add route 0.0.0.0/0 → nat-xxx. NAT Gateway là managed service, highly available trong AZ. Costs: $0.045 per GB data processed + Elastic IP charge. Alternative: NAT Instance (tự quản lý, cheaper nhưng cần more configuration)."
    },
    "VPC Peering": {
        "summary": "Kết nối VPCs với VPC Peering.",
        "explanation": "VPC Peering cho phép kết nối hai VPCs để traffic flow giữa chúng. Features: Non-transitive (A ↔ B không có nghĩa A ↔ C), No overlapping CIDRs, Low latency, No single point of failure. Create: aws ec2 create-vpc-peering-connection. Accept: aws ec2 accept-vpc-peering-connection. Update Route Tables ở cả hai VPCs để enable traffic. Use cases: Cross-account resources, Microservices architecture, Shared services."
    },
    # Route 53 Lessons
    "Route 53": {
        "summary": "Tìm hiểu Amazon Route 53 - DNS Service.",
        "explanation": "Amazon Route 53 là highly available và scalable DNS web service. Functions: DNS queries (translate domain names → IP addresses), Domain registration, Health checking. Record types: A (IPv4 address), AAAA (IPv6), CNAME (alias to another domain), Alias (AWS-specific, free), MX (mail), TXT (verification), SPF. Routing policies: Simple (single resource), Weighted (percentage-based), Latency-based, Geolocation, Failover (DR), Multi-value answer. Health checks: Monitor endpoints, Automatic failover."
    },
    "Route 53 Health Check": {
        "summary": "Cấu hình Health Checks trong Route 53.",
        "explanation": "Route 53 health checks monitor endpoints và tự động remove unhealthy resources khỏi DNS responses. Types: Endpoint (HTTP/HTTPS/TCP), CloudWatch alarm, Calculated (combine multiple checks). Configuration: Protocol, IP address hoặc domain, Port, Path (for HTTP), Interval (10s hoặc 30s). Health checkers: 8-18 locations globally. Failover routing: Kết hợp health check với failover routing policy để automatic DR. Latency check: Route đến region có latency thấp nhất."
    },
    "Route 53 Routing": {
        "summary": "Các Routing Policies trong Route 53.",
        "explanation": "Route 53 cung cấp nhiều routing policies: Simple - single resource, returns one record. Weighted - phân phối traffic theo percentage (VD: 80% → us-east-1, 20% → eu-west-1), hữu ích cho blue-green deployment và A/B testing. Latency - route đến region có latency thấp nhất cho user. Geolocation - route dựa trên vị trí địa lý của user (VD: US users → US servers, EU users → EU servers). Failover - active-passive DR, primary resource healthy thì sử dụng, không thì failover sang secondary. Multi-value answer - return multiple values với health checks."
    },
    # RDS Lessons
    "RDS": {
        "summary": "Tìm hiểu Amazon RDS - Managed Database Service.",
        "explanation": "Amazon RDS là managed relational database service hỗ trợ multiple database engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Amazon Aurora. Features: Automated backups (daily snapshots, point-in-time recovery), Multi-AZ deployment (synchronous replication, automatic failover), Read replicas (async replication, scale reads), Automated patching và backups, Security (encryption at rest, VPC isolation). RDS vs EC2 database: RDS managed everything (OS, DB software, patches), easier operations, less control. Aurora: MySQL và PostgreSQL compatible, up to 15 read replicas, auto-scaling storage."
    },
    "RDS Multi-AZ": {
        "summary": "Cấu hình Multi-AZ cho RDS database.",
        "explanation": "RDS Multi-AZ deployment tạo standby replica trong AZ khác để high availability. How it works: Primary DB in AZ-1, Standby DB in AZ-2, Synchronous replication đảm bảo zero data loss, Automatic failover trong ~60 seconds khi primary fails. Enable: Modify DB instance > Enable Multi-AZ. Failover triggers: AZ failure, instance failure, storage failure. During failover: Connection string giữ nguyên, RDS tự động switch DNS. Use cases: Production workloads, Applications requiring high availability."
    },
    "RDS Read Replica": {
        "summary": "Sử dụng Read Replicas để scale database reads.",
        "explanation": "RDS Read Replicas cho phép bạn scale database reads bằng cách tạo read-only copies. Benefits: Scale read capacity (15 max for Aurora, 5 for MySQL/PostgreSQL), Reduce load on primary, Cross-region replication cho DR. How it works: Async replication từ primary, Replicas có own endpoint, Application có thể distribute reads across primary và replicas. Use cases: Reporting queries, Read-heavy workloads, Cross-region deployment. Promotion: Có thể promote replica thành standalone instance (breaks replication)."
    },
    # DynamoDB Lessons
    "DynamoDB": {
        "summary": "Tìm hiểu Amazon DynamoDB - Serverless NoSQL Database.",
        "explanation": "Amazon DynamoDB là fully managed NoSQL database với single-digit millisecond latency ở any scale. Data model: Tables (collection of items), Items (rows, max 400KB), Attributes (columns). Keys: Partition Key (PK) - required, determines data distribution, Sort Key (SK) - optional, enables hierarchical queries. Capacity modes: Provisioned (specify RCU/WCU), On-demand (pay per request). Features: TTL, Streams (capture item changes), Global Tables (multi-region replication), DAX (in-memory cache). Partitioning: DynamoDB automatically partitions based on PK cardinality."
    },
    "DynamoDB Query Scan": {
        "summary": "Sử dụng Query và Scan trong DynamoDB.",
        "explanation": "Query và Scan là hai cách để đọc data từ DynamoDB. Query: Tìm items dựa trên Partition Key (bắt buộc) và Sort Key condition (tùy chọn). Efficient - chỉ đọc necessary items. Best practice - luôn sử dụng Query khi có thể. Scan: Đọc toàn bộ table hoặc secondary index. Inefficient - đọc tất cả items, tốn nhiều RCU. Nên tránh trong production. Pagination: DynamoDB paginates results (1MB per page). FilterExpression: Lọc results sau khi đọc, không giảm RCU."
    },
    "DynamoDB GSI": {
        "summary": "Sử dụng Global Secondary Index (GSI).",
        "explanation": "Global Secondary Index (GSI) cho phép bạn query on attributes khác ngoài primary key. Create: aws dynamodb update-table --global-secondary-index-updates. Partition Key: Có thể khác với table's PK. Use cases: Query by different attributes, Alternative access patterns, Create different sort keys. Considerations: Provisioned throughput riêng, Additional storage costs, eventual consistency by default. Best practice: Thiết kế GSIs carefully vì thay đổi GSI là expensive operation."
    },
    # Lambda Lessons
    "Lambda": {
        "summary": "Tìm hiểu AWS Lambda - Serverless Compute.",
        "explanation": "AWS Lambda là serverless compute service cho phép bạn chạy code mà không cần provision hoặc manage servers. Features: Pay per invocation (never pay for idle), Auto scaling (automatic from 0 to thousands), Multiple runtimes (Node.js, Python, Java, Go, Ruby, .NET, custom), Execution time limit (15 minutes max). Components: Function (your code), Runtime (execution environment), Event source (trigger). Deployment: Upload zip/container image, Max deployment size 50MB (zipped), 250MB (uncompressed). IAM role (execution role) cần được configure đúng permissions."
    },
    "Lambda Triggers": {
        "summary": "Các cách trigger Lambda functions.",
        "explanation": "Lambda có thể được trigger bởi nhiều AWS services. Event-driven triggers: S3 (object created/deleted), DynamoDB Streams, Kinesis, SNS (notifications), SQS (queue messages). API triggers: API Gateway (REST/HTTP APIs), ALB (Application Load Balancer), CloudFront (Lambda@Edge). Schedule: EventBridge (CloudWatch Events) for cron-like triggers. Code changes: CodeCommit, S3. Direct invocation: AWS SDK, CLI. Concurrency: Synchronous (caller waits for response), Asynchronous (Lambda queues và retries), Stream-based (poll stream và process batches)."
    },
    "Lambda Layers": {
        "summary": "Sử dụng Lambda Layers để quản lý dependencies.",
        "explanation": "Lambda Layers cho phép bạn share code và dependencies across multiple functions. Benefits: Reduce deployment package size, Centralize common code, Easier to update shared libraries. Create layer: Package dependencies (nodejs/node_modules hoặc python/lib/python3.8/site-packages), Create zip, Upload via Console hoặc CLI. Usage: Add up to 5 layers per function, Specify runtime-compatible layers. AWS managed layers: AWS SDK layer (auto-updated), Runtime interface emulators. Use cases: Common utilities, ML libraries (numpy, pandas), Custom runtimes."
    },
    "Lambda Versions Aliases": {
        "summary": "Quản lý Lambda versions và aliases.",
        "explanation": "Lambda versions và aliases giúp bạn quản lý deployments và rollbacks. Versions: $LATEST (editable code), numbered versions (immutable, có ARN riêng). Aliases: Pointers to specific versions (VD: prod → v3, dev → $LATEST). Use cases: Blue-green deployments, Gradual rollouts, Easy rollback. Provisioned Concurrency: Pre-warm functions for consistent latency. Environment-specific configuration: Dùng environment variables để distinguish between dev/staging/prod."
    },
    # API Gateway Lessons
    "API Gateway": {
        "summary": "Tìm hiểu Amazon API Gateway.",
        "explanation": "Amazon API Gateway là service để create, deploy, và manage APIs. Types: REST API (full features, AWS proxy integrations), HTTP API (lightweight, HTTP proxy và AWS ALB integration), WebSocket API (bidirectional communication). Features: TLS/SSL termination, DDoS protection, throttling (rate limit, burst), Caching, Authorizers (IAM, Cognito, Lambda), API keys. Integrations: Lambda functions, HTTP backends, AWS services. Deployment: APIs cần deployed đến stages (dev, prod) để become callable."
    },
    "API Gateway Integration": {
        "summary": "Tích hợp API Gateway với Lambda và các backend.",
        "explanation": "API Gateway integration kết nối API methods đến backend. Lambda integration: AWS_PROXY (Lambda handles everything), AWS (custom request/response mapping). HTTP integration: HTTP proxy (pass-through), HTTP custom (mapping). Mock integration: Return fixed responses (for testing). Request/Response transformations: Mapping templates để modify headers, query strings, body. Velocity Template Language (VTL) hoặc JSON transforms. Integration timeout: 29 seconds max. Error handling: Gateway responses, Lambda error handling."
    },
    "API Gateway Auth": {
        "summary": "Authentication và Authorization trong API Gateway.",
        "explanation": "API Gateway cung cấp nhiều authentication options. IAM auth: Use AWS Signature Version 4, Attach IAM policy to IAM role, Users sign requests with access keys. Cognito auth: User pools (JWT tokens), Identity pools (temporary AWS credentials). Lambda authorizer: Custom logic in Lambda function, Token-based (JWT) hoặc Request-based (headers). API Keys: Simple API key authentication, Rate limiting per key. Usage plans: Throttle và quota per customer. Best practice: Always authenticate APIs, không để public."
    },
    # Cognito Lessons
    "Cognito": {
        "summary": "Tìm hiểu Amazon Cognito - User Authentication.",
        "explanation": "Amazon Cognito cung cấp authentication, authorization, và user management cho apps. User Pools: Sign-up/sign-in, Managed user directory, Social sign-in (Google, Facebook, Apple), SAML/OWIN, Custom attributes, MFA support. Identity Pools (Federated Identities): Temporary AWS credentials, Access AWS services, Unauthenticated (guest) access. Token flow: ID token (user info), Access token (API permissions), Refresh token. Hosted UI: Ready-made sign-in pages, Customizable styling. Pricing: MAU (Monthly Active Users) based."
    },
    # ECS Lessons
    "ECS": {
        "summary": "Tìm hiểu Amazon ECS - Container Orchestration.",
        "explanation": "Amazon ECS là container orchestration service để run containerized applications. Launch types: EC2 (bạn quản lý EC2 instances), Fargate (serverless, AWS manage compute). Components: Cluster (logical grouping of container instances), Task Definition (blueprint for containers), Task (running containers from task definition), Service (maintain desired count). Task Definition: Image, Port mappings, Environment variables, CPU/Memory, Log configuration. Load balancing: Register containers with ALB/NLB. IAM roles: Task execution role, Task role."
    },
    # CloudWatch Lessons
    "CloudWatch": {
        "summary": "Tìm hiểu Amazon CloudWatch - Monitoring.",
        "explanation": "Amazon CloudWatch là monitoring và observability service. Metrics: System/app metrics, Custom metrics (put-metric-data), Resolution (standard 1min, high 1sec). Logs: Centralized logging, Log groups/streams, Insights (query language), Subscriptions (real-time processing). Alarms: Thresholds trigger actions, States (OK, ALARM, INSUFFICIENT), Actions (SNS, Auto Scaling, EC2). Dashboards: Custom visualizations, Multiple metrics, Widgets (graphs, numbers, text). Events: Schedule (cron), Event patterns (AWS resource changes). Embedded metric format: For high-cardinality data."
    },
    "CloudWatch Logs": {
        "summary": "Sử dụng CloudWatch Logs cho centralized logging.",
        "explanation": "CloudWatch Logs centralize logs từ various sources. Log groups: Logical grouping of log streams, Retention settings, Encryption. Log streams: Instances/applications. Sources: EC2 (CloudWatch Agent), Lambda (automatic), ECS, On-premises (SSM Agent). Insights: Query language cho logs, Join across log groups, Visualizations. Filters: Pattern matching, Trigger alarms. Subscriptions: Real-time delivery to Lambda/Kinesis/Firehose. Cost: GB stored, data transfer. Best practice: Set retention periods, Use structured logging (JSON)."
    },
    "CloudWatch Alarm": {
        "summary": "Tạo CloudWatch Alarms để monitor metrics.",
        "explanation": "CloudWatch Alarms theo dõi metrics và trigger actions khi thresholds exceeded. Create alarm: Select metric, Define condition, Set evaluation periods. Statistic: Average, Sum, Maximum, Minimum, SampleCount. Period: Time window for metric data (1 minute to 1 day). Evaluation: Number of periods to evaluate, periods breaching. Actions: SNS notifications, Auto Scaling policies, EC2 actions. States: OK (below threshold), ALARM (above threshold), INSUFFICIENT (not enough data). Composite alarms: Combine multiple alarms with AND/OR."
    },
    # SNS Lessons
    "SNS": {
        "summary": "Tìm hiểu Amazon SNS - Simple Notification Service.",
        "explanation": "Amazon SNS là pub/sub messaging service và mobile notifications. Components: Topics (channel for messages), Subscriptions (endpoints that receive messages), Publishers (send messages to topics). Protocols: HTTP/HTTPS (webhooks), Email, Email-JSON, SMS, Lambda, SQS, Mobile push (APNs, FCM). Features: Message filtering (filter policies), Message durability (stored redundantly), Fanout (one message to many destinations), FIFO (ordering). Use cases: Application alerts, Push notifications, Email notifications, Trigger Lambda functions. Pricing: $0.50 per 1M notifications."
    },
    # SES Lessons
    "SES": {
        "summary": "Tìm hiểu Amazon SES - Simple Email Service.",
        "explanation": "Amazon SES là email service cho sending/receiving emails. Sending: SMTP interface hoặc SDK, Bulk sending, Templates. Receiving: Rules to process incoming emails, Store in S3, Trigger Lambda. Features: DKIM/DMARC support, Dedicated IPs (for high volume), Sandboxed by default (need production access). Use cases: Transactional emails, Marketing campaigns, Email verification. Configuration: Domain verification, Email addresses verification. Pricing: $0.10 per 1,000 emails."
    },
    # VPN Lessons
    "Site to Site VPN": {
        "summary": "Tìm hiểu Site-to-Site VPN kết nối on-premises với AWS.",
        "explanation": "Site-to-Site VPN kết nối your on-premises network đến VPC over Internet. Components: Virtual Private Gateway (VGW) attached to VPC, Customer Gateway (CGW) - your on-premises device, VPN Connection. How it works: Encrypted tunnel over Internet, Static or dynamic (BGP) routing. Types: AWS VPN (managed service), DX with VPN (over Direct Connect). Performance: 1.25 Gbps per tunnel, Can create multiple tunnels. Use cases: Extend on-premises to cloud, Hybrid architectures."
    },
    # Egress Only IGW
    "Egress Only Internet Gateway": {
        "summary": "Sử dụng Egress Only Internet Gateway cho IPv6.",
        "explanation": "Egress Only Internet Gateway cho phép instances with IPv6 addresses truy cập Internet while preventing Internet-initiated connections. Stateful - return traffic automatically allowed. Create: aws ec2 create-egress-only-internet-gateway. Attach to VPC. Route Table: Add route ::/0 → egress-only-IGW. Use cases: IPv6-only instances need outbound Internet, NAT64/DNS64 for IPv4 communication. Note: Chỉ works với IPv6, không support IPv4."
    },
    # Hybrid DNS
    "Hybrid DNS": {
        "summary": "Cấu hình Hybrid DNS cho on-premises và AWS.",
        "explanation": "Hybrid DNS cho phép resolution giữa on-premises DNS và Route 53. Inbound Endpoints: Route 53 receives queries từ on-premises. Outbound Endpoints: Forward queries đến on-premises DNS. Resolver rules: Route queries based on domain. Architecture: On-premises → Inbound Endpoint → Route 53 Resolver → VPC. Use cases: Hybrid applications, Migration scenarios, Split-horizon DNS. Endpoints: VPCs, Direct Connect, VPN."
    },
    # Lambda Destinations
    "Lambda Destinations": {
        "summary": "Sử dụng Lambda Destinations cho async invocations.",
        "explanation": "Lambda Destinations cho phép bạn route results từ async invocations đến other services. On success: Lambda sends response to SQS, SNS, Lambda, EventBridge. On failure: Separate destination for failed invocations. Benefits: Decouple microservices, Asynchronous processing pipelines, Better error handling. Use cases: Event-driven workflows, Audit trails, Dead letter queues. Configuration: Destinations tab in function, Separate config for success/failure."
    },
    # Reserved Concurrency
    "Reserved Concurrency": {
        "summary": "Quản lý Lambda Concurrency - Reserved và Provisioned.",
        "explanation": "Lambda Concurrency control số functions có thể run đồng thời. Reserved Concurrency: Guarantee maximum concurrent executions, Prevents function from using others' concurrency. Provisioned Concurrency: Pre-warmed instances, Consistent latency (no cold starts). Settings: Reserve 10 for critical function, Provision 100 for latency-sensitive. Pricing: Reserved free, Provisioned charged. Auto Scaling: Configure provisioned concurrency with target tracking. Use cases: Critical functions, Predictable workloads, Latency-critical APIs."
    }
}

import re

count = 0
for keyword, data in detailed_content.items():
    # Find lessons containing this keyword
    pattern = rf'summary: "([^"]*{re.escape(keyword)}[^"]*)"'
    
    # For explanation - find and replace short explanations
    for match in re.finditer(rf'{re.escape(keyword)}', content):
        # Find the explanation block near this match
        pass

# Simpler approach - update based on specific patterns
updates = {
    "Serverless computing voi Lambda.": {
        "summary": "Tim hieu AWS Lambda - Serverless Compute.",
        "explanation": "AWS Lambda la serverless compute service cho phep chay code ma khong can servers. Features: Pay per invocation (never pay for idle), Auto scaling, Multiple runtimes (Node.js, Python, Java, Go, Ruby, .NET). Lambda cho phep upload code, chon runtime, va set memory/timeout. Execution time limit: 15 minutes. IAM execution role can be configured. Concurrency: 1000 default, can request increase. Layers: Share dependencies across functions."
    },
    "Tao APIs voi API Gateway.": {
        "summary": "Tim hieu Amazon API Gateway - Tao va quan ly APIs.",
        "explanation": "Amazon API Gateway la service de create, deploy, va manage APIs. Types: REST API (full features), HTTP API (lightweight), WebSocket API. Features: TLS/SSL termination, DDoS protection, throttling, Caching, Authorizers, API keys. Integrations: Lambda functions, HTTP backends. Deployment: APIs can be deployed to stages (dev, prod). CORS: Cross-origin resource sharing can be configured. Custom domain: Map your domain to API Gateway endpoints."
    },
    "Su dung DynamoDB NoSQL database.": {
        "summary": "Tim hieu Amazon DynamoDB - Serverless NoSQL Database.",
        "explanation": "Amazon DynamoDB la fully managed NoSQL database voi single-digit millisecond latency. Tables, Items, Attributes. Primary Key: Partition Key (required) + Sort Key (optional). Capacity modes: Provisioned va On-demand. Features: TTL, Streams, Global Tables, DAX (in-memory cache). Query: Tim items theo Partition Key, efficient. Scan: Doc toan bo table, tranh su dung trong production. Partitioning: Auto-scales based on data size va provisioned throughput."
    },
    "Tim hieu Auto Scaling trong AWS.": {
        "summary": "Tim hieu Auto Scaling - Tu dong dieu chinh so luong instances.",
        "explanation": "Auto Scaling tu dong dieu chinh so luong EC2 instances theo demand. Components: Launch Template (AMI, type, SG, user data), Auto Scaling Group (min/max/desired), Scaling Policies. Policies: Target tracking (keep CPU at 50%), Step scaling, Simple scaling. Metrics: CPUUtilization, Network, Custom CloudWatch. Cooldown: Thoi gian cho sau scaling action de tranh oscillation. Lifecycle hooks: Actions at scale-out/scale-in events. Health checks: ELB or EC2."
    },
    "Su dung IAM Roles.": {
        "summary": "Tim hieu IAM Roles - Quyen tam thoi cho services va users.",
        "explanation": "IAM Roles cung cap quyen tam thoi ma khong can access keys. Use cases: EC2 accessing S3, Lambda accessing DynamoDB, Cross-account access. Instance profiles: Container for role to attach to EC2. Trust policy: Defines who can assume the role. Permissions policy: What the role can do. Best practices: Use roles thay vi access keys, Grant least privilege, Regular audit. STS (Security Token Service): Assume role de lay temporary credentials."
    },
    "Tim hieu bai hoc nay tren AWS.": {
        "summary": "Tim hieu bai hoc AWS nay.",
        "explanation": "Day la bai hoc ve AWS service. Xem video de hieu chi tiet ve concepts, practical applications, va best practices. Cac bai hoc AWS giup ban hieu ve cloud computing va cac dich vu cua Amazon Web Services. Practice: Thuc hanh trong AWS Console, thu nghiem voi free tier, va building projects de cuong co kien thuc."
    },
    "Site-to-Site VPN ket noi on-prem voi AWS.": {
        "summary": "Tim hieu Site-to-Site VPN - Ket noi on-premises voi AWS.",
        "explanation": "Site-to-Site VPN ket noi your on-premises network den VPC over Internet. Components: Virtual Private Gateway (VGW), Customer Gateway (CGW), VPN Connection. How it works: Encrypted tunnel over Internet, Static hoac dynamic (BGP) routing. Performance: 1.25 Gbps per tunnel, Multiple tunnels supported. Use cases: Hybrid architectures, Extend on-premises to cloud. AWS VPN: Managed service, easy to setup."
    },
    "Egress Only Internet Gateway cho IPv6.": {
        "summary": "Su dung Egress Only Internet Gateway cho IPv6.",
        "explanation": "Egress Only Internet Gateway cho phep instances voi IPv6 addresses truy cap Internet outbound ma ngan chan Internet-initiated connections. Stateful: Return traffic tu dong allowed. Create: aws ec2 create-egress-only-internet-gateway. Route Table: Add route ::/0 den Egress Only IGW. Use cases: IPv6-only instances can access Internet. Note: Chi hoat dong voi IPv6, khong support IPv4."
    },
    "Hybrid DNS cau hinh on-prem va AWS.": {
        "summary": "Cau hinh Hybrid DNS - DNS Resolution giua on-premises va AWS.",
        "explanation": "Hybrid DNS cho phep DNS resolution giua on-premises va Route 53. Components: Inbound Endpoints (Route 53 receives queries), Outbound Endpoints (forward queries to on-premises), Resolver rules. Architecture: On-premises DNS <-> Inbound Endpoint <-> Route 53 Resolver <-> VPC. Use cases: Hybrid applications, Migration scenarios, Split-horizon DNS. Rules: Route queries based on domain names."
    },
    "Lambda reserved va provisioned concurrency.": {
        "summary": "Quan ly Lambda Concurrency - Reserved va Provisioned.",
        "explanation": "Lambda Concurrency controls so luong functions co the run dong thoi. Reserved Concurrency: Guarantee maximum, Prevents function from using others. Provisioned Concurrency: Pre-warmed instances, Consistent latency, No cold starts. Use cases: Critical functions need guaranteed capacity, Predictable workloads, Latency-sensitive APIs. Auto Scaling: Configure provisioned concurrency with target tracking. Pricing: Reserved free, Provisioned charged per minute."
    },
    "SNS notification service.": {
        "summary": "Tim hieu Amazon SNS - Simple Notification Service.",
        "explanation": "Amazon SNS la pub/sub messaging va mobile notification service. Components: Topics (channel), Subscriptions (endpoints), Publishers. Protocols: HTTP/HTTPS, Email, SMS, Lambda, SQS, Mobile push. Features: Message filtering, Message durability, Fanout, FIFO ordering. Use cases: Application alerts, Push notifications, Trigger Lambda functions. Pricing: $0.50 per 1M notifications. Best practice: Use topics for fanout patterns."
    },
    "CloudWatch monitoring va logging.": {
        "summary": "Tim hieu CloudWatch - Monitoring va Observability.",
        "explanation": "Amazon CloudWatch la monitoring va observability service. Metrics: System/app metrics, Custom metrics, Resolution. Logs: Centralized logging, Log groups/streams, Insights query. Alarms: Monitor metrics, Trigger actions when thresholds exceeded. Dashboards: Custom visualizations, Multiple metrics. Events: Schedule, Event patterns. Embedded metric format: High-cardinality data. Pricing: Basic monitoring free, detailed/advanced charged."
    },
    "Lambda Destinations.": {
        "summary": "Su dung Lambda Destinations cho async invocations.",
        "explanation": "Lambda Destinations route results tu async invocations den other services. On success: Send to SQS, SNS, Lambda, EventBridge. On failure: Separate destination for failed invocations. Benefits: Decouple microservices, Asynchronous processing, Better error handling. Use cases: Event-driven workflows, Audit trails, Dead letter queues. Configuration: Destinations tab in function console."
    },
    "VPC Endpoints de truy cap AWS services.": {
        "summary": "Su dung VPC Endpoints - Private access to AWS services.",
        "explanation": "VPC Endpoints cho phep connect to AWS services ma khong can Internet gateway, NAT device, hoac VPN. Gateway Endpoints: S3, DynamoDB. Interface Endpoints: Other AWS services (private link). Benefits: More secure, Lower latency, No charges for gateway endpoints. Create: VPC > Endpoints > Create Endpoint. Routing: Traffic automatically routed through VPC endpoint."
    }
}

count = 0
for old_exp, new_data in updates.items():
    if old_exp in content:
        # Find the lesson with this explanation
        # We need to find the lesson title and update both summary and explanation
        parts = content.split(old_exp)
        if len(parts) >= 2:
            # Find the summary before this explanation
            idx = parts[0].rfind('summary: "')
            if idx >= 0:
                old_summary_start = parts[0][idx:]
                old_summary_end = old_summary_start.find('"') + 1
                old_summary = old_summary_start[:old_summary_end]
                new_summary = f'summary: "{new_data["summary"]}"'
                
                content = content.replace(old_summary, new_summary, 1)
                content = content.replace(old_exp, new_data["explanation"], 1)
                count += 1
                print(f"Updated: {new_data['summary'][:40]}...")

with open('data.js', 'w') as f:
    f.write(content)

print(f"\nTotal updated: {count} lessons")
