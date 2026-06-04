#!/usr/bin/env python3
"""Update data.js with correct videoIds from smart_match.py output."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"

# Read current data.js
text = DATA_PATH.read_text(encoding="utf-8")

# Mapping based on smart_match.py analysis
# Format: lesson_id -> new_videoId
mapping = {
    # Module 1: Introduction - all correct
    "1-1": "rKNSc8RrwxA",
    "1-2": "JuE9gKNs5sA",
    "1-3": "zr48J9Xhaw4",
    "1-4": "OmfUnOYKxIg",
    "1-5": "NgI_Jkm7RRE",
    "1-6": "jRGW4uInhkE",
    "1-7": "fH5828qH4_k",
    "1-8": "WF5XS6jOUZ0",
    "1-9": "QDymcZ5xYow",
    
    # Module 2: EC2
    "2-1": "f-T4xWUZWSk",
    "2-2": "HPrq6kdsEZ0",
    "2-3": "8Vuvl4cvdv4",
    "2-4": "HaRki0xPPd4",
    "2-5": "EXs775-J5zE",
    "2-6": "poAvpknMDwI",
    "2-7": "nA96hTiakb8",
    "2-8": "wFf8Er1tz_0",
    "2-9": "CEyj_YGNvNM",
    "2-10": "TEUAsbB9bwU",
    "2-11": "5oZEJMZpZDs",
    
    # Module 3: EBS
    "3-1": "9OpRBa0CNRw",
    "3-2": "d6c6S_vICvs",
    "3-3": "JwEyueilFb4",
    "3-4": "1eUU1SybgQg",
    "3-5": "x2T5egBIdQg",
    
    # Module 4: Load Balancer & Auto Scaling
    "4-1": "tBhoVGT7a18",
    "4-2": "IUK7OXXVQFM",
    "4-3": "jkK29xGhQZo",
    "4-4": "E2I4GT-AqHY",
    
    # Module 5: IAM
    "5-1": "3Ys2SjowSts",
    "5-2": "3UAjLVGr-xg",
    "5-3": "B1PpTEfVDw4",
    "5-4": "A2Bc5dOwx_c",
    "5-5": "nooY45x12Qw",
    "5-6": "vVIgGvp1Xbg",
    
    # Module 6: S3
    "6-1": "rrUA7jY_Cw8",
    "6-2": "MwFH65uTMXw",
    "6-3": "nzEsMgAfo6U",
    "6-4": "Y6infh4tL_Q",
    "6-5": "KoKBhXhQe60",
    "6-6": "s3gMJU9Nc7U",
    "6-7": "5e4FlaHUPgY",
    
    # Module 7: CloudFront
    "7-1": "AjlUFYnScBk",
    "7-2": "vL1Eix6s_Pg",
    "7-3": "R-BiyXJumr8",
    
    # Module 8: Route 53
    "8-1": "GETj1PdFVYs",
    "8-2": "AkQKC-3COl4",
    "8-3": "R-BiyXJumr8",
    
    # Module 9: RDS
    "9-1": "o98frpNl6cs",
    "9-2": "KP6XRtyVVX4",
    "9-3": "MPglvFh-l7M",
    "9-4": "C27KFj051z4",
    
    # Module 10: DynamoDB
    "10-1": "PoJ2I2NAe34",
    "10-2": "1IJtgCn6jsg",
    
    # Module 11: Lambda - using best matches
    "11-1": "lKSCAVp_vNg",
    "11-2": "lKSCAVp_vNg",
    "11-3": "Nbk6EGVzNL8",
    "11-4": "69NwOxAJOEw",
    "11-5": "7r1r3M7ZCvo",
    
    # Module 12: API Gateway
    "12-1": "Ji8oT2QI9Z8",
    "12-2": "0ikAN6d5ZZ0",
    "12-3": "bSL-SMfjMJU",
    "12-4": "qUfqpNb1SLA",
    
    # Module 13: Cognito
    "13-1": "pxtKDujnZnU",
    "13-2": "pxtKDujnZnU",
    
    # Module 14: CloudWatch
    "14-1": "DD21R8SB9vk",
    "14-2": "z4RL_qzSje8",
    "14-3": "5prSZdGcSQc",
    
    # Module 15: SNS & SES
    "15-1": "gz0dphCEK2s",
    "15-2": "O8lzXZ_WlEc",
    
    # Module 16: ECS
    "16-1": "_4RvUXy2qjI",
    "16-2": "Hu4jep_43Zk",
}

# Update data.js
updated = 0
for lesson_id, new_vid in mapping.items():
    pattern = rf'(id:\s*"{re.escape(lesson_id)}"[^}}]*?videoId:\s*")([^"]+)(")'
    def make_replacement(vid):
        return lambda m: m.group(1) + vid + m.group(3)
    new_text, count = re.subn(pattern, make_replacement(new_vid), text, count=1)
    if count > 0:
        text = new_text
        updated += 1
        print(f"OK {lesson_id} -> {new_vid}")
    else:
        print(f"-- Not found: {lesson_id}")

print(f"\nUpdated {updated} lessons")
DATA_PATH.write_text(text, encoding="utf-8")
print("Done!")
