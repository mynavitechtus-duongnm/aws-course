#!/usr/bin/env python3
"""Update all remaining lessons with detailed content - simplified version"""

with open('data.js', 'r') as f:
    content = f.read()

# Simplified content - avoiding special characters
all_lessons = {
    # EC2 lessons
    "Access EC2 Instance From Linux Machine | EC2 Instance Connect": {
        "summary": "Huong dan ket noi SSH den EC2 instance tu Linux/Mac.",
        "explanation": "<p>Huong dan ket noi den EC2 Linux instance tu Linux hoac Mac terminal.</p><h4>SSH Connection</h4><pre>ssh -i key.pem ec2-user@public-ip</pre><h4>Key Permissions</h4><pre>chmod 400 key.pem</pre><h4>Common Issues</h4><ul><li>Permission denied: chmod 400 key.pem</li><li>Connection timeout: Check security group</li></ul>"
    },
    "Bootstrap Script in EC2 Instance | User Data In EC2": {
        "summary": "Su dung User Data script de tu dong chay commands khi EC2 khoi tao.",
        "explanation": "<p>User Data cho phep chay scripts tu dong khi EC2 instance start lan dau.</p><h4>Use Cases</h4><ul><li>Install software (nginx, apache)</li><li>Configure applications</li><li>Download code from S3</li></ul><h4>Example User Data</h4><pre>#!/bin/bash\nyum update -y\namazon-linux-extras install nginx1 -y\nsystemctl start nginx</pre>"
    },
    "AWS Pricing | Reserve Instance | Spot Instance | Saving Plan | Dedicated Host": {
        "summary": "Chi tiet ve cac mo hinh pricing: On-Demand, Reserved, Spot, Savings Plans.",
        "explanation": "<p>Tong quan day du ve AWS pricing models.</p><h4>1. On-Demand</h4><ul><li>Tra theo gio</li><li>Khong co commitment</li></ul><h4>2. Reserved Instances</h4><ul><li>Commitment 1-3 nam</li><li>Giam 30-72%</li></ul><h4>3. Savings Plans</h4><ul><li>Thay the linh hoat cho RIs</li><li>Giam den 72%</li></ul><h4>4. Spot Instances</h4><ul><li>Unused capacity</li><li>Giam den 90%</li><li>Co the interrupted</li></ul>"
    },
    "Create Windows Instance In AWS | AWS tutorials | AWS Step By Step": {
        "summary": "Huong dan tao Windows EC2 instance tren AWS.",
        "explanation": "<p>Tao Windows Server EC2 instance.</p><h4>Chon AMI</h4><ul><li>Windows Server 2022 Base</li><li>Windows Server 2019 Base</li></ul><h4>Tao Instance</h4><ol><li>Chon Windows AMI</li><li>Chon instance type</li><li>Configure Security Group: RDP (port 3389)</li><li>Launch voi key pair</li></ol><h4>Ket noi Windows</h4><ol><li>Download RDP file</li><li>Get password</li><li>Connect qua Remote Desktop</li></ol>"
    },
    "Access Windows Instance From Linux Machine | AWS tutorials | AWS Step By Step": {
        "summary": "Huong dan ket noi Windows EC2 instance tu Linux.",
        "explanation": "<p>Cach ket noi Windows instance tu Linux machine.</p><h4>Su dung Remmina</h4><pre>sudo apt install remmina remmina-plugin-rdp</pre><h4>Thong tin can thiet</h4><ul><li>Windows IP address</li><li>Username: Administrator</li><li>Password: Da lay tu AWS Console</li></ul>"
    },
    "Instance Metadata With UserData | AWS tutorials | AWS Step By Step": {
        "summary": "Tim hieu EC2 Instance Metadata - cach lay thong tin instance.",
        "explanation": "<p>Instance Metadata cung cap thong tin ve instance.</p><h4>Metadata URL</h4><pre>curl http://169.254.169.254/latest/meta-data/</pre><h4>Thong tin co san</h4><ul><li>ami-id: AMI ID</li><li>instance-id: Instance ID</li><li>instance-type: Instance type</li><li>public-ipv4: Public IP</li></ul><h4>User Data</h4><pre>curl http://169.254.169.254/latest/user-data/</pre>"
    },
    "Attach Elastic/Static IP to an EC2 Instance | AWS tutorials | AWS Step By Step": {
        "summary": "Cach gan Elastic IP address cho EC2 instance.",
        "explanation": "<p>Elastic IP la static public IPv4 address.</p><h4>Tao Elastic IP</h4><ol><li>EC2 Dashboard > Elastic IPs</li><li>Allocate new address</li><li>Associate voi instance</li></ol><h4>CLI</h4><pre>aws ec2 allocate-address\naws ec2 associate-address --instance-id i-xxx --public-ip x.x.x.x</pre><h4>Chi phi</h4><ul><li>Free neu associated</li><li>$0.005/gio neu khong su dung</li></ul>"
    },
    "Detach Elastic/Static IP | Release EIP | AWS tutorials | AWS Step By Step": {
        "summary": "Cach giai phong Elastic IP address.",
        "explanation": "<p>Huong dan detach va release Elastic IP.</p><h4>Disassociate</h4><pre>aws ec2 disassociate-address --public-ip x.x.x.x</pre><h4>Release</h4><pre>aws ec2 release-address --allocation-id eipalloc-xxx</pre><h4>Chi phi</h4><ul><li>$0.005/gio cho EIP khong associated</li><li>Release khi khong can</li></ul>"
    },
    "Elastic Block Storage (EBS) | Instance Store | AWS Step By Step": {
        "summary": "Tong quan ve EBS volumes va Instance Store.",
        "explanation": "<p>So sanh EBS va Instance Store.</p><h4>EBS Volumes</h4><ul><li>Network-attached storage</li><li>Independent of instance lifecycle</li><li>Persist after termination</li></ul><h4>Instance Store</h4><ul><li>Attached to host</li><li>Data lost when stopped</li><li>Higher I/O performance</li></ul><h4>Volume Types</h4><ul><li>gp3: General purpose SSD</li><li>io2: High performance SSD</li><li>st1: Throughput optimized HDD</li></ul>"
    },
    "Create First Elastic Block Storage Vol | Mount EBS in Linux | AWS Step By Step": {
        "summary": "Huong dan tao EBS volume va mount vao EC2 Linux.",
        "explanation": "<p>Tao va mount EBS volume tren Linux instance.</p><h4>Tao Volume</h4><ol><li>EC2 > Volumes > Create Volume</li><li>Chon size, type, AZ</li><li>Attach to instance</li></ol><h4>Mount tren Linux</h4><pre>lsblk\nsudo mkfs -t xfs /dev/xvdf\nsudo mkdir /mnt/data\nsudo mount /dev/xvdf /mnt/data</pre><h4>Auto-mount</h4><pre>/dev/xvdf /mnt/data xfs defaults,nofail 0 2</pre>"
    },
    "Detach an EBS volume from one EC2 Instance and Attach it Another One": {
        "summary": "Cach detach EBS volume va attach vao instance khac.",
        "explanation": "<p>Di chuyen EBS volume giua cac instances.</p><h4>Detach</h4><pre>aws ec2 detach-volume --volume-id vol-xxx</pre><h4>Attach</h4><pre>aws ec2 attach-volume --volume-id vol-xxx --instance-id i-xxx --device /dev/sdf</pre><h4>Luu y</h4><ul><li>Instance phai cung AZ</li><li>Umount truoc khi detach</li></ul>"
    },
    "Resize EBS Volume and Resize the File System": {
        "summary": "Cach mo rong EBS volume va file system.",
        "explanation": "<p>Tang dung luong EBS volume.</p><h4>Modify Volume</h4><ol><li>Volumes > Modify Volume</li><li>Change size</li></ol><h4>Extend</h4><pre>sudo growpart /dev/xvda 1\nsudo xfs_growfs /mnt/data</pre><h4>Verify</h4><pre>df -h</pre><h4>Luu y</h4><ul><li>Chi co the increase, khong decrease</li></ul>"
    },
    "How to Resize ROOT EBS Volume": {
        "summary": "Huong dan resize root EBS volume.",
        "explanation": "<p>Resize root volume de co them space cho OS.</p><h4>Cach don gian</h4><ol><li>Modify root volume size in console</li><li>Reboot instance</li><li>Extend file system</li></ol><h4>Extend</h4><pre>sudo growpart /dev/xvda 1\nsudo resize2fs /dev/xvda1</pre>"
    },
    "Attach One EBS Volume to Multiple EC2 Instance": {
        "summary": "Tim hieu EBS Multi-Attach - gan mot volume cho nhieu instances.",
        "explanation": "<p>Multi-Attach cho phep attach cung mot volume.</p><h4>Yeu cau</h4><ul><li>Volume type: io2</li><li>File system support concurrent access</li><li>Instances cung AZ</li></ul><h4>Use Cases</h4><ul><li>Clustered applications</li><li>Shared storage</li></ul>"
    },
    "Type of EBS Volumes - Which EBS Volume should I use ?": {
        "summary": "So sanh cac loai EBS volumes va cach chon phu hop.",
        "explanation": "<p>Huong dan chon dung EBS volume type.</p><h4>SSD-backed</h4><ul><li>gp3: 3000-16000 IOPS, Best value</li><li>io2: 64000 IOPS, highest durability</li></ul><h4>HDD-backed</h4><ul><li>st1: Throughput optimized</li><li>sc1: Cold storage, cheapest</li></ul><h4>Chon dung</h4><ul><li>Boot volumes: gp3</li><li>Databases: io2</li><li>Big data: st1</li></ul>"
    },
    "Snapshot Overview - AWS Snapshot - EBS Snapshot": {
        "summary": "Tong quan ve EBS Snapshots - incremental backups.",
        "explanation": "<p>EBS Snapshots la incremental backups.</p><h4>Dac diem</h4><ul><li>Incremental: Chi backup thay doi</li><li>Stored in S3</li><li>Can copy across regions</li></ul><h4>Benefits</h4><ul><li>Disaster recovery</li><li>Volume migration</li><li>AMI creation</li></ul>"
    },
    "Create First Snapshot - EBS Backup": {
        "summary": "Huong dan tao EBS snapshot de backup volume.",
        "explanation": "<p>Tao snapshot de backup EBS volume.</p><h4>Tao Snapshot</h4><pre>aws ec2 create-snapshot --volume-id vol-xxx --description Backup</pre><h4>Best Practices</h4><ul><li>Create snapshots regularly</li><li>Use lifecycle policies</li><li>Test restore</li></ul>"
    },
    "Automate EBS Volume Backup - EBS Lifecycle Manager - EBS Backup": {
        "summary": "Tu dong hoa backup su dung Data Lifecycle Manager.",
        "explanation": "<p>Su dung EBS Lifecycle Manager.</p><h4>Tao Policy</h4><ol><li>EC2 > Lifecycle Manager</li><li>Create lifecycle policy</li><li>Configure schedule va retention</li></ol><h4>Benefits</h4><ul><li>Automated backups</li><li>Automatic cleanup</li><li>Cost optimization</li></ul>"
    },
    "Snapshot and AMI Recycle Bin - Recycle Bin for Snapshot and AMI AWS": {
        "summary": "Su dung Recycle Bin de bao ve snapshots va AMIs.",
        "explanation": "<p>Recycle Bin bao ve snapshots khoi vo tinh xoa.</p><h4>Tinh nang</h4><ul><li>Soft delete: Khong xoa ngay</li><li>Recovery: Co the khoi phuc</li><li>Automatic cleanup</li></ul><h4>Recovery</h4><ol><li>Select snapshot in Recycle Bin</li><li>Actions > Restore</li></ol>"
    },
    "Copy Snapshot From One Region to Another- Copy Snapshot Cross Region/Account": {
        "summary": "Copy EBS snapshot sang region khac.",
        "explanation": "<p>Copy snapshot de migrate hoac DR.</p><h4>Copy Across Regions</h4><pre>aws ec2 copy-snapshot --source-region us-east-1 --region us-west-2 --source-snapshot-id snap-xxx</pre><h4>Share with Account</h4><pre>aws ec2 modify-snapshot-attribute --snapshot-id snap-xxx --attribute createVolumePermission --operation-type add --user-ids 123456789012</pre>"
    },
    "Encrypt the EBS Volume - What will happen when we encrypt the EBS volume": {
        "summary": "Ma hoa EBS volume su dung AES-256.",
        "explanation": "<p>EBS encryption su dung AES-256.</p><h4>Tu dong Encryption</h4><ul><li>Enable by default trong region</li><li>All new volumes encrypted</li></ul><h4>Ma hoa Volume moi</h4><ul><li>Tao volume voi Encrypted: true</li></ul><h4>Ma hoa Existing</h4><ol><li>Create snapshot</li><li>Copy snapshot voi encryption</li><li>Create volume tu encrypted snapshot</li></ol>"
    },
    "Delete EBS Snapshot - Cleanup Snapshot": {
        "summary": "Cach xoa EBS snapshots de tiet kiem chi phi.",
        "explanation": "<p>Xoa snapshots khong can thiet.</p><h4>Xoa Snapshot</h4><pre>aws ec2 delete-snapshot --snapshot-id snap-xxx</pre><h4>Kiem tra truoc</h4><pre>aws ec2 describe-snapshots --snapshot-ids snap-xxx</pre><h4>Chi phi</h4><ul><li>$0.05/GB-month</li><li>Delete unused snapshots</li></ul>"
    },
    "AWS AMI - Amazon Machine Image - Create your Own AMI": {
        "summary": "Tao custom AMI tu EC2 instance.",
        "explanation": "<p>AMI la blueprint de launch instances.</p><h4>Tao AMI</h4><pre>aws ec2 create-image --instance-id i-xxx --name My-AMI --description Web-server</pre><h4>Components</h4><ul><li>Root volume snapshot</li><li>Launch permissions</li><li>Block device mappings</li></ul><h4>Use Cases</h4><ul><li>Pre-configured instances</li><li>Consistent deployments</li></ul>"
    },
    "Share Your AMI with other AWS account - Delete Your AWS AMI": {
        "summary": "Share AMI voi AWS account khac va cach xoa AMI.",
        "explanation": "<p>Share AMIs de collaborate.</p><h4>Share AMI</h4><pre>aws ec2 modify-image-attribute --image-id ami-xxx --attribute launchPermission --operation-type add --user-ids 123456789012</pre><h4>Xoa AMI</h4><pre>aws ec2 deregister-image --image-id ami-xxx</pre>"
    },
    "Elastic Load Balancer in AWS (ELB) - Classic Load Balancer(CLB)": {
        "summary": "Gioi thieu Elastic Load Balancing va Classic Load Balancer.",
        "explanation": "<p>ELB phan phoi traffic den multiple targets.</p><h4>Load Balancer Types</h4><ul><li>Application LB: Layer 7, HTTP/HTTPS</li><li>Network LB: Layer 4, TCP/UDP</li><li>Gateway LB: Layer 3</li><li>Classic LB: Legacy</li></ul><h4>Features</h4><ul><li>High availability</li><li>Health checks</li><li>SSL termination</li><li>CloudWatch monitoring</li></ul>"
    },
    "EC2 Instance Accessible by LoadBalancer Only | Access Webserver via LoadBalancer": {
        "summary": "Cau hinh EC2 chi accessible qua Load Balancer.",
        "explanation": "<p>Bao mat EC2 bang cach chi cho phep traffic qua LB.</p><h4>Security Groups</h4><h5>LB SG: Inbound 0.0.0.0, Outbound to EC2 SG</h5><h5>EC2 SG: Inbound from LB SG only</h5><h4>Benefits</h4><ul><li>Hide instances</li><li>Single entry point</li><li>Better DDoS protection</li></ul>"
    },
    "Delete Classic Load Balancer": {
        "summary": "Cach xoa Classic Load Balancer.",
        "explanation": "<p>Xoa CLB khi khong can thiet.</p><h4>Xoa</h4><pre>aws elb delete-load-balancer --load-balancer-name my-clb</pre><h4>Luu y</h4><ul><li>CLB deletion khong affect instances</li><li>DNS records can update</li></ul>"
    },
    "Application Load Balancer | Layer 7 Load Balancer": {
        "summary": "Gioi thieu Application Load Balancer.",
        "explanation": "<p>ALB hoat dong o Layer 7.</p><h4>Features</h4><ul><li>Path-based routing</li><li>Host-based routing</li><li>HTTP/2, WebSocket support</li></ul><h4>Components</h4><ul><li>Load Balancer</li><li>Listeners</li><li>Target Groups</li><li>Rules</li></ul><h4>Create ALB</h4><pre>aws elbv2 create-load-balancer --name my-alb --type application --subnets subnet-xxx --security-groups sg-xxx</pre>"
    },
    "Path Base Routing in Application Load Balancer | Application Load Balancer": {
        "summary": "Su dung path-based routing de route traffic.",
        "explanation": "<p>ALB co the route traffic dua tren URL path.</p><h4>Vi du Routing</h4><pre>/api/* -> API Target Group\n/images/* -> Static Content\n/* -> Default</pre><h4>Create Rule</h4><pre>aws elbv2 create-rule --listener-arn arn:aws:... --conditions Field=path-pattern,Values=/api/* --priority 100 --actions Type=forward,TargetGroupArn=arn:aws:...</pre>"
    },
    "How Get Client IP address on Application Server | Application Load Balancer": {
        "summary": "Cach lay client IP khi su dung ALB.",
        "explanation": "<p>ALB forward client IP trong headers.</p><h4>Headers</h4><ul><li>X-Forwarded-For: Client IP</li><li>X-Forwarded-Port: Client port</li><li>X-Forwarded-Proto: HTTP/HTTPS</li></ul><h4>Example (Node.js)</h4><pre>const clientIP = req.headers['x-forwarded-for'];</pre><h4>Example (Nginx)</h4><pre>set_real_ip_from 10.0.0.0/8;\nreal_ip_header X-Forwarded-For;</pre>"
    },
    "Stickiness And Custom Page Routing in Application Load Balancer": {
        "summary": "Cau hinh sticky sessions trong ALB.",
        "explanation": "<p>Sticky sessions dam bao requests cung client den cung target.</p><h4>Enable</h4><pre>aws elbv2 modify-target-group-attributes --target-group-arn arn:aws:... --attributes Key=stickiness.enabled,Value=true Key=stickiness.lb_cookie.duration_seconds,Value=86400</pre><h4>Use Cases</h4><ul><li>Session-based applications</li><li>User state</li></ul>"
    },
    "Network Load Balancer | Layer 4 Load Balancer | AWS Tutorials": {
        "summary": "Gioi thieu Network Load Balancer.",
        "explanation": "<p>NLB hoat dong o Layer 4, ultra-low latency.</p><h4>Features</h4><ul><li>Layer 4 (TCP/UDP/TLS)</li><li>Static IP per AZ</li><li>Preserve client IP</li><li>Handle millions requests/second</li></ul><h4>vs ALB</h4><ul><li>NLB: Static IP, Layer 4</li><li>ALB: Dynamic IP, Layer 7</li></ul>"
    },
    "AWS Launch Template - Auto Scaling Group ( ASG ) - AWS (In Hindi)": {
        "summary": "Tao Launch Template va Auto Scaling Group.",
        "explanation": "<p>Launch Template va ASG giup auto-scale instances.</p><h4>Launch Template</h4><ul><li>AMI, instance type, SG</li><li>User data, IAM role</li></ul><h4>Auto Scaling Group</h4><ul><li>Min, Max, Desired capacity</li><li>Load Balancer integration</li><li>Scaling policies</li></ul><h4>Create</h4><pre>aws autoscaling create-auto-scaling-group --auto-scaling-group-name my-asg --launch-template launch-template-id lt-xxx --min-size 1 --max-size 5 --desired-capacity 2</pre>"
    },
    "Auto Scaling in Action - How to Enable Automatic Scaling - AWS (In Hindi)": {
        "summary": "Cau hinh Auto Scaling policies.",
        "explanation": "<p>Auto Scaling policies kiem soat khi nao scale.</p><h4>Target Tracking</h4><pre>Keep CPU at 50%\naws autoscaling put-scaling-policy --policy-name cpu-tracking --auto-scaling-group-name my-asg --policy-type TargetTrackingScaling --target-tracking-configuration TargetValue=50</pre><h4>Metrics</h4><ul><li>CPUUtilization</li><li>NetworkIn/Out</li><li>RequestCountPerTarget</li></ul>"
    },
    "Auto Scaling With Load Balancer - Load Balancer with Auto Scaling - AWS (Hindi)": {
        "summary": "Tich hop Auto Scaling Group voi Load Balancer.",
        "explanation": "<p>Ket hop ASG va ELB.</p><h4>Benefits</h4><ul><li>LB distributes traffic</li><li>ASG replaces unhealthy instances</li><li>Automatic registration</li></ul><h4>Setup</h4><ol><li>Create ALB/NLB</li><li>Create Target Group</li><li>Attach TG to ASG</li></ol>"
    },
    "Enable Termination Protection - Hibernet vs PowerOff - AWS (Hindi)": {
        "summary": "Bao ve instances khoi accidental termination.",
        "explanation": "<p>Termination protection prevent accidental deletion.</p><h4>Enable</h4><pre>aws ec2 modify-instance-attribute --instance-id i-xxx --disable-api-termination Value=true</pre><h4>Stop vs Hibernate vs Terminate</h4><ul><li>Stop: EBS preserved</li><li>Hibernate: Memory to EBS</li><li>Terminate: Deleted</li></ul>"
    },
    "How to create Reserve Instace - How to attach multiple NIC - AWS (Hindi)": {
        "summary": "Tao Reserved Instances va cau hinh multiple NICs.",
        "explanation": "<p>Reserved Instances tiet kiem chi phi.</p><h4>Purchase</h4><ol><li>EC2 > Reserved Instances</li><li>Select offering</li><li>Choose payment option</li></ol><h4>Payment Options</h4><ul><li>No Upfront</li><li>Partial Upfront</li><li>All Upfront</li></ul><h4>Multiple ENIs</h4><pre>aws ec2 create-network-interface --subnet-id subnet-xxx</pre>"
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
