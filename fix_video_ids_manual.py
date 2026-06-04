#!/usr/bin/env python3
"""Update videoIds based on video number matching."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Build playlist index by video number
playlist_by_num = {}
lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
for line in lines:
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Za-z0-9_-]{11}$", parts[0]):
        vid_id = parts[0]
        vid_title = parts[1].strip()
        m = re.match(r"AWS Tutorials?\s*-\s*(\d+)", vid_title)
        if m:
            num = int(m.group(1))
            playlist_by_num[num] = vid_id

print(f"Playlist videos indexed by number: {len(playlist_by_num)}")

# Manual mapping for lessons that don't have a clear number match
# Based on lesson content and YouTube video titles
manual_mapping = {
    # Module 1: Introduction
    "1-1": "rKNSc8RrwxA",  # Video 1: Playlist intro
    "1-2": "JuE9gKNs5sA",  # Video 2: What is AWS
    "1-3": "zr48J9Xhaw4",  # Video 3: Service Models
    "1-4": "OmfUnOYKxIg",  # Video 4: Deployment Models
    "1-5": "NgI_Jkm7RRE",  # Video 5: AWS Pricing
    "1-6": "jRGW4uInhkE",  # Video 6: AWS Region
    "1-7": "fH5828qH4_k",  # Video 7: Availability Zones
    "1-8": "WF5XS6jOUZ0",  # Video 8: Local Zones
    "1-9": "QDymcZ5xYow",  # Video 9: Create AWS Account
    
    # Module 2: EC2
    "2-1": "f-T4xWUZWSk",  # Video 10: Create First EC2 Instance
    "2-2": "HPrq6kdsEZ0",  # Video 11: Access EC2 from Windows
    "2-3": "8Vuvl4cvdv4",  # Video 12: Access EC2 from Linux
    "2-4": "HaRki0xPPd4",  # Video 13: Install Nginx
    "2-5": "EXs775-J5zE",  # Video 14: Bootstrap Script
    "2-6": "poAvpknMDwI",  # Video 15: Security Group
    "2-7": "nA96hTiakb8",  # Video 16: EC2 Instance Types
    "2-8": "wFf8Er1tz_0",  # Video 17: EC2 Pricing
    "2-9": "CEyj_YGNvNM",  # Video 18: Create Windows Instance
    "2-10": "TEUAsbB9bwU",  # Video 19: Instance Metadata
    "2-11": "5oZEJMZpZDs",  # Video 21: Elastic IP
    
    # Module 3: EBS
    "3-1": "9OpRBa0CNRw",  # Video 23: EBS Overview
    "3-2": "d6c6S_vICvs",  # Video 24: Create EBS Volume
    "3-3": "JwEyueilFb4",  # Video 25/26: Resize EBS
    "3-4": "1eUU1SybgQg",  # Video 30: Snapshots
    "3-5": "x2T5egBIdQg",  # Video 37: AMI
    
    # Module 4: Load Balancer & Auto Scaling
    "4-1": "tBhoVGT7a18",  # Video 39: Classic LB
    "4-2": "IUK7OXXVQFM",  # Video 42: Application LB
    "4-3": "jkK29xGhQZo",  # Video 46: Auto Scaling
    "4-4": "E2I4GT-AqHY",  # Video 47/48: Auto Scaling with LB
    
    # Module 5: IAM
    "5-1": "3Ys2SjowSts",  # Video 59: S3 Overview (intro)
    "5-2": "3UAjLVGr-xg",  # Video 52: IAM Groups
    "5-3": "B1PpTEfVDw4",  # Video 53: Password Policy
    "5-4": "A2Bc5dOwx_c",  # Video 54: MFA
    "5-5": "nooY45x12Qw",  # Video 55: AWS CLI
    "5-6": "vVIgGvp1Xbg",  # Video 51: IAM Overview
    
    # Module 6: S3
    "6-1": "rrUA7jY_Cw8",  # Video 59: S3 Overview
    "6-2": "MwFH65uTMXw",  # Video 60: Create Bucket
    "6-3": "nzEsMgAfo6U",  # Video 63: Versioning
    "6-4": "Y6infh4tL_Q",  # Video 64: Host Static Website
    "6-5": "KoKBhXhQe60",  # Video 70: Storage Classes
    "6-6": "s3gMJU9Nc7U",  # Video 72: Lifecycle
    "6-7": "5e4FlaHUPgY",  # Video 74: CORS
    
    # Module 7: CloudFront
    "7-1": "AjlUFYnScBk",  # Video 77: CloudFront Overview
    "7-2": "vL1Eix6s_Pg",  # Video 78: Invalidation
    "7-3": "R-BiyXJumr8",  # Video 80: CloudFront with S3
    
    # Module 8: Route 53
    "8-1": "GETj1PdFVYs",  # Video 89: Route 53 Overview
    "8-2": "AkQKC-3COl4",  # Video 90: Routing Policies
    "8-3": "R-BiyXJumr8",  # Video 92: Public/Private Subnet (best match)
    
    # Module 9: RDS
    "9-1": "AcM8KQWR3S4",  # Video 144: RDS Overview
    "9-2": "KP6XRtyVVX4",  # Video 20: Access Windows (placeholder - need real RDS video)
    "9-3": "MPglvFh-l7M",  # Video 143: Cross Region Read Replica
    "9-4": "C27KFj051z4",  # Video 139: Aurora
    
    # Module 10: DynamoDB
    "10-1": "PoJ2I2NAe34",  # Video 144: DynamoDB Overview
    "10-2": "1IJtgCn6jsg",  # Video 148: Global Secondary Index
    
    # Module 11: Lambda - need to verify these
    # Module 12: API Gateway - need to verify
    # Module 13: Cognito - need to verify
    # Module 14: CloudWatch - need to verify
    # Module 15: SNS & SES - need to verify
    # Module 16: ECS - need to verify
}

# Read data.js
text = DATA_PATH.read_text(encoding="utf-8")

# Update each lesson
updated = 0
for lesson_id, new_vid in manual_mapping.items():
    # Find and replace the videoId for this lesson
    pattern = rf'(id:\s*"{re.escape(lesson_id)}"[^}}]*?videoId:\s*")([^"]+)(")'
    replacement = rf'\1{new_vid}\3'
    new_text, count = re.subn(pattern, replacement, text, count=1)
    if count > 0:
        text = new_text
        updated += 1
        print(f"✓ Updated {lesson_id} -> {new_vid}")
    else:
        print(f"✗ Not found: {lesson_id}")

print(f"\nUpdated {updated} lessons")
DATA_PATH.write_text(text, encoding="utf-8")
print("Done!")
