#!/usr/bin/env python3
"""Compare current videoIds with expected ones."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Build playlist index
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
            playlist_by_num[num] = (vid_id, vid_title)

# Expected mapping based on lesson order
expected_mapping = {
    # Module 1: Introduction (videos 1-9)
    "1-1": 1, "1-2": 2, "1-3": 3, "1-4": 4, "1-5": 5,
    "1-6": 6, "1-7": 7, "1-8": 8, "1-9": 9,
    
    # Module 2: EC2 (videos 10-21)
    "2-1": 10, "2-2": 11, "2-3": 12, "2-4": 13, "2-5": 14,
    "2-6": 15, "2-7": 16, "2-8": 17, "2-9": 18, "2-10": 19, "2-11": 21,
    
    # Module 3: EBS (videos 22-29, 30-37)
    "3-1": 23, "3-2": 24, "3-3": 26, "3-4": 30, "3-5": 37,
    
    # Module 4: Load Balancer & Auto Scaling (videos 39-48)
    "4-1": 39, "4-2": 42, "4-3": 46, "4-4": 48,
    
    # Module 5: IAM (videos 51-58)
    "5-1": 59, "5-2": 52, "5-3": 53, "5-4": 54, "5-5": 55, "5-6": 51,
    
    # Module 6: S3 (videos 59-75)
    "6-1": 59, "6-2": 60, "6-3": 63, "6-4": 64, "6-5": 70, "6-6": 72, "6-7": 74,
    
    # Module 7: CloudFront (videos 77-87)
    "7-1": 77, "7-2": 78, "7-3": 80,
    
    # Module 8: Route 53 (videos 88-93)
    "8-1": 89, "8-2": 90, "8-3": 92,
    
    # Module 9: RDS (videos 144-145)
    "9-1": 144, "9-2": 145, "9-3": 143, "9-4": 139,
    
    # Module 10: DynamoDB (videos 144-155)
    "10-1": 144, "10-2": 148,
    
    # Module 11: Lambda (videos 172-196)
    "11-1": 172, "11-2": 172, "11-3": 176, "11-4": 182, "11-5": 188,
    
    # Module 12: API Gateway
    "12-1": 200, "12-2": 201, "12-3": 203, "12-4": 208,
    
    # Module 13: Cognito
    "13-1": 226, "13-2": 226,
    
    # Module 14: CloudWatch
    "14-1": 161, "14-2": 163, "14-3": 167,
    
    # Module 15: SNS & SES
    "15-1": 158, "15-2": 155,
    
    # Module 16: ECS
    "16-1": 233, "16-2": 233,
}

# Read current lessons
text = DATA_PATH.read_text(encoding="utf-8")
lessons = re.findall(
    r'id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"',
    text
)

print("Current vs Expected videoIds:")
print("=" * 100)
mismatches = 0
for lesson_id, lesson_title, current_vid in lessons:
    if lesson_id in expected_mapping:
        expected_num = expected_mapping[lesson_id]
        if expected_num in playlist_by_num:
            expected_vid, expected_title = playlist_by_num[expected_num]
            if current_vid != expected_vid:
                mismatches += 1
                print(f"[MISMATCH] {lesson_id}: {lesson_title[:50]}")
                print(f"  Current: {current_vid}")
                print(f"  Expected: {expected_vid} (Video {expected_num}: {expected_title[:60]})")
                print()

print(f"\nTotal mismatches: {mismatches}/{len(lessons)}")
