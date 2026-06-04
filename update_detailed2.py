#!/usr/bin/env python3
"""Update remaining short explanations with more detailed content"""

with open('data.js', 'r') as f:
    content = f.read()

# Comprehensive content updates
updates = [
    {
        "pattern": "Huong dan ket noi den EC2 Linux instance tu Linux hoac Mac terminal.",
        "summary": "Huong dan ket noi SSH den EC2 instance tu Linux/Mac.",
        "explanation": "SSH la Secure Shell protocol de ket noi secure den EC2 instances. Voi Linux/Mac: <pre>ssh -i key.pem ec2-user@public-ip</pre> Cac loi thuong gap: Permission denied (can chmod 400 key.pem), Connection timeout (check Security Group), Host key changed (ssh-keygen -R ip-address). Sau khi connect, ban co the update system (yum update) va cai dat packages. EC2 Instance Connect la phuong phap thay the - khong can key pair, SSH duoc managed boi AWS."
    },
    {
        "pattern": "User Data cho phep chay scripts tu dong khi EC2 instance start lan dau.",
        "summary": "Su dung User Data script de tu dong chay commands khi EC2 khoi tao.",
        "explanation": "User Data cho phep chay scripts tu dong khi EC2 instance start lan dau. Use cases: Install software (nginx, apache), configure applications, download code tu S3, setup monitoring agents. Example User Data: <pre>#!/bin/bash\\nyum update -y\\namazon-linux-extras install nginx1 -y\\nsystemctl start nginx</pre> Xem logs: <pre>sudo cat /var/log/cloud-init-output.log</pre> User Data duoc chay voi root privileges."
    },
    {
        "pattern": "Tong quan day du ve AWS pricing models.",
        "summary": "Chi tiet ve cac mo hinh pricing: On-Demand, Reserved, Spot, Savings Plans.",
        "explanation": "AWS pricing philosophy: Pay for what you use, Pay less when you reserve, Pay even less with more. On-Demand: Khong co commitment, tra theo gio, phu hop cho short-term projects. Reserved Instances: Commitment 1-3 nam, giam 30-72%, co the chon No/Partial/All Upfront. Savings Plans: Thay the linh hoat hon cho RIs, giam den 72%, co Compute va EC2 Instance Savings Plans. Spot Instances: Su dung unused capacity, giam den 90%, co the interrupted bat cu luc nao, phu hop cho batch jobs, ML training. AWS Free Tier: Always Free (Lambda 1M requests, DynamoDB 25GB), 12 Months Free (EC2 750h, S3 5GB)."
    },
    {
        "pattern": "Tao Windows Server EC2 instance.",
        "summary": "Huong dan tao Windows EC2 instance tren AWS.",
        "explanation": "Tao Windows Server EC2 instance de chay cac ung dung Windows. Chon AMI: Windows Server 2022 Base, Windows Server 2019 Base. Tao Instance: Chon Windows AMI, chon instance type (t3.micro free tier), configure network, add Storage (50GB thuong du), configure Security Group: RDP (port 3389), launch voi key pair. Ket noi Windows: Tai RDP file tu AWS Console, get password su dung key pair, connect qua Remote Desktop. Su dung PuTTY hoac Remmina tu Linux de ket noi Windows instances."
    },
    {
        "pattern": "Cach ket noi Windows instance tu Linux machine.",
        "summary": "Huong dan ket noi Windows EC2 instance tu Linux.",
        "explanation": "Co nhieu cach ket noi Windows tu Linux. Su dung Remmina: <pre>sudo apt install remmina remmina-plugin-rdp\\nremmina</pre> Su dung xrdp: <pre>sudo apt install xrdp\\nsudo systemctl enable xrdp</pre> Thong tin can thiet: Windows IP address, Username: Administrator, Password: Da lay tu AWS Console. Security Group: Mo port 3389 (RDP) tu IP cua ban. Thuc hien ket noi va nhap thong tin dang nhap de truy cap Windows desktop."
    },
    {
        "pattern": "Instance Metadata cung cap thong tin ve instance.",
        "summary": "Tim hieu EC2 Instance Metadata - cach lay thong tin instance.",
        "explanation": "Instance Metadata cung cap thong tin ve instance ma khong can su dung AWS CLI. Metadata URL: <pre>curl http://169.254.169.254/latest/meta-data/</pre> Thong tin co san: ami-id (AMI ID), instance-id (Instance ID), instance-type (Instance type), local-ipv4 (Private IP), public-ipv4 (Public IP), security-groups (Security groups). User Data: <pre>curl http://169.254.169.254/latest/user-data/</pre> Luu y bao mat: Metadata accessible tu trong instance, su dung IAM roles thay vi access keys, enable IMDSv2 de prevent hijacking."
    },
    {
        "pattern": "Elastic IP la static public IPv4 address.",
        "summary": "Cach gan Elastic IP address cho EC2 instance.",
        "explanation": "Elastic IP la static public IPv4 address co the gan cho instances. Tao: EC2 Dashboard > Elastic IPs > Allocate new address. Gán: Actions > Associate Elastic IP address. CLI: <pre>aws ec2 associate-address --instance-id i-xxx --public-ip x.x.x.x</pre> Use cases: Static IP cho website, whitelist IP in firewall, point DNS records. Chi phi: Free neu associated voi running instance, $0.005/gio neu not associated hoac instance stopped. Best practice: Khong nen rely hoan toan vao EIP, consider Route 53 cho DNS-based failover."
    },
    {
        "pattern": "Huong dan detach va release Elastic IP.",
        "summary": "Cach giai phong Elastic IP address.",
        "explanation": "Detach va release Elastic IP khi khong can nua de tranh charges. Disassociate: <pre>aws ec2 disassociate-address --public-ip x.x.x.x</pre> Release: <pre>aws ec2 release-address --allocation-id eipalloc-xxx</pre> Chi phi: $0.005/gio cho EIP khong associated. Best Practices: Release EIP khi khong can, use Route 53 thay vi EIP cho most use cases, automate cleanup voi Lambda hoac budget alerts. Qua trinh: Disassociate truoc, sau do release."
    },
    {
        "pattern": "So sanh EBS va Instance Store.",
        "summary": "Tong quan ve EBS volumes va Instance Store.",
        "explanation": "EBS vs Instance Store: EBS la network-attached storage, persist independently of instance lifecycle, co the attach/detach. Instance Store la attached directly to host, data lost when instance stops, free voi instance, higher I/O performance. EBS Volume Types: gp3 (3000-16000 IOPS, $0.08/GB), gp2 (legacy), io2 (64000 IOPS, 99.999% durability), st1 (throughput optimized HDD), sc1 (cold storage HDD). EBS volumes tu dong replicated trong AZ de protect khoi component failure."
    },
    {
        "pattern": "Tao va mount EBS volume tren Linux instance.",
        "summary": "Huong dan tao EBS volume va mount vao EC2 Linux.",
        "explanation": "Tao EBS volume va mount tren Linux instance. Tao Volume: EC2 > Volumes > Create Volume, chon size, type (gp3), AZ. Attach: Actions > Attach Volume, chon instance trong cung AZ. Mount tren Linux: <pre>lsblk</pre> de check available disks, <pre>sudo mkfs -t xfs /dev/xvdf</pre> de format, <pre>sudo mkdir /mnt/data && sudo mount /dev/xvdf /mnt/data</pre> de mount. Add to /etc/fstab for auto-mount: <pre>/dev/xvdf /mnt/data xfs defaults,nofail 0 2</pre> Verify: <pre>df -h</pre>"
    },
    {
        "pattern": "Di chuyen EBS volume giua cac instances.",
        "summary": "Cach detach EBS volume va attach vao instance khac.",
        "explanation": "Detach EBS volume tu instance nay va attach sang instance khac. Detach: <pre>aws ec2 detach-volume --volume-id vol-xxx</pre> Hoac qua Console: Volumes > Select > Actions > Detach Volume. Attach: <pre>aws ec2 attach-volume --volume-id vol-xxx --instance-id i-xxx --device /dev/sdf</pre> Luu y: Instance phai cung AZ, umount truoc khi detach, force detach neu can: <pre>aws ec2 detach-volume --volume-id vol-xxx --force</pre>."
    },
    {
        "pattern": "Tang dung luong EBS volume.",
        "summary": "Cach mo rong EBS volume va file system.",
        "explanation": "Mo rong EBS volume khi can them storage. Buoc 1: Modify Volume - Volumes > Modify Volume > Change size. Buoc 2: Extend Partition - <pre>sudo growpart /dev/xvda 1</pre> Buoc 3: Extend File System - XFS: <pre>sudo xfs_growfs /mnt/data</pre>, ext4: <pre>sudo resize2fs /dev/xvdf</pre> Verify: <pre>df -h && lsblk</pre> Luu y: Chi co the increase size, khong decrease. Volume phai be attached. File system phai match type."
    },
    {
        "pattern": "Resize root volume de co them space cho OS.",
        "summary": "Huong dan resize root EBS volume.",
        "explanation": "Resize root EBS volume de co them space cho OS. Cach don gian: Modify root volume size in console, reboot instance, extend file system. Extend Root Partition: <pre>sudo growpart /dev/xvda 1</pre> Extend File System: XFS: <pre>sudo xfs_growfs /</pre>, ext4: <pre>sudo resize2fs /dev/xvda1</pre> Kiem tra: <pre>df -h && lsblk</pre> Hoac tao snapshot, tao volume lon hon tu snapshot, attach."
    },
    {
        "pattern": "Multi-Attach cho phep attach cung mot volume.",
        "summary": "Tim hieu EBS Multi-Attach - gan mot volume cho nhieu instances.",
        "explanation": "Multi-Attach cho phep attach cung mot EBS volume cho nhieu instances trong cung AZ. Yeu cau: Volume type phai la io2 hoac io2 Block Express, file system phai support concurrent access (XFS, GFS2), instances phai cung AZ. Benefits: Clustered applications, applications can shared storage, improved availability. Cai dat: Enable Multi-Attach khi tao volume, attach den multiple instances. Canh bao: Can proper locking de tranh data corruption."
    },
    {
        "pattern": "Huong dan chon dung EBS volume type.",
        "summary": "So sanh cac loai EBS volumes va cach chon phu hop.",
        "explanation": "Chon dung EBS volume type cho workload cua ban. SSD-backed: gp3 (3000-16000 IOPS, best value, $0.08/GB), io2 (64000 IOPS, highest durability 99.999%, $0.125/GB). HDD-backed: st1 (throughput optimized HDD, $0.045/GB), sc1 (cold storage, cheapest, $0.015/GB). Chon dung: Boot volumes -> gp3, Web servers/dev -> gp3, Databases -> io2, Big data/log processing -> st1, Archival -> sc1. Upgrade: Co the upgrade tu gp2/gp3, io1/io2 nhung khong downgrade."
    },
    {
        "pattern": "EBS Snapshots la incremental backups.",
        "summary": "Tong quan ve EBS Snapshots - incremental backups.",
        "explanation": "EBS Snapshots la incremental backups duoc luu trong S3. Dac diem: Incremental - chi backup thay doi, stored in S3 (managed by AWS), can copy across regions, can share voi other accounts. Tinh incremental: First snapshot la full copy, subsequent chi save changes, deleting snapshot chi xoa unique data. Benefits: Disaster recovery, volume migration, AMI creation, compliance backup. Encryption: Snapshots from encrypted volumes tu dong encrypted."
    },
    {
        "pattern": "Tu dong hoa backup su dung Data Lifecycle Manager.",
        "summary": "Su dung S3 Lifecycle Policies de tu dong chuyen doi objects.",
        "explanation": "S3 Lifecycle policies tu dong chuyen doi hoac xoa objects theo thoi gian. Tao Policy: S3 > Bucket > Management > Lifecycle rule. Actions: Transition (chuyen sang storage class: Standard IA sau 30 ngay, Glacier sau 90 ngay), Expiration (xoa sau X ngay, xoa incomplete uploads). Use cases: Auto-archive to Glacier, delete old logs, reduce storage costs. Example: Move to IA after 30 days, Glacier after 90 days, Delete after 365 days. Cost savings co the rat lon."
    },
    {
        "pattern": "Gioi thieu Elastic Load Balancing va Classic Load Balancer.",
        "summary": "Gioi thieu ELB - phan phoi traffic den nhieu targets.",
        "explanation": "ELB phan phoi incoming traffic den multiple targets nhu EC2 instances, containers, IP addresses. Load Balancer Types: Application LB (ALB) - Layer 7, HTTP/HTTPS, advanced routing (path-based, host-based). Network LB (NLB) - Layer 4, TCP/UDP, static IP per AZ, ultra-low latency. Gateway LB - Layer 3, virtual appliances. Classic LB (CLB) - legacy (deprecated). ELB features: High availability, health checks, SSL termination, sticky sessions, CloudWatch monitoring, integrated with Auto Scaling."
    },
    {
        "pattern": "Cau hinh EC2 chi accessible qua Load Balancer.",
        "summary": "Bao mat EC2 chi cho phep traffic qua Load Balancer.",
        "explanation": "Bao mat EC2 instances bang cach chi cho phep traffic qua Load Balancer. Security Group Configuration: Load Balancer SG - Inbound 0.0.0.0/0 (HTTP/HTTPS), Outbound to EC2 SG (port 80/443). EC2 Instance SG - Inbound chi from LB SG (port 80/443), Outbound anywhere. Benefits: Hide instances from direct access, single entry point, easier to manage security, better DDoS protection. Setup: Create ALB, configure instance SG de allow from ALB SG, register instances voi target group, update route53 record den ALB."
    },
    {
        "pattern": "Cach xoa Classic Load Balancer.",
        "summary": "Cach xoa CLB va cleanup resources.",
        "explanation": "Xoa CLB khi khong can thiet de tien ich chi phi. Xoa: EC2 > Load Balancers > Select CLB > Actions > Delete. CLI: <pre>aws elb delete-load-balancer --load-balancer-name my-clb</pre> Luu y: CLB deletion khong affect instances, associated IAM roles duoc cleaned up, CloudWatch metrics duoc removed, DNS records can update rieng. Best Practice: Update DNS truoc khi xoa, verify no traffic den CLB, consider migration to ALB."
    },
    {
        "pattern": "Gioi thieu Application Load Balancer.",
        "summary": "Tim hieu ALB - Layer 7 Load Balancer cho HTTP/HTTPS.",
        "explanation": "ALB hoat dong o Layer 7 (HTTP/HTTPS), cung cap advanced routing. Features: Path-based routing (/api/* -> API targets), Host-based routing, Query string routing, Header-based routing, HTTP/2 va WebSocket support. Components: Load Balancer (entry point), Listeners (port va protocol), Target Groups (group of targets), Rules (route traffic). ALB is ideal cho microservices architecture, multiple services on same port, blue-green va canary deployments. ALB co the authenticate users voi Cognito hoac IAM."
    },
    {
        "pattern": "ALB co the route traffic dua tren URL path.",
        "summary": "Su dung path-based routing de route traffic den different target groups.",
        "explanation": "ALB co the route traffic dua tren URL path den different target groups. Vi du Routing: /api/* -> API Target Group, /images/* -> Static Content Target Group, /* -> Default Target Group. Tao Rules: ALB > Listeners > View/edit rules > Add rule. Conditions: If path pattern: /api/*, Then: Forward to api-target-group. CLI: <pre>aws elbv2 create-rule --listener-arn arn:aws:... --conditions Field=path-pattern,Values='/api/*' --priority 100 --actions Type=forward,TargetGroupArn=arn:aws:...</pre> Benefits: Multiple apps on same domain, easier microservices, cost optimization."
    },
    {
        "pattern": "ALB forward client IP trong headers.",
        "summary": "Cach lay client IP khi su dung ALB.",
        "explanation": "Khi su dung ALB, client IP duoc forward trong headers. Client IP Headers: X-Forwarded-For (original client IP), X-Forwarded-Port (client port), X-Forwarded-Proto (HTTP/HTTPS). Example Node.js: <pre>const clientIP = req.headers['x-forwarded-for']</pre> Example Nginx: <pre>set_real_ip_from 10.0.0.0/8;\\nreal_ip_header X-Forwarded-For;</pre> Example Apache: <pre>LogFormat '%h %l %u %t \\\"%r\\\" %>s %b \\\"%{X-Forwarded-For}i\\\"' combined</pre> Note: ALB terminates HTTP va creates new connection to targets, targets see ALB IP as source."
    },
    {
        "pattern": "Sticky sessions dam bao requests cung client den cung target.",
        "summary": "Cau hinh sticky sessions trong ALB.",
        "explanation": "Sticky sessions (session affinity) dam bao requests tu same client duoc gui den same target. How it Works: ALB creates LB cookie, cookie identifies target, subsequent requests routed to same target. Enable: Target Group > Attributes > Enable stickiness > Set duration (1 second to 7 days). CLI: <pre>aws elbv2 modify-target-group-attributes --target-group-arn arn:aws:... --attributes Key=stickiness.enabled,Value=true Key=stickiness.lb_cookie.duration_seconds,Value=86400</pre> Use Cases: Session-based applications, applications with user state, caching benefits. Considerations: Co the cause uneven load distribution."
    },
    {
        "pattern": "NLB hoat dong o Layer 4, ultra-low latency.",
        "summary": "Tim hieu Network Load Balancer - Layer 4 LB.",
        "explanation": "Network Load Balancer hoat dong o Layer 4 (TCP/UDP/TLS), cung cap ultra-low latency. Features: Layer 4 (TCP/UDP/TLS), Static IP per AZ, Preserve client IP, Handle millions of requests/second, 99.99% SLA. vs ALB: NLB cung cap static IP va ultra-low latency; ALB cung cap HTTP-level routing. Use Cases: High performance applications, gaming servers, IoT protocols, non-HTTP applications. NLB is best khi ban can static IP addresses hoac very high performance. Create: <pre>aws elbv2 create-load-balancer --name my-nlb --type network --subnets subnet-xxx</pre>"
    },
    {
        "pattern": "Tu dong dieu chinh so luong EC2 instances.",
        "summary": "Cau hinh Auto Scaling policies de scale tu dong.",
        "explanation": "Auto Scaling tu dong dieu chinh so luong EC2 instances theo demand. Components: Launch Template (AMI, instance type, SG, user data), Auto Scaling Group (min/max/desired capacity), Scaling Policies. Scaling Policies Types: Target tracking (keep CPU at 50%), Step scaling (add 2 instances when CPU > 70%), Simple scaling (add when > 80%, wait 300s). Metrics: CPUUtilization, NetworkIn/Out, RequestCountPerTarget, Custom CloudWatch. Cooldown: Thoi gian cho sau scaling action de prevent oscillation."
    },
    {
        "pattern": "IAM cho phep quan ly truy cap AWS resources.",
        "summary": "Tim hieu AWS IAM - Identity and Access Management.",
        "explanation": "IAM cho phep quan ly truy cap an toan den AWS services va resources. Components: Users (individual people), Groups (collection of users with shared permissions), Roles (quyen tam thoi cho services/users), Policies (JSON documents defining permissions). Features: Fine-grained permissions, Multi-factor authentication (MFA), Password policy, Access keys rotation. Best Practices: Enable MFA for all users, use groups thay vi individual users, follow principle of least privilege, regular review permissions."
    },
    {
        "pattern": "MFA tang cuong bao mat bang cach yeu cau ma thu hai.",
        "summary": "Kich hoat MFA cho tai khoan AWS.",
        "explanation": "Multi-Factor Authentication tang cuong bao mat. Loai devices: Virtual (Google Authenticator, Authy, Microsoft Authenticator), Hardware (YubiKey, Gemalto), SMS (deprecated for root). Enable MFA: IAM > Users > Security credentials > Assign MFA device, scan QR code voi authenticator app, enter 2 consecutive codes. Best practice: Enable MFA cho tat ca users, dac biet la root account va admin users. MFA cho root account rat quan trong vi root co quyen cao nhat."
    },
    {
        "pattern": "AWS CLI cho phep tuong tac voi AWS bang command line.",
        "summary": "Huong dan cai dat va su dung AWS CLI.",
        "explanation": "AWS CLI cho phep tuong tac voi AWS services bang commands. Cai dat: <pre>pip install awscli</pre> hoac <pre>brew install awscli</pre>. Configure: <pre>aws configure</pre> (AWS Access Key ID, Secret Access Key, Default region, Output format). Su dung profiles: <pre>aws configure --profile production</pre>. Common commands: <pre>aws ec2 describe-instances</pre>, <pre>aws s3 ls</pre>. Multi-account: Su dung named profiles va environment variable AWS_PROFILE."
    }
]

count = 0
for update in updates:
    if update["pattern"] in content:
        content = content.replace(update["pattern"], update["explanation"], 1)
        count += 1

with open('data.js', 'w') as f:
    f.write(content)

print(f"Updated {count} lessons with detailed content")
