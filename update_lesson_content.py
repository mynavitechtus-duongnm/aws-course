#!/usr/bin/env python3
"""
Script to update data.js with detailed explanations for AWS course lessons
Based on Gaurav Sharma's AWS Tutorials course
"""

detailed_content = {
    # Module 1: Introduction to AWS
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
    <li><strong>200+ Services:</strong>覆盖计算、存储、数据库、AI、IoT等全方位服务</li>
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
        "summary": "Giải thích chi tiết 3 mô hình dịch vụ đám mây: IaaS (Infrastructure as a Service), PaaS (Platform as a Service), và SaaS (Software as a Service). So sánh vị trí kiểm soát của khách hàng trong mỗi mô hình.",
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
<table style="width:100%; border-collapse: collapse;">
<tr style="background: var(--bg-surface);">
    <th style="padding: 10px; border: 1px solid var(--border);">Layer</th>
    <th style="padding: 10px; border: 1px solid var(--border);">On-Premise</th>
    <th style="padding: 10px; border: 1px solid var(--border);">IaaS</th>
    <th style="padding: 10px; border: 1px solid var(--border);">PaaS</th>
    <th style="padding: 10px; border: 1px solid var(--border);">SaaS</th>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Applications</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Data</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Shared</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Runtime</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Operating System</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Virtualization</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Servers</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Storage</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Networking</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Customer</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Shared</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Shared</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Provider</td>
</tr>
</table>"""
    },
    
    "Deployment Model of Clouds - Public Private and Hybrid Cloud": {
        "summary": "Giới thiệu 3 deployment models của cloud computing: Public Cloud, Private Cloud, và Hybrid Cloud. Giải thích khi nào nên sử dụng từng loại và các use cases cụ thể.",
        "explanation": """<p>Bài học này phân tích 3 deployment models (mô hình triển khai) của cloud computing và các use cases phù hợp cho từng loại.</p>

<h4>1. Public Cloud</h4>
<ul>
    <li><strong>Khái niệm:</strong> Tài nguyên được chia sẻ giữa nhiều organizations, hosted bởi cloud provider (AWS, Azure, GCP)</li>
    <li><strong>Ví dụ AWS:</strong> AWS Regions, AWS Outposts (dạng managed)</li>
    <li><strong>Ưu điểm:</strong>
        <ul>
            <li>Chi phí thấp (pay-as-you-go)</li>
            <li>Không cần quản lý infrastructure</li>
            <li>Scale linh hoạt, almost unlimited</li>
            <li>High availability built-in</li>
        </ul>
    </li>
    <li><strong>Nhược điểm:</strong>
        <ul>
            <li>Less control over infrastructure</li>
            <li>Security concerns cho某些敏感数据</li>
            <li>Compliance restrictions có thể áp dụng</li>
        </ul>
    </li>
    <li><strong>Use cases:</strong> Web applications, development/test environments, startups</li>
</ul>

<h4>2. Private Cloud</h4>
<ul>
    <li><strong>Khái niệm:</strong> Cloud infrastructure dành riêng cho một organization, có thể on-premise hoặc hosted</li>
    <li><strong>Ví dụ AWS:</strong> AWS Outposts (on-premise), VMware on AWS</li>
    <li><strong>Ưu điểm:</strong>
        <ul>
            <li>Full control over infrastructure</li>
            <li>Enhanced security và compliance</li>
            <li>Consistent với on-premise workloads</li>
            <li>Predictable performance</li>
        </ul>
    </li>
    <li><strong>Nhược điểm:</strong>
        <ul>
            <li>Higher upfront costs</li>
            <li>Requires technical expertise to manage</li>
            <li>Limited scalability</li>
        </ul>
    </li>
    <li><strong>Use cases:</strong> Financial services, healthcare, government, enterprises with strict compliance</li>
</ul>

<h4>3. Hybrid Cloud</h4>
<ul>
    <li><strong>Khái niệm:</strong> Kết hợp public cloud và private cloud, cho phép data và applications di chuyển giữa hai môi trường</li>
    <li><strong>Ví dụ AWS:</strong> AWS Direct Connect, AWS Storage Gateway, AWS Outposts</li>
    <li><strong>Ưu điểm:</strong>
        <ul>
            <li>Flexibility - workloads có thể chạy ở nơi tốt nhất</li>
            <li>Cost optimization - burst to cloud khi cần</li>
            <li>Security - sensitive data stays on-premise</li>
            <li>Migration path - gradually move to cloud</li>
        </ul>
    </li>
    <li><strong>Use cases:</strong>
        <ul>
            <li>Web apps on public cloud + databases on private</li>
            <li>Burst processing during peak times</li>
            <li>Disaster recovery (DR) setups</li>
            <li>Cloud bursting architecture</li>
        </ul>
    </li>
</ul>

<h4>4. Multi-Cloud</h4>
<ul>
    <li><strong>Khái niệm:</strong> Sử dụng multiple cloud providers (AWS + Azure + GCP)</li>
    <li><strong>Ưu điểm:</strong> Vendor independence, avoid lock-in, best-of-breed services</li>
    <li><strong>Thách thức:</strong> Complexity in management, requires multi-cloud expertise</li>
</ul>

<h4>So sánh nhanh</h4>
<ul>
    <li><strong>Public Cloud:</strong> Best for most workloads, cost-effective, scalable</li>
    <li><strong>Private Cloud:</strong> Best for regulated industries, sensitive data</li>
    <li><strong>Hybrid Cloud:</strong> Best for gradual migration, burst capacity</li>
    <li><strong>Multi-Cloud:</strong> Best for avoiding vendor lock-in, disaster recovery</li>
</ul>"""
    },
    
    "How Aws Charge - AWS pricing": {
        "summary": "Giải thích cách AWS tính phí và các mô hình pricing: Pay-as-you-go, Reserved Instances, Savings Plans, Spot Instances. Hiểu cách tối ưu chi phí AWS.",
        "explanation": """<p>AWS sử dụng mô hình pricing linh hoạt "pay for what you use" (trả tiền cho những gì bạn sử dụng). Bài học này giải thích chi tiết các cách tính phí và chiến lược tối ưu chi phí.</p>

<h4>AWS Pricing Philosophy</h4>
<ul>
    <li><strong>Pay for what you use:</strong> Không phí trả trước, không chi phí ẩn</li>
    <li><strong>Pay less when you reserve:</strong> Giảm 30-70% với Reserved Instances</li>
    <li><strong>Pay even less with more:</strong> Volume discounts khi sử dụng nhiều hơn</li>
    <li><strong>No charges for Data Transfer between Services:</strong> Data transfer trong same region free</li>
</ul>

<h4>Main Pricing Models</h4>

<h5>1. On-Demand (Pay-as-you-go)</h5>
<ul>
    <li>Không có commitment</li>
    <li>Trả theo giờ hoặc giây (với Lambda, ECS)</li>
    <li>Phù hợp cho: Short-term projects, spike workloads, testing</li>
    <li>Ví dụ EC2: t3.micro ~$0.0104/hr (us-east-1)</li>
</ul>

<h5>2. Reserved Instances (RI)</h5>
<ul>
    <li>Commitment 1 hoặc 3 years</li>
    <li>Giảm 30-72% so với On-Demand</li>
    <li>Các loại:
        <ul>
            <li><strong>Standard RI:</strong> Giảm nhiều nhất, ít flexible</li>
            <li><strong>Convertible RI:</strong> Có thể đổi instance family</li>
            <li><strong>Scheduled RI:</strong> Cho recurring schedules</li>
        </ul>
    </li>
    <li>Phù hợp cho: Baseline workloads, production systems</li>
</ul>

<h5>3. Savings Plans</h5>
<ul>
    <li>Thay thế linh hoạt hơn cho RIs</li>
    <li><strong>Compute Savings Plans:</strong> Áp dụng cho EC2, Lambda, Fargate</li>
    <li><strong>EC2 Instance Savings Plans:</strong> Áp dụng cho specific instance family</li>
    <li>Giảm lên đến 72%</li>
</ul>

<h5>4. Spot Instances</h5>
<ul>
    <li>Sử dụng unused EC2 capacity</li>
    <li>Giảm đến 90% so với On-Demand</li>
    <li>Có thể bị interrupted bất cứ lúc nào (2-minute warning)</li>
    <li>Phù hợp cho: Batch processing, ML training, fault-tolerant workloads</li>
</ul>

<h5>5. Dedicated Hosts</h5>
<ul>
    <li>Physical servers dedicated cho bạn</li>
    <li>Compliance requirements, BYOL (Bring Your Own License)</li>
    <li>Most expensive option</li>
</ul>

<h4>AWS Free Tier</h4>
<ul>
    <li><strong>Always Free:</strong> Lambda (1M requests/month), DynamoDB (25GB), SNS (1M publishes)</li>
    <li><strong>12 Months Free:</strong> EC2 (750h t2.micro), S3 (5GB), RDS (750h db.t2.micro)</li>
    <li><strong>Short-term Trials:</strong> Free trials cho nhiều services</li>
</ul>

<h4>Cost Optimization Tips</h4>
<ul>
    <li>Use Cost Explorer để monitor spending</li>
    <li>Set up Budgets với alerts</li>
    <li>Right-size instances (đừng over-provision)</li>
    <li>Use Auto Scaling để match demand</li>
    <li>Delete unused resources (EBS volumes, Elastic IPs)</li>
    <li>Leverage S3 Intelligent-Tiering</li>
</ul>"""
    },
    
    "What/Why is AWS region | AWS Region Map | AWSGlobal Infrastructure": {
        "summary": "Giới thiệu AWS Regions - các vùng địa lý trên toàn thế giới nơi AWS có data centers. Giải thích cách chọn region phù hợp dựa trên latency, compliance, và chi phí.",
        "explanation": """<p>AWS Regions là tập hợp các Availability Zones được đặt tại các vị trí địa lý khác nhau trên thế giới. Mỗi Region là một khu vực độc lập với multiple Availability Zones.</p>

<h4>AWS Global Infrastructure</h4>
<ul>
    <li><strong>Regions:</strong> 33 geographic locations (2024)</li>
    <li><strong>Availability Zones:</strong> 105 data centers riêng biệt</li>
    <li><strong>Edge Locations:</strong> 450+ locations cho CDN và DNS</li>
    <li><strong>Local Zones:</strong> Mở rộng AWS closer to users</li>
    <li><strong>Wavelength Zones:</strong> Cho 5G applications</li>
</ul>

<h4>AWS Regions (tính đến 2024)</h4>
<table style="width:100%; border-collapse: collapse;">
<tr style="background: var(--bg-surface);">
    <th style="padding: 10px; border: 1px solid var(--border);">Region Name</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Region Code</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Location</th>
</tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">US East (N. Virginia)</td><td style="padding: 8px; border: 1px solid var(--border);">us-east-1</td><td style="padding: 8px; border: 1px solid var(--border);">North America</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">US West (Oregon)</td><td style="padding: 8px; border: 1px solid var(--border);">us-west-2</td><td style="padding: 8px; border: 1px solid var(--border);">North America</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">Europe (Ireland)</td><td style="padding: 8px; border: 1px solid var(--border);">eu-west-1</td><td style="padding: 8px; border: 1px solid var(--border);">Europe</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">Asia Pacific (Singapore)</td><td style="padding: 8px; border: 1px solid var(--border);">ap-southeast-1</td><td style="padding: 8px; border: 1px solid var(--border);">Asia Pacific</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">Asia Pacific (Tokyo)</td><td style="padding: 8px; border: 1px solid var(--border);">ap-northeast-1</td><td style="padding: 8px; border: 1px solid var(--border);">Asia Pacific</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">South America (São Paulo)</td><td style="padding: 8px; border: 1px solid var(--border);">sa-east-1</td><td style="padding: 8px; border: 1px solid var(--border);">South America</td></tr>
</table>

<h4>Cách chọn Region</h4>

<h5>1. Latency</h5>
<ul>
    <li>Chọn region gần users nhất để giảm latency</li>
    <li>Sử dụng Route 53 Latency Routing để auto-route đến region nhanh nhất</li>
</ul>

<h5>2. Compliance & Data Sovereignty</h5>
<ul>
    <li>Một số countries có yêu cầu data phải stay trong borders</li>
    <li>GDPR: Data of EU citizens phải stay in EU</li>
    <li>Chọn region phù hợp với regulatory requirements</li>
</ul>

<h5>3. Service Availability</h5>
<ul>
    <li>Một số services không có sẵn ở tất cả regions</li>
    <li>Kiểm tra AWS Regional Services List trước khi chọn</li>
</ul>

<h5>4. Cost</h5>
<ul>
    <li>Giá services khác nhau giữa các regions</li>
    <li>Ví dụ: us-east-1 thường rẻ hơn các regions khác</li>
</ul>

<h5>5. Disaster Recovery</h5>
<ul>
    <li>Multi-region architecture cho DR</li>
    <li>Chọn regions cách xa nhau để tránh regional outages</li>
</ul>

<h4>Không nên chọn region gần nhất về mặt địa lý?</h4>
<ul>
    <li>Region gần nhất có thể không phải là region nhanh nhất</li>
    <li>Network routes có thể không tối ưu</li>
    <li>Best practice: Test latency từ các regions khác nhau</li>
</ul>"""
    },
    
    "What/Why is AWS Availability Zones | AWS Global Infrastructure": {
        "summary": "Giải thích Availability Zones (AZs) - các data centers riêng biệt trong một Region. Tại sao AZs quan trọng cho high availability và cách thiết kế multi-AZ architecture.",
        "explanation": """<p>Availability Zones (AZs) là các data centers riêng biệt về mặt vật lý nhưng được kết nối với nhau bằng low-latency networking trong một Region. Mỗi AZ được thiết kế để isolated khỏi failures của các AZs khác.</p>

<h4>Cấu trúc của Availability Zone</h4>
<ul>
    <li><strong>Physical Separation:</strong> AZs cách nhau ít nhất 100km (thường 50-80km)</li>
    <li><strong>Independent Power:</strong> Separate power grids, backup generators</li>
    <li><strong>Independent Networking:</strong> Separate ISPs, redundant network paths</li>
    <li><strong>Independent Cooling:</strong> Separate HVAC systems</li>
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
    <li>Redundancy at every level</li>
</ul>

<h5>3. Scalability</h5>
<ul>
    <li>Có thể distribute workloads across multiple AZs</li>
    <li>Load balancing giữa các AZs</li>
</ul>

<h4>Multi-AZ Architecture</h4>

<h5>RDS Multi-AZ</h5>
<ul>
    <li>Automatic replication đến standby AZ</li>
    <li>Automatic failover trong 1-2 phút</li>
    <li>Zero data loss với synchronous replication</li>
</ul>

<h5>EC2 Auto Scaling</h5>
<ul>
    <li>Auto Scaling Group phân phối instances across multiple AZs</li>
    <li>Tự động replace failed instances</li>
</ul>

<h5>Application Architecture</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
                    ┌─────────────────────────────────┐
                    │           INTERNET              │
                    └─────────────┬───────────────────┘
                                  │
                    ┌─────────────▼───────────────────┐
                    │       Load Balancer             │
                    │  (Multi-AZ automatically)       │
                    └─────┬───────────────┬───────────┘
                          │               │
              ┌───────────▼───┐   ┌───────▼───────────┐
              │   AZ-1        │   │   AZ-2            │
              │  ┌─────────┐  │   │  ┌─────────┐      │
              │  │EC2 Inst│  │   │  │EC2 Inst│      │
              │  └─────────┘  │   │  └─────────┘      │
              └───────────────┘   └───────────────────┘
                          │               │
              ┌───────────▼───────────┬───▼────────────┐
              │   Primary RDS       │   Standby RDS   │
              │   (AZ-1)            │   (AZ-2)       │
              └─────────────────────┴─────────────────┘
</pre>

<h4>Best Practices</h4>
<ul>
    <li><strong>Luôn sử dụng at least 2 AZs</strong> cho production workloads</li>
    <li><strong>Use Load Balancers</strong> để distribute traffic</li>
    <li><strong>Enable Multi-AZ</strong> cho RDS, ElastiCache, Redshift</li>
    <li><strong>Don't put all resources in one AZ</strong> - đó là anti-pattern</li>
    <li><strong>Test failover</strong> định kỳ</li>
</ul>

<h4>SLA và Credits</h4>
<ul>
    <li>Single AZ: 99.5% uptime</li>
    <li>Multi-AZ: 99.99% uptime</li>
    <li>Nếu không đạt SLA, AWS cấp service credits</li>
</ul>"""
    },
    
    "What/Why is Local Zones | Local Zones | AWS Global Infrastructure": {
        "summary": "Giới thiệu AWS Local Zones - mở rộng AWS infrastructure closer to users ở các thành phố lớn. Giải thích sự khác biệt giữa Regions, Availability Zones, và Local Zones.",
        "explanation": """<p>AWS Local Zones là các vị trí compute edge được đặt closer to large population centers, cho phép run latency-sensitive applications gần users hơn mà không cần chờ Region infrastructure.</p>

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
    <li>Subset of AWS services (compute, storage, databases, containers)</li>
    <li>Latency: < 10ms cho end users</li>
    <li>Ví dụ: Los Angeles, Boston, Chicago, Dallas, Houston</li>
</ul>

<h5>Edge Locations</h5>
<ul>
    <li>Part of CloudFront CDN network</li>
    <li>Used for caching và delivery (CloudFront, Route 53)</li>
    <li>Không run full EC2 workloads</li>
</ul>

<h4>Use Cases cho Local Zones</h4>

<h5>1. Ultra-low Latency Applications</h5>
<ul>
    <li>Real-time gaming</li>
    <li>Video conferencing</li>
    <li>AR/VR applications</li>
    <li>Machine learning inference</li>
</ul>

<h5>2. Content Delivery</h5>
<ul>
    <li>Streaming media</li>
    <li>Live sports events</li>
    <li>Local content caching</li>
</ul>

<h5>3. Data Residency Requirements</h5>
<ul>
    <li>Regulatory requirements cần data stay in specific location</li>
    <li>Compliance-sensitive workloads</li>
</ul>

<h4>Available Local Zones (2024)</h4>
<ul>
    <li>US: Los Angeles, Boston, Chicago, Dallas, Denver, Houston, Kansas City, Las Vegas, Miami, Minneapolis, Nashville, Phoenix, Portland, Seattle</li>
    <li>More coming: Atlanta, New York, Philadelphia, San Francisco Bay Area</li>
</ul>

<h4>How to Use Local Zones</h4>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Enable Local Zone for your VPC
aws ec2 modify-availability-zone-group \
    --group-name us-west-2-lax-1 \
    --opt-in-status opted-in

# Create subnet in Local Zone
aws ec2 create-subnet \
    --vpc-id vpc-xxxx \
    --availability-zone-id us-west-2-lax-1a \
    --cidr-block 10.0.1.0/24

# Launch instance in Local Zone
aws ec2 run-instances \
    --image-id ami-xxxx \
    --instance-type t3.medium \
    --subnet-id subnet-xxxx
</pre>

<h4>Services Available in Local Zones</h4>
<ul>
    <li>Amazon EC2 (compute)</li>
    <li>Amazon EBS (storage)</li>
    <li>Amazon VPC (networking)</li>
    <li>Amazon ECS/EKS (containers)</li>
    <li>Amazon RDS (Aurora, PostgreSQL, MySQL)</li>
    <li>Amazon ElastiCache</li>
</ul>

<h4>Limitations</h4>
<ul>
    <li>Không phải tất cả services đều available</li>
    <li>Không thể use Local Zones as DR target (vì nó extension của Region)</li>
    <li>Data transfer costs có thể khác</li>
</ul>"""
    },
    
    "Create AWS Account | Create AWS Free Tier Account": {
        "summary": "Hướng dẫn tạo AWS Account mới và kích hoạt Free Tier. Giải thích các loại Free Tier (Always Free, 12 Months Free, Short-term Trials) và cách tránh charges không mong muốn.",
        "explanation": """<p>Bài học này hướng dẫn step-by-step cách tạo AWS Account mới và kích hoạt Free Tier để bắt đầu học AWS miễn phí.</p>

<h4>Yêu cầu trước khi tạo Account</h4>
<ul>
    <li>Email address hợp lệ</li>
    <li>Credit/Debit card (Visa, Mastercard, hoặc American Express)</li>
    <li>Phone number để xác minh (SMS hoặc voice call)</li>
</ul>

<h4>Các bước tạo AWS Account</h4>

<h5>Bước 1: Truy cập AWS Console</h5>
<ul>
    <li>Go to: <a href="https://aws.amazon.com/console">https://aws.amazon.com/console</a></li>
    <li>Click "Create an AWS Account"</li>
</ul>

<h5>Bước 2: Nhập thông tin</h5>
<ul>
    <li>Email address</li>
    <li>AWS account name (friendly name)</li>
    <li>Password (minimum 12 characters)</li>
</ul>

<h5>Bước 3: Xác minh identity</h5>
<ul>
    <li>AWS sẽ gửi verification code qua email</li>
    <li>Nhập code để xác minh</li>
</ul>

<h5>Bước 4: Thông tin cá nhân</h5>
<ul>
    <li>Full name</li>
    <li>Phone number</li>
    <li>Country/Region</li>
</ul>

<h5>Bước 5: Thông tin thanh toán</h5>
<ul>
    <li>Nhập credit/debit card information</li>
    <li>AWS sẽ charge $1 (hoặc equivalent) để verify card (sẽ được refund)</li>
</ul>

<h5>Bước 6: Xác minh phone</h5>
<ul>
    <li>AWS sẽ gọi hoặc gửi SMS với PIN code</li>
    <li>Nhập PIN để hoàn tất</li>
</ul>

<h5>Bước 7: Chọn Support Plan</h5>
<ul>
    <li><strong>Basic Support:</strong> Miễn phí, bao gồm documentation và forums</li>
    <li><strong>Developer Support:</strong> $29/tháng</li>
    <li><strong>Business Support:</strong> $100/tháng</li>
    <li><strong>Enterprise Support:</strong> $15,000/tháng</li>
</ul>

<h4>AWS Free Tier Details</h4>

<h5>Always Free (Không bao giờ hết hạn)</h5>
<ul>
    <li>AWS Lambda: 1M requests/month, 400,000 GB-seconds compute</li>
    <li>Amazon DynamoDB: 25GB storage, 25 WCU/RCU</li>
    <li>Amazon SNS: 1M publishes</li>
    <li>Amazon SQS: 1M requests</li>
    <li>CloudWatch: 10 custom metrics, 5GB logs storage</li>
</ul>

<h5>12 Months Free (Từ ngày đăng ký)</h5>
<ul>
    <li>EC2: 750 hours t2.micro/tháng</li>
    <li>S3: 5GB standard storage</li>
    <li>RDS: 750 hours db.t2.micro</li>
    <li>CloudFront: 1TB outbound, 10M requests</li>
</ul>

<h4>Cách tránh charges không mong muốn</h4>

<h5>1. Set up Billing Alerts</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Enable billing alerts in CloudWatch
aws cloudwatch put-metric-alarm \
    --alarm-name billing-alarm \
    --alarm-description "Alert when charges exceed $10" \
    --metric-name EstimatedCharges \
    --namespace AWS/Billing \
    --statistic Maximum \
    --period 21600 \
    --threshold 10 \
    --comparison-operator GreaterThanThreshold
</pre>

<h5>2. Use Budgets</h5>
<ul>
    <li>Set up AWS Budgets với alerts</li>
    <li>Set action để auto-stop resources khi exceed budget</li>
</ul>

<h5>3. Xóa unused resources</h5>
<ul>
    <li>Terminate EC2 instances khi không sử dụng</li>
    <li>Delete unused EBS volumes</li>
    <li>Release unused Elastic IPs</li>
    <li>Delete unused RDS instances</li>
</ul>

<h5>4. Use Cost Explorer</h5>
<ul>
    <li>Theo dõi spending hàng ngày</li>
    <li>Identify services with unexpected charges</li>
</ul>

<h4>Root Account Security Best Practices</h4>
<ul>
    <li><strong>Enable MFA</strong> immediately after creating account</li>
    <li><strong>Don't use root account</strong> for daily tasks - create IAM users</li>
    <li><strong>Set strong password</strong> for root account</li>
    <li><strong>Enable CloudTrail</strong> for audit logging</li>
</ul>"""
    }
}

# Add more detailed content for EC2 lessons
ec2_lessons = {
    "Create First EC2 Instance | EC2 Instance Creation in AWS": {
        "summary": "Hướng dẫn step-by-step cách tạo EC2 instance đầu tiên trên AWS Console. Bao gồm chọn AMI, instance type, configure network, và kết nối đến instance.",
        "explanation": """<p>Amazon EC2 (Elastic Compute Cloud) cung cấp scalable computing capacity trong AWS cloud. Bài học này hướng dẫn cách tạo EC2 instance đầu tiên.</p>

<h4>EC2 Instance Creation Steps</h4>

<h5>Bước 1: Chọn AMI (Amazon Machine Image)</h5>
<ul>
    <li><strong>Amazon Linux 2 AMI:</strong> Free tier eligible, RHEL-based, stable</li>
    <li><strong>Ubuntu Server:</strong> Popular, good community support</li>
    <li><strong>Windows Server:</strong> For Windows workloads</li>
    <li><strong>CentOS, Fedora:</strong> Other Linux distributions</li>
</ul>

<h5>Bước 2: Chọn Instance Type</h5>
<ul>
    <li><strong>t2.micro:</strong> Free tier, 1 vCPU, 1GB RAM</li>
    <li><strong>t3.micro:</strong> 2 vCPU, 1GB RAM, better performance</li>
    <li><strong>m5.large:</strong> 2 vCPU, 8GB RAM, general purpose</li>
    <li><strong>c5.large:</strong> 2 vCPU, 4GB RAM, compute optimized</li>
</ul>

<h5>Bước 3: Configure Instance Details</h5>
<ul>
    <li><strong>Number of instances:</strong> Số lượng muốn launch</li>
    <li><strong>Network:</strong> VPC và subnet (default VPC hoặc custom)</li>
    <li><strong>Auto-assign Public IP:</strong> Enable để có public IP</li>
    <li><strong>Shutdown behavior:</strong> Stop hoặc Terminate</li>
    <li><strong>Enable termination protection:</strong> Prevent accidental termination</li>
</ul>

<h5>Bước 4: Add Storage</h5>
<ul>
    <li><strong>Root volume:</strong> OS disk, thường 8GB-30GB</li>
    <li><strong>Additional volumes:</strong> Data volumes như EBS</li>
    <li><strong>Volume type:</strong> gp3 (general purpose SSD)</li>
    <li><strong>Encrypted:</strong> Enable encryption for security</li>
</ul>

<h5>Bước 5: Add Tags</h5>
<ul>
    <li>Key-value pairs để organize resources</li>
    <li>Ví dụ: Name=WebServer, Environment=Production</li>
</ul>

<h5>Bước 6: Configure Security Group</h5>
<ul>
    <li><strong>SSH (port 22):</strong> Cho Linux access</li>
    <li><strong>RDP (port 3389):</strong> Cho Windows access</li>
    <li><strong>HTTP (port 80):</strong> Web traffic</li>
    <li><strong>HTTPS (port 443):</strong> Secure web traffic</li>
    <li><strong>Source:</strong> My IP, Anywhere, Custom IP</li>
</ul>

<h5>Bước 7: Review và Launch</h5>
<ul>
    <li>Review tất cả settings</li>
    <li>Chọn hoặc tạo key pair để SSH</li>
    <li>Click "Launch Instances"</li>
</ul>

<h4>Kết nối đến EC2 Instance</h4>

<h5>Linux/Mac</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Change key permissions
chmod 400 your-key.pem

# Connect via SSH
ssh -i your-key.pem ec2-user@your-public-ip

# For Ubuntu AMI
ssh -i your-key.pem ubuntu@your-public-ip
</pre>

<h5>Windows (PuTTY)</h5>
<ul>
    <li>Convert .pem to .ppk using PuTTYgen</li>
    <li>Connect sử dụng PuTTY với private key</li>
</ul>

<h4>Basic Linux Commands sau khi login</h4>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Update system packages
sudo yum update -y  # Amazon Linux
sudo apt update -y  # Ubuntu

# Check system info
uname -a
df -h
free -h

# Check network
hostname -I
ping google.com
</pre>

<h4>Common EC2 Instance States</h4>
<ul>
    <li><strong>pending:</strong> Đang khởi tạo</li>
    <li><strong>running:</strong> Đang chạy</li>
    <li><strong>stopping:</strong> Đang dừng</li>
    <li><strong>stopped:</strong> Đã dừng (không charge compute, nhưng charge storage)</li>
    <li><strong>terminated:</strong> Đã xóa (không thể recover)</li>
</ul>

<h4>Cost Considerations</h4>
<ul>
    <li><strong>Running:</strong> Charge theo giờ</li>
    <li><strong>Stopped:</strong> Chỉ charge EBS storage</li>
    <li><strong>Terminated:</strong> Không charge gì</li>
    <li><strong>Data transfer:</strong> Separate charges áp dụng</li>
</ul>"""
    },
    
    "Access EC2 Instance From Windows Machine | EC2 Instance Connect": {
        "summary": "Hướng dẫn kết nối đến EC2 instance từ Windows sử dụng EC2 Instance Connect, PuTTY, và Windows Subsystem for Linux (WSL). So sánh các phương pháp và best practices.",
        "explanation": """<p>Có nhiều cách để kết nối đến EC2 Linux instance từ Windows machine. Bài học này giới thiệu các phương pháp phổ biến nhất.</p>

<h4>Phương pháp 1: EC2 Instance Connect (Khuyến nghị)</h4>

<h5>Ưu điểm</h5>
<ul>
    <li>Không cần key pair - sử dụng browser</li>
    <li>SSH keys được managed bởi AWS</li>
    <li>Tự động timeout sau 60 giây không hoạt động</li>
    <li>Audit logging through CloudTrail</li>
</ul>

<h5>Cách sử dụng</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
1. Mở AWS Console > EC2 > Instances
2. Chọn instance của bạn
3. Click "Connect"
4. Chọn tab "EC2 Instance Connect"
5. Click "Connect"
6. Browser sẽ mở terminal
</pre>

<h5>Yêu cầu</h5>
<ul>
    <li>Instance phải có public IP</li>
    <li>Security group cho phép port 22</li>
    <li>EC2 Instance Connect endpoint phải reachable</li>
</ul>

<h4>Phương pháp 2: PuTTY</h4>

<h5>Bước 1: Cài đặt PuTTY</h5>
<ul>
    <li>Download từ: <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/">https://www.chiark.greenend.org.uk/~sgtatham/putty/</a></li>
    <li>Cài đặt cả PuTTY và PuTTYgen</li>
</ul>

<h5>Bước 2: Convert .pem to .ppk</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
1. Mở PuTTYgen
2. Click "Load" > Chọn file .pem
3. Click "Save private key"
4. Save as .ppk file
</pre>

<h5>Bước 3: Kết nối với PuTTY</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
1. Mở PuTTY
2. Host Name: ec2-user@your-public-ip (hoặc ubuntu@ cho Ubuntu)
3. Port: 22
4. Connection > SSH > Auth > Browse > Chọn file .ppk
5. Click "Open"
</pre>

<h4>Phương pháp 3: Windows Subsystem for Linux (WSL)</h4>

<h5>Bước 1: Enable WSL</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Run in PowerShell (Admin)
wsl --install

# Restart computer sau khi cài đặt
</pre>

<h5>Bước 2: Kết nối SSH</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Copy key vào WSL
cp /mnt/c/path/to/key.pem ~/key.pem
chmod 400 ~/key.pem

# Connect
ssh -i ~/key.pem ec2-user@your-public-ip
</pre>

<h4>Phương pháp 4: Windows Command Prompt/PowerShell (OpenSSH)</h4>

<h5>Bước 1: Enable OpenSSH Client</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Run in PowerShell (Admin)
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
</pre>

<h5>Bước 2: Kết nối</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Navigate to key location
cd C:\\path\\to\\key

# Set permissions (PowerShell)
icacls key.pem /inheritance:r /grant:r "$env:USERNAME:R"

# Connect
ssh -i key.pem ec2-user@your-public-ip
</pre>

<h4>Security Best Practices</h4>

<h5>1. Security Group Configuration</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Restrict SSH to your IP only
Type: SSH
Protocol: TCP
Port: 22
Source: Your IP Address (e.g., 203.0.113.0/32)
</pre>

<h5>2. Use Session Manager thay vì SSH</h5>
<ul>
    <li>Không cần public IP</li>
    <li>No port 22 cần mở</li>
    <li>Full audit logging</li>
    <li>Use IAM policies để control access</li>
</ul>

<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Install SSM Agent (pre-installed on Amazon Linux 2)
sudo yum install -y amazon-ssm-agent

# Start SSM Agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
</pre>

<h5>3. Enable Connection Limiting</h5>
<ul>
    <li>Limit số concurrent SSH connections</li>
    <li>Use fail2ban để block brute force attacks</li>
</ul>

<h4>Troubleshooting Common Issues</h4>

<h5>Connection Timeout</h5>
<ul>
    <li>Check Security Group allows SSH (port 22)</li>
    <li>Check instance có public IP không</li>
    <li>Check subnet có Internet Gateway không</li>
</ul>

<h5>Permission Denied</h5>
<ul>
    <li>Verify key pair đúng</li>
    <li>Check file permissions (chmod 400)</li>
    <li>Check username đúng (ec2-user, ubuntu, bitnami)</li>
</ul>

<h5>Host Key Verification Failed</h5>
<ul>
    <li>Xóa old host key: <code>ssh-keygen -R your-public-ip</code></li>
    <li>Hoặc edit known_hosts và remove old entry</li>
</ul>"""
    },
    
    "AWS Security Group | Security Group AWS": {
        "summary": "Giải thích chi tiết về Security Groups - virtual firewall cho EC2 instances. Cách tạo, configure, và best practices để bảo mật instances.",
        "explanation": """<p>AWS Security Group là một stateful virtual firewall kiểm soát traffic vào và ra cho EC2 instances và các tài nguyên AWS khác. Đây là first line of defense cho cloud resources.</p>

<h4>Security Group Fundamentals</h4>

<h5>Stateful vs Stateless</h5>
<ul>
    <li><strong>Stateful:</strong> Nếu inbound được allowed, outbound response cũng được allowed tự động</li>
    <li><strong>Stateless:</strong> Phải configure cả inbound và outbound rules riêng biệt</li>
</ul>

<h5>Default Behavior</h5>
<ul>
    <li><strong>Inbound:</strong> Tất cả denied by default</li>
    <li><strong>Outbound:</strong> Tất cả allowed by default</li>
</ul>

<h4>Security Group Rules</h4>

<h5>Rule Components</h5>
<ul>
    <li><strong>Type:</strong> SSH, HTTP, HTTPS, Custom TCP, All Traffic, etc.</li>
    <li><strong>Protocol:</strong> TCP, UDP, ICMP, All</li>
    <li><strong>Port Range:</strong> Specific port (22, 80, 443) hoặc range (8000-9000)</li>
    <li><strong>Source/Destination:</strong>
        <ul>
            <li>IP Address (e.g., 203.0.113.0/24)</li>
            <li>Security Group (e.g., sg-0123456789)</li>
            <li>Prefix List</li>
        </ul>
    </li>
    <li><strong>Description:</strong> Optional, để mô tả rule</li>
</ul>

<h4>Common Security Group Configurations</h4>

<h5>Web Server Security Group</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
Inbound Rules:
┌─────────┬────────┬──────────────┬────────────────────────┐
│  Type   │ Port   │ Source       │ Description             │
├─────────┼────────┼──────────────┼────────────────────────┤
│ SSH     │ 22     │ My IP        │ Admin access only      │
│ HTTP    │ 80     │ 0.0.0.0/0    │ Web traffic            │
│ HTTPS   │ 443    │ 0.0.0.0/0    │ Secure web traffic     │
└─────────┴────────┴──────────────┴────────────────────────┘

Outbound Rules:
┌─────────┬────────┬──────────────┬────────────────────────┐
│  Type   │ Port   │ Destination  │ Description             │
├─────────┼────────┼──────────────┼────────────────────────┤
│ All     │ All    │ 0.0.0.0/0    │ Allow all outbound     │
└─────────┴────────┴──────────────┴────────────────────────┘
</pre>

<h5>Database Server Security Group</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
Inbound Rules:
┌────────────┬─────────┬─────────────────┬──────────────────┐
│  Type      │ Port    │ Source          │ Description       │
├────────────┼─────────┼─────────────────┼──────────────────┤
│ MySQL/Aurora│ 3306   │ App SG ID       │ App tier access  │
│ SSH        │ 22     │ Admin SG ID     │ Admin access     │
└────────────┴─────────┴─────────────────┴──────────────────┘
</pre>

<h5>Load Balancer Security Group</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
Inbound Rules:
┌─────────┬────────┬──────────────┬────────────────────────┐
│  Type   │ Port   │ Source       │ Description             │
├─────────┼────────┼──────────────┼────────────────────────┤
│ HTTP    │ 80     │ 0.0.0.0/0    │ HTTP traffic           │
│ HTTPS   │ 443    │ 0.0.0.0/0    │ HTTPS traffic          │
└─────────┴────────┴──────────────┴────────────────────────┘

Outbound Rules:
┌────────────┬─────────┬─────────────────┬──────────────────┐
│  Type      │ Port    │ Destination     │ Description       │
├────────────┼─────────┼─────────────────┼──────────────────┤
│ Custom TCP │ 80, 443 │ Web Server SG   │ To EC2 instances  │
└────────────┴─────────┴─────────────────┴──────────────────┘
</pre>

<h4>Best Practices</h4>

<h5>1. Principle of Least Privilege</h5>
<ul>
    <li>Chỉ allow những ports cần thiết</li>
    <li>Use specific IP ranges thay vì 0.0.0.0/0</li>
    <li>Restrict admin access đến known IPs</li>
</ul>

<h5>2. Use Security Groups as Source</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# BAD: Allow from any IP
Source: 0.0.0.0/0

# GOOD: Allow from specific security group
Source: sg-0123456789 (Application Server SG)
</pre>

<h5>3. Separate Security Groups by Function</h5>
<ul>
    <li>Web Server SG: HTTP/HTTPS</li>
    <li>Application Server SG: Access from Web SG only</li>
    <li>Database SG: Access from App SG only</li>
</ul>

<h5>4. Naming Conventions</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Good examples
sg-web-prod-01
sg-app-prod-db-access
sg-bastion-prod

# Bad examples
sg-default
sg-test
security-group-1
</pre>

<h5>5. Regular Security Audits</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# List all security groups
aws ec2 describe-security-groups

# Find security groups with wide open access
aws ec2 describe-security-groups \
    --filters Name=ip-permission.cidr,Values="0.0.0.0/0" \
    --query "SecurityGroups[*].{Name:GroupName,ID:GroupId,Rules:IpPermissions}"
</pre>

<h4>Security Group vs NACLs</h4>

<table style="width:100%; border-collapse: collapse;">
<tr style="background: var(--bg-surface);">
    <th style="padding: 10px; border: 1px solid var(--border);">Feature</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Security Group</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Network ACLs</th>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Level</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Instance level</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Subnet level</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Stateful</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Yes (auto-return traffic)</td>
    <td style="padding: 10px; border: 1px solid var(--border);">No (must configure both)</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Rule evaluation</td>
    <td style="padding: 10px; border: 1px solid var(--border);">All rules evaluated</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Processed in order</td>
</tr>
<tr>
    <td style="padding: 10px; border: 1px solid var(--border);">Default</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Allow nothing inbound</td>
    <td style="padding: 10px; border: 1px solid var(--border);">Allow all</td>
</tr>
</table>"""
    },
    
    "EC2 Instance Type | Instance Type in AWS": {
        "summary": "Tổng quan về các loại EC2 Instance Types: General Purpose (T, M), Compute Optimized (C), Memory Optimized (R, X), Storage Optimized (I, D). Cách chọn instance type phù hợp với workload.",
        "explanation": """<p>AWS cung cấp hơn 500 instance types được tối ưu cho các use cases khác nhau. Việc chọn đúng instance type là quan trọng để optimize performance và cost.</p>

<h4>EC2 Instance Families</h4>

<h5>1. General Purpose (T, M)</h5>
<ul>
    <li><strong>Use case:</strong> Web servers, development environments, small databases</li>
    <li><strong>Balance:</strong> CPU, memory, network</li>
    <li><strong>T-Series (Burstable):</strong>
        <ul>
            <li>T3, T3a, T4g - có ability to burst above baseline</li>
            <li>CPU Credits: accumulate when idle, spend when busy</li>
            <li>Phù hợp cho workloads với variable CPU usage</li>
        </ul>
    </li>
    <li><strong>M-Series:</strong>
        <ul>
            <li>M5, M6i, M7g - steady-state performance</li>
            <li>No bursting - consistent CPU</li>
        </ul>
    </li>
</ul>

<h5>2. Compute Optimized (C)</h5>
<ul>
    <li><strong>Use case:</strong> High performance computing, batch processing, ML inference</li>
    <li><strong>Features:</strong> High CPU performance, NVMe storage</li>
    <li><strong>Types:</strong> C5, C6i, C7g, C7i</li>
    <li><strong>Phù hợp cho:</strong>
        <ul>
            <li>Scientific computing</li>
            <li>Video encoding/transcoding</li>
            <li>High-traffic web servers</li>
            <li>Batch processing jobs</li>
        </ul>
    </li>
</ul>

<h5>3. Memory Optimized (R, X, U)</h5>
<ul>
    <li><strong>Use case:</strong> In-memory databases, big data analytics</li>
    <li><strong>Features:</strong> High memory-to-CPU ratio</li>
    <li><strong>Types:</strong>
        <ul>
            <li><strong>R6i, R7g:</strong> General memory optimized</li>
            <li><strong>X2gd, X2idn:</strong> Very high memory</li>
            <li><strong>U-3tb1:</strong> Extreme memory (3TB RAM)</li>
        </ul>
    </li>
    <li><strong>Phù hợp cho:</strong>
        <ul>
            <li>Redis, Memcached</li>
            <li>SAP HANA</li>
            <li>Spark, Hadoop clusters</li>
        </ul>
    </li>
</ul>

<h5>4. Storage Optimized (I, D, H)</h5>
<ul>
    <li><strong>Use case:</strong> High-frequency read/write operations, data warehousing</li>
    <li><strong>Features:</strong> High disk throughput, large instance storage</li>
    <li><strong>Types:</strong>
        <ul>
            <li><strong>I4i, I3:</strong> NVMe SSD, high IOPS</li>
            <li><strong>D2, D3:</strong> High storage density (up to 48TB)</li>
            <li><strong>H1:</strong> Balance of storage and compute</li>
        </ul>
    </li>
</ul>

<h5>5. Accelerated Computing (P, G, Inf)</h5>
<ul>
    <li><strong>Use case:</strong> Machine learning, graphics-intensive applications</li>
    <li><strong>Features:</strong> GPU or FPGA accelerators</li>
    <li><strong>Types:</strong>
        <ul>
            <li><strong>P4d, P5:</strong> NVIDIA A100 GPUs (ML training)</li>
            <li><strong>G4dn, G5:</strong> NVIDIA T4, A10G GPUs (inference)</li>
            <li><strong>Inf2:</strong> AWS Inferentia (ML inference)</li>
            <li><strong>Trn1:</strong> AWS Trainium (ML training)</li>
        </ul>
    </li>
</ul>

<h4>Instance Naming Convention</h4>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
Example: m6i.xlarge
│ │ │ │ └─── Size: nano, micro, small, medium, large, xlarge, 2xlarge, 4xlarge...
│ │ │ └─── Generation: 1, 2, 3, 4, 5...
│ │ └─── Instance Family: i (compute optimized), g (GPU), m (general purpose)...
│ └─── Instance class: 6 (generation number)
└── Family prefix: m (general purpose), c (compute), r (memory)...
</pre>

<h4>Comparing Popular Instance Types</h4>
<table style="width:100%; border-collapse: collapse;">
<tr style="background: var(--bg-surface);">
    <th style="padding: 10px; border: 1px solid var(--border);">Instance</th>
    <th style="padding: 10px; border: 1px solid var(--border);">vCPU</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Memory</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Storage</th>
    <th style="padding: 10px; border: 1px solid var(--border);">Use Case</th>
</tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">t3.micro</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">1 GB</td><td style="padding: 8px; border: 1px solid var(--border);">EBS only</td><td style="padding: 8px; border: 1px solid var(--border);">Dev/Test</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">t3.medium</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">4 GB</td><td style="padding: 8px; border: 1px solid var(--border);">EBS only</td><td style="padding: 8px; border: 1px solid var(--border);">Small Web</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">m5.large</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">8 GB</td><td style="padding: 8px; border: 1px solid var(--border);">EBS only</td><td style="padding: 8px; border: 1px solid var(--border);">App Server</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">c5.large</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">4 GB</td><td style="padding: 8px; border: 1px solid var(--border);">EBS only</td><td style="padding: 8px; border: 1px solid var(--border);">Compute</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">r5.large</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">16 GB</td><td style="padding: 8px; border: 1px solid var(--border);">EBS only</td><td style="padding: 8px; border: 1px solid var(--border);">In-Memory DB</td></tr>
<tr><td style="padding: 8px; border: 1px solid var(--border);">i3.large</td><td style="padding: 8px; border: 1px solid var(--border);">2</td><td style="padding: 8px; border: 1px solid var(--border);">15.25 GB</td><td style="padding: 8px; border: 1px solid var(--border);">NVMe SSD</td><td style="padding: 8px; border: 1px solid var(--border);">NoSQL DB</td></tr>
</table>

<h4>How to Choose Right Instance Type</h4>

<h5>1. Analyze Your Workload</h5>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
Questions to ask:
- CPU-bound or Memory-bound?
- Need local NVMe storage?
- GPU required?
- Burstable or steady-state?
</pre>

<h5>2. Right-Sizing</h5>
<ul>
    <li>Start với smaller instance, monitor và scale up nếu cần</li>
    <li>Use CloudWatch metrics: CPUUtilization, MemoryUtilization</li>
    <li>Use AWS Compute Optimizer để recommend</li>
</ul>

<h5>3. Consider Cost Optimization</h5>
<ul>
    <li>T3: Good for dev/test, not for production CPU spikes</li>
    <li>M5: Good balance for most applications</li>
    <li>Use Savings Plans or RIs cho steady-state workloads</li>
</ul>

<h4>Changing Instance Type</h4>
<pre style="background: var(--bg-surface); padding: 15px; border-radius: 8px; overflow-x: auto;">
# Stop instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Change instance type
aws ec2 modify-instance-attribute \
    --instance-id i-1234567890abcdef0 \
    --instance-type "{\"Value\": \"t3.large\"}"

# Start instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0
</pre>"""
    }
}

# Merge all content
all_content = {**detailed_content, **ec2_lessons}

# Output the content as JSON for use in the update script
import json
print(json.dumps(all_content, indent=2, ensure_ascii=False))
