#!/usr/bin/env python3
"""Rebuild data.js with ALL 236 videos from yt-dlp output."""
import re, json, subprocess
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
OUTPUT_PATH = BASE_DIR / "data.js"

# Fetch using --print to get playlist_index
res = subprocess.run(
    ["python3", "-m", "yt_dlp", "--flat-playlist", "--print", "%(playlist_index)s %(id)s %(title)s",
     "https://www.youtube.com/playlist?list=PL6XT0grm_TfgtwtwUit305qS-HhDvb4du"],
    capture_output=True, text=True, timeout=60
)

# Parse yt-dlp output - format: "001 videoId Title"
videos = []
for line in res.stdout.splitlines():
    line = line.strip()
    if not line:
        continue
    # Format: "001 abcdefghijk Title..."
    parts = line.split(" ", 2)
    if len(parts) >= 2:
        pos_str = parts[0]
        vid_id = parts[1]
        title = parts[2].strip() if len(parts) > 2 else ""
        
        # Skip if vid_id looks like a number (broken entries like "119 1")
        if re.match(r"^\d+$", vid_id):
            continue
        if not re.match(r"^[A-Za-z0-9_-]{11}$", vid_id):
            continue
            
        try:
            pos = int(pos_str)
        except ValueError:
            continue
            
        # Fix broken titles
        if vid_id == "gTWsuYsJ3x8":
            title = "AWS Tutorial 177 - AWS Lambda Hot Start vs Cold Start Explained - Part 2"
        elif vid_id == "UIQ-ZfXMEJE":
            title = "AWS Tutorial 194 - AWS Lambda - Easily Create Events and Test AWS Lambda Functions"
        elif vid_id == "DK5U3HtE9qo":
            title = "AWS Tutorial 203 - AWS Lambda - Reserved Concurrency and Provisioned Concurrency"
            
        videos.append((pos, vid_id, title))

# Sort by position
videos.sort(key=lambda x: x[0])
print(f"Parsed {len(videos)} videos from yt-dlp output")

# Check coverage
positions = [v[0] for v in videos]
missing_pos = sorted(set(range(1, 237)) - set(positions))
print(f"Position range: {min(positions)} - {max(positions)}")
if missing_pos:
    print(f"Missing positions: {missing_pos}")

# Module definitions with actual position ranges
MODULES = [
    (1, "Giới thiệu AWS", "Tổng quan về AWS, điện toán đám mây, và cơ sở hạ tầng toàn cầu", "cloud", 1, 9),
    (2, "Amazon EC2", "Virtual Servers trên AWS - cách tạo, cấu hình và quản lý EC2 instances", "server", 10, 22),
    (3, "EBS & Storage", "Elastic Block Storage - lưu trữ block-level cho EC2, snapshots, và các loại volumes", "database", 23, 38),
    (4, "Load Balancer & Auto Scaling", "ELB, ALB, NLB, Classic LB và Auto Scaling Groups", "activity", 39, 51),
    (5, "IAM - Identity & Access Management", "Quản lý users, groups, roles và policies để kiểm soát truy cập AWS resources", "shield", 52, 59),
    (6, "Amazon S3", "Object storage - lưu trữ và quản lý files với các storage classes khác nhau", "box", 60, 78),
    (7, "CloudFront CDN", "Content Delivery Network - phân phối content toàn cầu với latency thấp", "globe", 79, 89),
    (8, "Amazon VPC", "Virtual Private Cloud - tạo private network trong AWS với subnets, routing, NAT", "shield", 90, 107),
    (9, "Amazon Route 53", "DNS service - quản lý domain, routing policies và health checks", "globe", 108, 132),
    (10, "Amazon RDS", "Managed database service - MySQL, PostgreSQL, Oracle, MariaDB, Aurora", "database", 133, 146),
    (11, "Amazon DynamoDB", "NoSQL database - serverless, fully managed, single-digit millisecond latency", "database", 147, 157),
    (12, "Amazon SES & SNS", "Notifications và Email - Simple Notification Service và Simple Email Service", "mail", 158, 165),
    (13, "CloudWatch", "Monitoring và observability - metrics, logs, alarms, dashboards", "activity", 166, 177),
    (14, "AWS Lambda", "Serverless compute - chạy code không cần servers, trả tiền theo execution", "zap", 178, 203),
    (15, "Amazon API Gateway", "Tạo, deploy và quản lý APIs - REST, HTTP, WebSocket", "globe", 204, 226),
    (16, "Amazon Cognito", "User authentication và authorization - user pools, identity pools, hosted UI", "user", 227, 232),
    (17, "AWS ECS", "Elastic Container Service - container orchestration, Fargate, EKS", "server", 233, 236),
]

# Build position index
pos_map = {pos: (vid, title) for pos, vid, title in videos}

# Extract meaningful part from title
def clean(title: str) -> str:
    t = title.strip()
    
    # Keep everything after "AWS Tutorials - N - " pattern
    m = re.match(r"^AWS\s*Tutorials\s*-\s*\d+\s*-\s*(.+)$", t, flags=re.IGNORECASE)
    if m:
        t = m.group(1).strip()
    else:
        # For titles without the pattern, keep as-is (e.g., module titles)
        pass
    
    # Remove trailing parenthetical suffixes (with flexible whitespace)
    t = re.sub(r"\s*\(\s*[Ii]n\s+[Hh]indi\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*Hindi\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s+in\s+[Hh]indi\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s+Hindi\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s+Tutorials?\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s+Beginner\s+Guide\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*AWS\s+Step\s+By\s+Step\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*2025\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*Must-Know\s+for\s+DevOps\s*\)\s*$", "", t)
    t = re.sub(r"\s*\(\s*[Bb]eginners?\s*\)\s*$", "", t)
    
    t = re.sub(r"\s{2,}", " ", t).strip(" -|")
    return t or "Lesson"

def duration(title: str) -> str:
    t = (title or "").lower()
    if "overview" in t or "introduction" in t or "intro" in t:
        return "12:00"
    if "create" in t or "setup" in t or "how to" in t or "project" in t or "deploy" in t:
        return "15:00"
    if "delete" in t or "cleanup" in t:
        return "8:00"
    if "full" in t or "complete" in t or "step by step" in t:
        return "18:00"
    if "destination" in t:
        return "14:00"
    return "12:00"

# Build data.js
parts = [
    "// Course Data - AWS Tutorials by Gaurav Sharma",
    "// Complete course with all lessons from the YouTube playlist",
    "",
    "const modules = [",
]

total_lessons = 0
missing_count = 0

for mi, (mid, mtitle, mdesc, micon, start, end) in enumerate(MODULES):
    parts += [
        f"    {{",
        f"        id: {mid},",
        f'        title: "{mtitle}",',
        f'        description: "{mdesc}",',
        f'        icon: "{micon}",',
        "        lessons: [",
    ]
    lesson_idx = 0
    for pos in range(start, end + 1):
        if pos in pos_map:
            vid_id, title = pos_map[pos]
            # Skip private videos
            if "[private" in title.lower():
                continue
            lt = clean(title)
            parts += [
                "            {",
                f'                id: "{mid}-{lesson_idx + 1}",',
                f'                title: "{lt}",',
                f'                videoId: "{vid_id}",',
                f'                duration: "{duration(title)}",',
                f'                summary: "Bài học về {lt} trong khóa học AWS.",',
                f'                explanation: `<p>Bài học về {lt}. Xem video để hiểu chi tiết.</p>`',
                "            },",
            ]
            lesson_idx += 1
            total_lessons += 1
        else:
            missing_count += 1
            print(f"  Missing pos {pos} in module {mid} ({mtitle})")
    
    parts += ["        ]", "    }" + ("," if mi < len(MODULES) - 1 else "")]

parts += ["];", "", "if (typeof module !== 'undefined' && module.exports) {", "    module.exports = modules;", "}"]

OUTPUT_PATH.write_text("\n".join(parts), encoding="utf-8")
print(f"\nWritten {total_lessons} lessons ({missing_count} missing)")
