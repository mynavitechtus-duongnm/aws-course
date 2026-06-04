// AWS Course App - JavaScript

// Icon SVGs
const icons = {
    cloud: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`,
    server: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="20" height="8" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
        <rect x="2" y="14" width="20" height="8" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
        <line x1="6" y1="6" x2="6.01" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        <line x1="6" y1="18" x2="6.01" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    </svg>`,
    database: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="12" cy="5" rx="9" ry="3" stroke="currentColor" stroke-width="2"/>
        <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" stroke="currentColor" stroke-width="2"/>
        <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" stroke="currentColor" stroke-width="2"/>
    </svg>`,
    activity: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`,
    shield: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`,
    globe: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
        <line x1="2" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="2"/>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" stroke="currentColor" stroke-width="2"/>
    </svg>`,
    zap: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`,
    user: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2"/>
    </svg>`,
    mail: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <polyline points="22 6 12 13 2 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`,
    box: `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <polyline points="3 27 12 22 21 27" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <line x1="12" y1="22" x2="12" y2="11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <line x1="3" y1="10" x2="21" y2="10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`
};

// State
let activeModuleIndex = null;
let player = null;
let playerReady = false;
let youtubeApiReady = false;

// Load last viewed lesson from localStorage
function getLastViewed() {
    try {
        const saved = localStorage.getItem('awsCourse_lastViewed');
        return saved ? JSON.parse(saved) : null;
    } catch (e) {
        return null;
    }
}

// Save last viewed lesson to localStorage
function setLastViewed(moduleIndex, lessonIndex) {
    try {
        localStorage.setItem('awsCourse_lastViewed', JSON.stringify({
            moduleIndex,
            lessonIndex,
            timestamp: Date.now()
        }));
    } catch (e) {
        console.log('Could not save to localStorage');
    }
}

// YouTube IFrame API callback - MUST be global
function onYouTubeIframeAPIReady() {
    console.log('YouTube API Ready');
    youtubeApiReady = true;
}

// Create YouTube player using iframe
function createYouTubePlayer(videoId, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    // Validate videoId
    if (!videoId || typeof videoId !== 'string' || videoId.trim() === '') {
        container.innerHTML = '<p style="color:red;padding:20px;">Video ID không hợp lệ</p>';
        return;
    }
    
    // Validate YouTube video ID format (11 chars, alphanumeric, hyphens, underscores)
    const validVideoId = /^[a-zA-Z0-9_-]{11}$/.test(videoId);
    if (!validVideoId) {
        container.innerHTML = '<p style="color:red;padding:20px;">Video ID không đúng định dạng: ' + videoId + '</p>';
        return;
    }
    
    // Use iframe embed with captions
    const embedUrl = `https://www.youtube.com/embed/${videoId}?rel=0&cc_load_policy=1&cc_lang_pref=vi&hl=vi&playsinline=1`;
    
    container.innerHTML = `
        <iframe 
            width="100%" 
            height="100%" 
            src="${embedUrl}" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen
           webkitallowfullscreen
            mozallowfullscreen>
        </iframe>
    `;
}

// Enable Vietnamese captions on existing player
function enableVietnameseCaptions() {
    if (player && playerReady) {
        try {
            // Get available caption tracks
            var captionTracks = player.getOption('captions', 'tracklist');
            if (captionTracks && captionTracks.length > 0) {
                // Set Vietnamese caption if available
                player.setOption('captions', 'track', {'languageCode': 'vi'});
                player.setOption('captions', 'loading', 0);
                player.setOption('captions', 'visibility', 'on');
            } else {
                // If no Vietnamese captions, try to enable auto-generated
                player.setOption('captions', 'track', {'languageCode': 'en'});
                player.setOption('captions', 'visibility', 'on');
            }
        } catch (e) {
            console.log('Caption settings not available');
        }
    }
}

// Render modules grid
function renderModules() {
    const grid = document.getElementById('modulesGrid');
    if (!grid) return;

    if (typeof modules === 'undefined') {
        grid.innerHTML = '<p style="color:#ff6b6b;padding:20px;">Không thể tải dữ liệu module.</p>';
        return;
    }

    const lastViewed = getLastViewed();
    
    grid.innerHTML = modules.map((mod, index) => `
        <div class="module-card ${activeModuleIndex === index ? 'active' : ''} ${lastViewed && lastViewed.moduleIndex === index ? 'last-viewed' : ''}" onclick="toggleModule(${index})">
            <div class="module-header">
                <div class="module-number">${mod.id}</div>
                <div class="module-icon">${icons[mod.icon] || icons.cloud}</div>
                ${lastViewed && lastViewed.moduleIndex === index ? '<span class="last-viewed-badge" title="Bài đã xem gần nhất">✓</span>' : ''}
                <div class="module-expand-icon">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <polyline points="6 9 12 15 18 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
            </div>
            <h3 class="module-title">${mod.title}</h3>
            <p class="module-description">${mod.description}</p>
            <div class="module-meta">
                <span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <polygon points="5 3 19 12 5 21 5 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    ${mod.lessons.length} bài
                </span>
            </div>
            <div class="lesson-list" id="lessonList${index}">
                ${activeModuleIndex === index ? renderLessonList(index) : ''}
            </div>
        </div>
    `).join('');
}

// Render list of lessons for a module
function renderLessonList(moduleIndex) {
    const mod = modules[moduleIndex];
    const lastViewed = getLastViewed();
    
    return mod.lessons.map((lesson, lessonIndex) => {
        const isLastViewed = lastViewed && lastViewed.moduleIndex === moduleIndex && lastViewed.lessonIndex === lessonIndex;
        return `
        <div class="lesson-item ${isLastViewed ? 'last-viewed' : ''}" onclick="event.stopPropagation(); openLesson(${moduleIndex}, ${lessonIndex})">
            <div class="lesson-item-play">
                <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <polygon points="5 3 19 12 5 21 5 3"/>
                </svg>
            </div>
            <div class="lesson-item-info">
                <span class="lesson-item-title">${lesson.title}</span>
                <span class="lesson-item-duration">${lesson.duration}</span>
            </div>
            ${isLastViewed ? '<span class="last-viewed-dot" title="Đã xem"></span>' : ''}
        </div>
    `}).join('');
}

// Toggle module expansion
function toggleModule(moduleIndex) {
    if (activeModuleIndex === moduleIndex) {
        activeModuleIndex = null;
    } else {
        activeModuleIndex = moduleIndex;
    }
    renderModules();
    const cards = document.querySelectorAll('.module-card');
    if (cards[moduleIndex]) {
        cards[moduleIndex].scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// Current state
let currentModuleIndex = 0;
let currentLessonIndex = 0;

// Generate enhanced content for a lesson based on its title
function generateEnhancedContent(lesson, moduleTitle) {
    const title = lesson.title || '';
    const lowerTitle = title.toLowerCase();

    // Key AWS concepts to detect
    const isIntro = lowerTitle.includes('introducing') || lowerTitle.includes('what is aws');
    const isEC2 = lowerTitle.includes('ec2') || lowerTitle.includes('instance');
    const isS3 = lowerTitle.includes('s3') || lowerTitle.includes('storage') || lowerTitle.includes('bucket');
    const isIAM = lowerTitle.includes('iam') || lowerTitle.includes('access') || lowerTitle.includes('user') || lowerTitle.includes('role');
    const isVPC = lowerTitle.includes('vpc') || lowerTitle.includes('subnet') || lowerTitle.includes('network');
    const isLambda = lowerTitle.includes('lambda') || lowerTitle.includes('serverless');
    const isRDS = lowerTitle.includes('rds') || lowerTitle.includes('database') || lowerTitle.includes('mysql') || lowerTitle.includes('postgresql');
    const isCloudFront = lowerTitle.includes('cloudfront') || lowerTitle.includes('cdn');
    const isRoute53 = lowerTitle.includes('route53') || lowerTitle.includes('dns') || lowerTitle.includes('domain');
    const isDynamoDB = lowerTitle.includes('dynamodb') || lowerTitle.includes('nosql');
    const isEBS = lowerTitle.includes('ebs') || lowerTitle.includes('volume') || lowerTitle.includes('snapshot');
    const isLoadBalancer = lowerTitle.includes('load balancer') || lowerTitle.includes('elb') || lowerTitle.includes('alb') || lowerTitle.includes('nlb');
    const isAutoScaling = lowerTitle.includes('auto scaling') || lowerTitle.includes('asg');
    const isCloudWatch = lowerTitle.includes('cloudwatch') || lowerTitle.includes('monitoring') || lowerTitle.includes('log');
    const isSNS = lowerTitle.includes('sns') || lowerTitle.includes('notification') || lowerTitle.includes('topic');
    const isSES = lowerTitle.includes('ses') || lowerTitle.includes('email') || lowerTitle.includes('mail');
    const isCognito = lowerTitle.includes('cognito') || lowerTitle.includes('authentication') || lowerTitle.includes('user pool');
    const isAPIGateway = lowerTitle.includes('api gateway') || lowerTitle.includes('rest api') || lowerTitle.includes('http api');
    const isECS = lowerTitle.includes('ecs') || lowerTitle.includes('container') || lowerTitle.includes('docker');

    // Build comprehensive explanation based on detected topics
    let explanation = '';
    let examples = [];
    let references = [];

    if (isIntro) {
        explanation = `
            <p>Amazon Web Services (AWS) là nền tảng điện toán đám mây toàn diện và được sử dụng rộng rãi nhất trên thế giới, cung cấp hơn 200 dịch vụ từ các trung tâm dữ liệu trên toàn cầu.</p>
            
            <h4>Tại sao nên sử dụng AWS?</h4>
            <ul>
                <li><strong>Tiết kiệm chi phí:</strong> Chỉ trả tiền cho những gì bạn sử dụng (Pay-as-you-go)</li>
                <li><strong>Khả năng mở rộng:</strong> Dễ dàng tăng giảm tài nguyên theo nhu cầu</li>
                <li><strong>Độ tin cậy:</strong> Hệ thống uptime cao với các Availability Zones</li>
                <li><strong>Bảo mật:</strong> Đạt chứng chỉ an ninh quốc tế</li>
            </ul>
            
            <h4>Các mô hình dịch vụ đám mây</h4>
            <ul>
                <li><strong>IaaS (Infrastructure as a Service):</strong> Cung cấp tài nguyên hạ tầng ảo hóa như máy chủ, lưu trữ, mạng</li>
                <li><strong>PaaS (Platform as a Service):</strong> Cung cấp nền tảng phát triển ứng dụng</li>
                <li><strong>SaaS (Software as a Service):</strong> Cung cấp phần mềm hoàn chỉnh qua internet</li>
            </ul>
            
            <h4>AWS Regions và Availability Zones</h4>
            <p>AWS có các Regions (Vùng) trên toàn thế giới, mỗi Region chứa nhiều Availability Zones (AZ) riêng biệt để đảm bảo high availability và fault tolerance.</p>
        `;
        examples = [
            { title: 'So sánh chi phí', content: 'On-premise: Cần đầu tư ban đầu lớn cho server, điện,冷却. Cloud: Bắt đầu với chi phí thấp, chỉ trả khi sử dụng.' },
            { title: 'Mở rộng nhanh chóng', content: 'Khi traffic tăng đột biến, AWS cho phép scale up trong vài phút thay vì mua thêm server trong nhiều ngày.' }
        ];
        references = [
            { name: 'AWS Documentation', url: 'https://docs.aws.amazon.com' },
            { name: 'AWS Well-Architected Framework', url: 'https://aws.amazon.com/architecture' },
            { name: 'AWS Free Tier', url: 'https://aws.amazon.com/free' }
        ];
    } else if (isEC2) {
        explanation = `
            <p>Amazon Elastic Compute Cloud (EC2) là dịch vụ cung cấp máy chủ ảo (virtual servers) trong AWS cloud, cho phép bạn khởi chạy và quản lý các instances theo nhu cầu.</p>
            
            <h4>Các loại EC2 Instance</h4>
            <ul>
                <li><strong>General Purpose (T3, T2):</strong> Cân bằng giữa compute, memory, network</li>
                <li><strong>Compute Optimized (C5, C4):</strong> Tối ưu cho compute-intensive workloads</li>
                <li><strong>Memory Optimized (R5, R4):</strong> Cho các ứng dụng cần nhiều RAM</li>
                <li><strong>Storage Optimized (I3, D2):</strong> Tối ưu cho storage-intensive workloads</li>
            </ul>
            
            <h4>Security Groups</h4>
            <p>Security Group hoạt động như một virtual firewall để kiểm soát traffic vào và ra instance. Đây là first line of defense cho EC2 instances.</p>
            
            <h4>EC2 Instance Connect</h4>
            <p>Cho phép kết nối đến EC2 instance qua SSH một cách bảo mật mà không cần quản lý SSH keys.</p>
        `;
        examples = [
            { title: 'Tạo EC2 Instance', content: 'Sử dụng AWS Console hoặc CLI: aws ec2 run-instances --image-id ami-xxxx --instance-type t3.micro --key-name my-key' },
            { title: 'Cấu hình Security Group', content: 'Mở port 80 cho HTTP: aws ec2 authorize-security-group-ingress --group-id sg-xxx --protocol tcp --port 80 --cidr 0.0.0.0/0' }
        ];
        references = [
            { name: 'EC2 Documentation', url: 'https://docs.aws.amazon.com/ec2' },
            { name: 'EC2 Instance Types', url: 'https://aws.amazon.com/ec2/instance-types' },
            { name: 'Amazon Machine Images (AMI)', url: 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html' }
        ];
    } else if (isS3) {
        explanation = `
            <p>Amazon Simple Storage Service (S3) là dịch vụ lưu trữ object storage với độ bền cao (99.999999999%), scalability vô hạn và chi phí thấp.</p>
            
            <h4>S3 Storage Classes</h4>
            <ul>
                <li><strong>S3 Standard:</strong> Truy cập thường xuyên, chi phí cao nhất</li>
                <li><strong>S3 Intelligent-Tiering:</strong> Tự động di chuyển data giữa các tiers</li>
                <li><strong>S3 Standard-IA:</strong> Truy cập ít thường xuyên, phí retrieval</li>
                <li><strong>S3 Glacier:</strong> Lưu trữ lâu dài, chi phí thấp, retrieval trong vài phút đến giờ</li>
            </ul>
            
            <h4>S3 Versioning</h4>
            <p>Cho phép lưu giữ nhiều phiên bản của một object, giúp bảo vệ against accidental deletes và có thể khôi phục previous versions.</p>
            
            <h4>S3 Lifecycle Policies</h4>
            <p>Tự động chuyển objects sang storage classes khác hoặc xóa sau một khoảng thời gian nhất định.</p>
        `;
        examples = [
            { title: 'Tạo S3 Bucket', content: 'aws s3 mb s3://my-unique-bucket-name --region us-east-1' },
            { title: 'Upload file', content: 'aws s3 cp myfile.txt s3://my-bucket/' },
            { title: 'Enable Versioning', content: 'aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled' }
        ];
        references = [
            { name: 'S3 Documentation', url: 'https://docs.aws.amazon.com/s3' },
            { name: 'S3 Storage Classes', url: 'https://aws.amazon.com/s3/storage-classes' },
            { name: 'S3 Cost Optimization', url: 'https://aws.amazon.com/s3/cost-optimization' }
        ];
    } else if (isIAM) {
        explanation = `
            <p>AWS Identity and Access Management (IAM) cho phép bạn quản lý truy cập an toàn đến các dịch vụ AWS. IAM controls ai có thể truy cập và họ có thể làm gì với resources.</p>
            
            <h4>IAM Users</h4>
            <p>User IAM đại diện cho một người hoặc ứng dụng cần truy cập AWS resources. Mỗi user có credentials riêng (access keys, password).</p>
            
            <h4>IAM Groups</h4>
            <p>Groups là cách để quản lý permissions cho nhiều users cùng một lúc. Gán policies cho group thay vì từng user.</p>
            
            <h4>IAM Roles</h4>
            <p>Roles cấp permissions tạm thời cho services, users, hoặc applications mà không cần shared credentials.</p>
            
            <h4>IAM Policies</h4>
            <p>JSON documents định nghĩa permissions. Có thể attach vào users, groups, hoặc roles.</p>
        `;
        examples = [
            { title: 'Tạo IAM User', content: 'aws iam create-user --user-name my-user' },
            { title: 'Tạo IAM Group', content: 'aws iam create-group --group-name Developers' },
            { title: 'Attach Policy', content: 'aws iam attach-group-policy --group-name Developers --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess' }
        ];
        references = [
            { name: 'IAM Documentation', url: 'https://docs.aws.amazon.com/iam' },
            { name: 'IAM Best Practices', url: 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html' },
            { name: 'IAM Policy Simulator', url: 'https://policysim.aws.amazon.com' }
        ];
    } else if (isLambda) {
        explanation = `
            <p>AWS Lambda là dịch vụ serverless compute cho phép bạn chạy code mà không cần provisioning hoặc quản lý servers. Chỉ trả tiền cho compute time thực sự sử dụng.</p>
            
            <h4>Lambda Functions</h4>
            <p>Lambda function là một đơn vị deployment. Mỗi function chạy trong một execution environment với assigned memory và timeout.</p>
            
            <h4>Triggers</h4>
            <p>Lambda functions có thể được triggered bởi nhiều AWS services: S3, DynamoDB, SNS, API Gateway, CloudWatch Events, và nhiều hơn nữa.</p>
            
            <h4>Cold Start vs Warm Start</h4>
            <p>Cold start xảy ra khi function được invoke lần đầu tiên hoặc sau thời gian không hoạt động. Warm start là invocation tiếp theo trong cùng execution environment.</p>
            
            <h4>Concurrency</h4>
            <ul>
                <li><strong>Reserved Concurrency:</strong> Đảm bảo capacity cho function</li>
                <li><strong>Provisioned Concurrency:</strong> Pre-warms functions để tránh cold starts</li>
            </ul>
        `;
        examples = [
            { title: 'Lambda Function Example (Node.js)', content: 'exports.handler = async (event) => { return { statusCode: 200, body: JSON.stringify("Hello from Lambda!") }; };' },
            { title: 'Deploy with AWS CLI', content: 'aws lambda create-function --function-name my-function --runtime nodejs18.x --handler index.handler --zip-file fileb://deployment.zip --role lambda-role-arn' }
        ];
        references = [
            { name: 'Lambda Documentation', url: 'https://docs.aws.amazon.com/lambda' },
            { name: 'Lambda Pricing', url: 'https://aws.amazon.com/lambda/pricing' },
            { name: 'Serverless Land', url: 'https://serverlessland.com' }
        ];
    } else if (isVPC) {
        explanation = `
            <p>Amazon Virtual Private Cloud (VPC) cho phép bạn tạo một virtual network riêng trong AWS cloud, kiểm soát hoàn toàn network configuration của mình.</p>
            
            <h4>VPC Components</h4>
            <ul>
                <li><strong>Subnets:</strong> Phân chia VPC thành các mạng con, có thể là public hoặc private</li>
                <li><strong>Route Tables:</strong> Xác định traffic flow trong VPC</li>
                <li><strong>Internet Gateway:</strong> Cho phép VPC kết nối internet</li>
                <li><strong>NAT Gateway:</strong> Cho phép private instances truy cập internet outbound</li>
            </ul>
            
            <h4>Public vs Private Subnets</h4>
            <p>Public subnets có route đến Internet Gateway. Private subnets chỉ có route internal, chỉ accessible từ within VPC hoặc through NAT.</p>
        `;
        examples = [
            { title: 'Tạo VPC', content: 'aws ec2 create-vpc --cidr-block 10.0.0.0/16' },
            { title: 'Tạo Subnet', content: 'aws ec2 create-subnet --vpc-id vpc-xxx --cidr-block 10.0.1.0/24 --availability-zone us-east-1a' }
        ];
        references = [
            { name: 'VPC Documentation', url: 'https://docs.aws.amazon.com/vpc' },
            { name: 'VPC Networking Fundamentals', url: 'https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html' }
        ];
    } else if (isRDS) {
        explanation = `
            <p>Amazon Relational Database Service (RDS) là managed database service hỗ trợ nhiều database engines: MySQL, PostgreSQL, Oracle, MariaDB, và Amazon Aurora.</p>
            
            <h4>Database Engines</h4>
            <ul>
                <li><strong>Amazon Aurora:</strong> MySQL và PostgreSQL-compatible, tự động replication, up to 15 read replicas</li>
                <li><strong>MySQL/PostgreSQL:</strong> Popular open-source databases với full managed experience</li>
                <li><strong>MariaDB:</strong> MySQL-compatible, community-driven fork</li>
                <li><strong>Oracle/SQL Server:</strong> Enterprise databases với license options</li>
            </ul>
            
            <h4>High Availability với Multi-AZ</h4>
            <p>Multi-AZ deployment tự động replicate data đến một standby instance trong AZ khác, cung cấp automatic failover.</p>
        `;
        examples = [
            { title: 'Tạo RDS Instance', content: 'aws rds create-db-instance --db-instance-identifier my-db --db-instance-class db.t3.micro --engine mysql --allocated-storage 20 --master-username admin --master-user-password mypassword' }
        ];
        references = [
            { name: 'RDS Documentation', url: 'https://docs.aws.amazon.com/rds' },
            { name: 'RDS Best Practices', url: 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html' }
        ];
    } else if (isEBS) {
        explanation = `
            <p>Amazon Elastic Block Store (EBS) cung cấp block storage volumes có độ bền cao cho use với EC2 instances. EBS volumes là independent resources tách biệt khỏi EC2 instances.</p>
            
            <h4>EBS Volume Types</h4>
            <ul>
                <li><strong>gp3:</strong> General purpose SSD, chi phí thấp nhất</li>
                <li><strong>gp2:</strong> General purpose SSD (thế hệ trước)</li>
                <li><strong>io2:</strong> Provisioned IOPS SSD, cho workloads cần high performance</li>
                <li><strong>st1:</strong> Throughput optimized HDD, cho sequential data</li>
                <li><strong>sc1:</strong> Cold storage HDD, chi phí thấp nhất</li>
            </ul>
            
            <h4>EBS Snapshots</h4>
            <p>Snapshots là incremental backups được lưu trữ trong S3. Có thể tạo new volumes từ snapshots hoặc copy snapshots across regions.</p>
        `;
        examples = [
            { title: 'Tạo EBS Volume', content: 'aws ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a' },
            { title: 'Attach Volume', content: 'aws ec2 attach-volume --volume-id vol-xxx --instance-id i-xxx --device /dev/sdf' }
        ];
        references = [
            { name: 'EBS Documentation', url: 'https://docs.aws.amazon.com/ebs' },
            { name: 'EBS Volume Types', url: 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html' }
        ];
    } else if (isLoadBalancer) {
        explanation = `
            <p>Elastic Load Balancing (ELB) phân phối incoming traffic đến multiple targets như EC2 instances, containers, và IP addresses để improve application availability và fault tolerance.</p>
            
            <h4>Load Balancer Types</h4>
            <ul>
                <li><strong>Application Load Balancer (ALB):</strong> Layer 7, HTTP/HTTPS traffic, path-based routing, host-based routing</li>
                <li><strong>Network Load Balancer (NLB):</strong> Layer 4, TCP/UDP traffic, ultra-low latency, static IP</li>
                <li><strong>Gateway Load Balancer:</strong> Cho third-party virtual appliances</li>
                <li><strong>Classic Load Balancer:</strong> Legacy, Layer 4 & 7 (không khuyến khích)</li>
            </ul>
            
            <h4>Auto Scaling Group (ASG)</h4>
            <p>ASG tự động điều chỉnh số lượng EC2 instances dựa trên metrics như CPU usage, memory, hoặc custom metrics.</p>
        `;
        examples = [
            { title: 'Tạo ALB', content: 'aws elbv2 create-load-balancer --name my-alb --type application --subnets subnet-xxx --security-groups sg-xxx' },
            { title: 'Tạo Target Group', content: 'aws elbv2 create-target-group --name my-tg --protocol HTTP --port 80 --vpc-id vpc-xxx' }
        ];
        references = [
            { name: 'ELB Documentation', url: 'https://docs.aws.amazon.com/elasticloadbalancing' },
            { name: 'ALB Documentation', url: 'https://docs.aws.amazon.com/elasticloadbalancing/latest/application' }
        ];
    } else if (isCloudFront) {
        explanation = `
            <p>Amazon CloudFront là Content Delivery Network (CDN) giúp deliver content to users globally với low latency và high transfer speeds.</p>
            
            <h4>How CloudFront Works</h4>
            <p>Khi user request content, CloudFront edge locations gần nhất sẽ serve request. Nếu content không có sẵn, CloudFront sẽ lấy từ origin và cache lại.</p>
            
            <h4>Key Features</h4>
            <ul>
                <li><strong>Edge Locations:</strong> 450+ locations worldwide</li>
                <li><strong>Cache Behavior:</strong> Kiểm soát caching rules</li>
                <li><strong>SSL/TLS:</strong> Free shared certificate hoặc custom SSL</li>
                <li><strong>Geo-Restriction:</strong> Kiểm soát ai có thể truy cập content</li>
            </ul>
        `;
        examples = [
            { title: 'Tạo CloudFront Distribution', content: 'aws cloudfront create-distribution --origin-domain-name my-bucket.s3.amazonaws.com' }
        ];
        references = [
            { name: 'CloudFront Documentation', url: 'https://docs.aws.amazon.com/cloudfront' },
            { name: 'CloudFront Pricing', url: 'https://aws.amazon.com/cloudfront/pricing' }
        ];
    } else if (isRoute53) {
        explanation = `
            <p>Amazon Route 53 là highly available và scalable DNS web service, đồng thời cung cấp domain registration và health checking.</p>
            
            <h4>DNS Record Types</h4>
            <ul>
                <li><strong>A Record:</strong> Map domain name đến IPv4 address</li>
                <li><strong>AAAA Record:</strong> Map domain name đến IPv6 address</li>
                <li><strong>CNAME:</strong> Alias cho domain name khác</li>
                <li><strong>MX Record:</strong> Email routing</li>
                <li><strong>TXT Record:</strong> Text data cho verification</li>
            </ul>
            
            <h4>Routing Policies</h4>
            <ul>
                <li><strong>Simple:</strong> Single resource</li>
                <li><strong>Weighted:</strong> Phân phối traffic theo tỷ lệ</li>
                <li><strong>Latency:</strong> Route đến region có latency thấp nhất</li>
                <li><strong>Failover:</strong> Primary và secondary resources</li>
                <li><strong>Geolocation:</strong> Route dựa trên vị trí user</li>
            </ul>
        `;
        examples = [
            { title: 'Tạo A Record', content: 'aws route53 change-resource-record-sets --hosted-zone-id Zxxx --change-batch file://change.json' }
        ];
        references = [
            { name: 'Route 53 Documentation', url: 'https://docs.aws.amazon.com/route53' },
            { name: 'Route 53 Developer Guide', url: 'https://docs.aws.amazon.com/Route53/latest/DeveloperGuide' }
        ];
    } else if (isDynamoDB) {
        explanation = `
            <p>Amazon DynamoDB là fully managed NoSQL database service với single-digit millisecond latency ở bất kỳ scale nào. Hoàn hảo cho workloads cần consistent, single-digit millisecond performance.</p>
            
            <h4>Core Components</h4>
            <ul>
                <li><strong>Tables:</strong> Collection of items</li>
                <li><strong>Items:</strong> Row trong table, up to 400KB</li>
                <li><strong>Attributes:</strong> Columns, có thể be nested</li>
                <li><strong>Primary Key:</strong> Partition key hoặc Partition + Sort key</li>
            </ul>
            
            <h4>Capacity Modes</h4>
            <ul>
                <li><strong>On-Demand:</strong> Pay per request, không cần capacity planning</li>
                <li><strong>Provisioned:</strong> Đặt trước RCU/WCU, có thể use auto-scaling</li>
            </ul>
        `;
        examples = [
            { title: 'Create Table', content: 'aws dynamodb create-table --table-name Music --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S --key-schema AttributeName=Artist,KeyType=H AttributeName=SongTitle,KeyType=R --billing-mode PAY_PER_REQUEST' }
        ];
        references = [
            { name: 'DynamoDB Documentation', url: 'https://docs.aws.amazon.com/dynamodb' },
            { name: 'DynamoDB Best Practices', url: 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html' }
        ];
    } else if (isCloudWatch) {
        explanation = `
            <p>Amazon CloudWatch là dịch vụ monitoring và observability, cung cấp data và insights về application health, resource utilization, và operational health.</p>
            
            <h4>CloudWatch Features</h4>
            <ul>
                <li><strong>Metrics:</strong> Resource và application metrics</li>
                <li><strong>Logs:</strong> Centralized logging từ EC2, Lambda, etc.</li>
                <li><strong>Alarms:</strong> Reactive notifications khi metrics vượt ngưỡng</li>
                <li><strong>Dashboards:</strong> Custom visualizations</li>
            </ul>
            
            <h4>CloudWatch Agent</h4>
            <p>Install CloudWatch Agent trên EC2 instances để collect system-level metrics và log files.</p>
        `;
        examples = [
            { title: 'Create Alarm', content: 'aws cloudwatch put-metric-alarm --alarm-name high-cpu --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 80 --comparison-operator GreaterThanThreshold --dimensions Name=InstanceId,Value=i-xxx --evaluation-periods 2 --alarm-actions arn:aws:sns:us-east-1:123456789012:my-topic' }
        ];
        references = [
            { name: 'CloudWatch Documentation', url: 'https://docs.aws.amazon.com/cloudwatch' },
            { name: 'CloudWatch Agent', url: 'https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent' }
        ];
    } else if (isSNS || isSES) {
        explanation = `
            <p>${isSNS ? 'Amazon Simple Notification Service (SNS)' : 'Amazon Simple Email Service (SES)'} là ${isSNS ? 'messaging service' : 'email service'} managed hoàn toàn bởi AWS.</p>
            
            <h4>${isSNS ? 'SNS Concepts' : 'SES Features'}</h4>
            <ul>
                ${isSNS ? `
                <li><strong>Topics:</strong> Channel để publish messages</li>
                <li><strong>Subscriptions:</strong> Endpoints đăng ký nhận messages</li>
                <li><strong>Publishers:</strong> Applications hoặc AWS services publish messages</li>
                ` : `
                <li><strong>Verified Identities:</strong> Domains hoặc email addresses</li>
                <li><strong>Send Options:</strong> SMTP hoặc AWS SDK</li>
                <li><strong>Receiving:</strong> Process incoming emails</li>
                `}
            </ul>
        `;
        references = [
            { name: isSNS ? 'SNS Documentation' : 'SES Documentation', url: isSNS ? 'https://docs.aws.amazon.com/sns' : 'https://docs.aws.amazon.com/ses' }
        ];
    } else if (isCognito) {
        explanation = `
            <p>Amazon Cognito cung cấp authentication, authorization, và user management cho web và mobile apps. Hỗ trợ đăng nhập bằng social identity providers (Google, Facebook, Apple) và enterprise identity providers (SAML, OIDC).</p>
            
            <h4>User Pools</h4>
            <p>User directory và sign-up/sign-in service. Cung cấp JWT tokens sau khi authentication thành công.</p>
            
            <h4>Identity Pools</h4>
            <p>Cho phép users nhận temporary AWS credentials để access AWS services trực tiếp.</p>
        `;
        examples = [
            { title: 'Cognito Flow', content: '1. User signs up/signs in -> Cognito verifies credentials\\n2. Cognito returns JWT tokens (ID Token, Access Token, Refresh Token)\\n3. App uses ID Token for user identification\\n4. App uses Access Token to call APIs with authorization' }
        ];
        references = [
            { name: 'Cognito Documentation', url: 'https://docs.aws.amazon.com/cognito' },
            { name: 'Cognito User Pools', url: 'https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html' }
        ];
    } else if (isAPIGateway) {
        explanation = `
            <p>Amazon API Gateway là fully managed service để create, deploy, và manage APIs at any scale. Hỗ trợ REST, HTTP, và WebSocket APIs.</p>
            
            <h4>API Types</h4>
            <ul>
                <li><strong>REST API:</strong> Full feature set cho RESTful APIs</li>
                <li><strong>HTTP API:</strong> Lightweight, low-cost, cho serverless workloads</li>
                <li><strong>WebSocket API:</strong> Bidirectional communication cho real-time apps</li>
            </ul>
            
            <h4>Integration Types</h4>
            <ul>
                <li><strong>Lambda:</strong> Invoke Lambda functions</li>
                <li><strong>HTTP:</strong> Proxy to HTTP endpoints</li>
                <li><strong>AWS Service:</strong> Direct integration với AWS services</li>
            </ul>
        `;
        references = [
            { name: 'API Gateway Documentation', url: 'https://docs.aws.amazon.com/apigateway' },
            { name: 'API Gateway REST API', url: 'https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html' }
        ];
    } else if (isECS) {
        explanation = `
            <p>Amazon Elastic Container Service (ECS) là highly scalable, high performance container orchestration service hỗ trợ Docker containers.</p>
            
            <h4>ECS Concepts</h4>
            <ul>
                <li><strong>Clusters:</strong> Logical grouping of container instances</li>
                <li><strong>Task Definitions:</strong> Blueprint cho containers</li>
                <li><strong>Tasks:</strong> Running instances of task definitions</li>
                <li><strong>Services:</strong> Maintain desired count of tasks</li>
            </ul>
            
            <h4>Launch Types</h4>
            <ul>
                <li><strong>EC2:</strong> Manage EC2 instances để run containers</li>
                <li><strong>Fargate:</strong> Serverless - AWS manages the infrastructure</li>
            </ul>
        `;
        references = [
            { name: 'ECS Documentation', url: 'https://docs.aws.amazon.com/ecs' },
            { name: 'ECS on Fargate', url: 'https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html' }
        ];
    } else {
        // Generic content for other topics
        explanation = `
            <p>Bài học này thuộc module <strong>${moduleTitle}</strong> trong khóa học AWS toàn diện.</p>
            
            <h4>Tổng quan</h4>
            <p>AWS cung cấp hơn 200 dịch vụ giúp bạn xây dựng và deploy applications một cách nhanh chóng và hiệu quả trên cloud.</p>
            
            <h4>Các best practices khi làm việc với AWS</h4>
            <ul>
                <li>Sử dụng IAM roles thay vì shared credentials</li>
                <li>Enable logging và monitoring cho tất cả resources</li>
                <li>Use infrastructure as code (CloudFormation, Terraform)</li>
                <li>Implement backup và disaster recovery strategies</li>
                <li>Regularly review và optimize costs</li>
            </ul>
        `;
        references = [
            { name: 'AWS Documentation', url: 'https://docs.aws.amazon.com' },
            { name: 'AWS Well-Architected Framework', url: 'https://aws.amazon.com/architecture' }
        ];
    }

    return { explanation, examples, references };
}

// Open lesson modal
function openLesson(moduleIndex, lessonIndex) {
    currentModuleIndex = moduleIndex;
    currentLessonIndex = lessonIndex;

    const module = modules[moduleIndex];
    const lesson = module.lessons[lessonIndex];
    const modal = document.getElementById('lessonModal');
    const modalBody = document.getElementById('modalBody');

    if (!modal || !modalBody) return;

    const prevLesson = lessonIndex > 0 ? module.lessons[lessonIndex - 1] : null;
    const nextLesson = lessonIndex < module.lessons.length - 1 ? module.lessons[lessonIndex + 1] : null;

    // Use explanation from data.js if available, otherwise fallback to generateEnhancedContent
    const customExplanation = lesson.explanation;
    const { explanation, examples, references } = customExplanation ? 
        { explanation: customExplanation, examples: [], references: [] } : 
        generateEnhancedContent(lesson, module.title);
    const summary = lesson.summary || `Bài học về ${lesson.title} trong module ${module.title}.`;

    modalBody.innerHTML = `
        <button class="modal-close" onclick="closeModal()">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </button>
        <div class="lesson-video-column">
            <div class="video-header">
                <div class="lesson-category">${module.title}</div>
                <h1 class="lesson-title">${lesson.title}</h1>
                <div class="lesson-meta">
                    <span>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                            <polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        ${lesson.duration}
                    </span>
                    <span>Bài ${lessonIndex + 1} / ${module.lessons.length}</span>
                </div>
            </div>

            <div class="video-container">
                <div id="youtubePlayer"></div>
            </div>
        </div>

        <div class="lesson-content-column">
            <!-- Summary Section -->
            <div class="lesson-section">
                <h2 class="lesson-section-title">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <polyline points="14 2 14 8 20 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="16" y1="13" x2="8" y2="13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <line x1="16" y1="17" x2="8" y2="17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Tóm tắt
                </h2>
                <div class="lesson-summary">${summary}</div>
            </div>

            <!-- Detailed Explanation Section -->
            <div class="lesson-section">
                <h2 class="lesson-section-title">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Giải thích chi tiết
                </h2>
                <div class="lesson-explanation">${explanation}</div>
            </div>

            <!-- Examples Section -->
            ${examples && examples.length > 0 ? `
            <div class="lesson-section">
                <h2 class="lesson-section-title">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <polyline points="16 18 22 12 16 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <polyline points="8 6 2 12 8 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Ví dụ minh hoạ
                </h2>
                ${examples.map(ex => `
                    <div class="example-box">
                        <div class="example-box-title">${ex.title}</div>
                        <pre class="example-code">${ex.content}</pre>
                    </div>
                `).join('')}
            </div>
            ` : ''}

            <!-- References Section -->
            ${references && references.length > 0 ? `
            <div class="lesson-section">
                <h2 class="lesson-section-title">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Tài liệu tham khảo
                </h2>
                <div class="references-list">
                    ${references.map(ref => `
                        <a href="${ref.url}" target="_blank" class="reference-link">
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <polyline points="15 3 21 3 21 9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <line x1="10" y1="14" x2="21" y2="3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            ${ref.name}
                        </a>
                    `).join('')}
                </div>
            </div>
            ` : ''}

            <!-- Fixed Navigation at bottom of content column -->
            <div class="lesson-nav-spacer"></div>
            <div class="lesson-nav">
                ${prevLesson ? `
                <a href="#" class="lesson-nav-btn prev" onclick="event.preventDefault(); openLesson(${moduleIndex}, ${lessonIndex - 1})">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <polyline points="15 18 9 12 15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <div class="nav-btn-text">
                        <span class="nav-label">Bài trước</span>
                        <span class="nav-title">${prevLesson.title}</span>
                    </div>
                </a>
                ` : '<div></div>'}
                ${nextLesson ? `
                <a href="#" class="lesson-nav-btn next" onclick="event.preventDefault(); openLesson(${moduleIndex}, ${lessonIndex + 1})">
                    <div class="nav-btn-text">
                        <span class="nav-label">Bài tiếp theo</span>
                        <span class="nav-title">${nextLesson.title}</span>
                    </div>
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <polyline points="9 18 15 12 9 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </a>
                ` : '<div></div>'}
            </div>
        </div>

    `;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    
    // Save to localStorage
    setLastViewed(moduleIndex, lessonIndex);
    
    // Initialize YouTube player
    const videoId = lesson.videoId;
    setTimeout(() => {
        createYouTubePlayer(videoId, 'youtubePlayer');
    }, 100);
}

// Go back to lesson list
function goBackToList(moduleIndex) {
    closeModal();
    activeModuleIndex = moduleIndex;
    renderModules();
    setTimeout(() => {
        const cards = document.querySelectorAll('.module-card');
        if (cards[moduleIndex]) {
            cards[moduleIndex].scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }, 100);
}

// Close modal
function closeModal() {
    const modal = document.getElementById('lessonModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        // Stop YouTube player
        if (player) {
            player.stopVideo();
            player.destroy();
            player = null;
            playerReady = false;
        }
    }
}

// Close on escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Close on overlay click
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        closeModal();
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderModules();
    
    // Auto-open last viewed lesson if exists
    const lastViewed = getLastViewed();
    if (lastViewed) {
        // Validate that the lesson still exists
        if (!modules[lastViewed.moduleIndex] || 
            !modules[lastViewed.moduleIndex].lessons[lastViewed.lessonIndex]) {
            console.log('Last viewed lesson no longer exists, clearing...');
            localStorage.removeItem('awsCourse_lastViewed');
            return;
        }
        
        const videoId = modules[lastViewed.moduleIndex].lessons[lastViewed.lessonIndex].videoId;
        if (!videoId) {
            console.log('Last viewed lesson has no videoId, clearing...');
            localStorage.removeItem('awsCourse_lastViewed');
            return;
        }
        
        setTimeout(() => {
            if (typeof YT !== 'undefined' && YT.Player) {
                openLesson(lastViewed.moduleIndex, lastViewed.lessonIndex);
            } else {
                // Wait for YouTube API to load
                const checkApi = setInterval(() => {
                    if (typeof YT !== 'undefined' && YT.Player) {
                        clearInterval(checkApi);
                        openLesson(lastViewed.moduleIndex, lastViewed.lessonIndex);
                    }
                }, 100);
                // Timeout after 5 seconds
                setTimeout(() => clearInterval(checkApi), 5000);
            }
        }, 500);
    }
});
