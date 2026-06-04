#!/usr/bin/env python3
"""Update all remaining lessons with keyword-based summaries"""

with open('data.js', 'r') as f:
    content = f.read()

import re

# Get all remaining placeholder summaries
pattern = r'summary: "Bài học về ([^"]+) trong khóa học AWS\."'
matches = re.findall(pattern, content)

print(f"Found {len(matches)} remaining lessons")

# Generic summaries by keyword
generics = {
    "VPN": "Site-to-Site VPN ket noi on-prem voi AWS.",
    "Egress": "Egress Only Internet Gateway cho IPv6.",
    "Hybrid DNS": "Hybrid DNS cau hinh on-prem va AWS.",
    "Endpoint": "VPC Endpoints de truy cap AWS services.",
    "Notification": "SNS notification den HTTP/HTTPS endpoints.",
    "Dashboard": "CloudWatch Dashboard hien thi metrics.",
    "Log": "CloudWatch Logs de centralize logging.",
    "Insights": "CloudWatch Logs Insights query logs.",
    "Reserved Concurrency": "Lambda reserved va provisioned concurrency.",
    "SNS": "SNS notification service.",
    "CloudWatch": "CloudWatch monitoring va logging.",
    "Lambda": "Lambda serverless functions.",
    "Site to Site": "Site-to-Site VPN.",
    "VPC": "VPC networking."
}

count = 0
for lesson_title in matches:
    new_summary = None
    
    # Find matching keyword
    for keyword, summary in generics.items():
        if keyword.lower() in lesson_title.lower():
            new_summary = summary
            break
    
    if not new_summary:
        # Use generic summary
        new_summary = "Tim hieu bai hoc nay tren AWS."
    
    # Replace
    old = f'summary: "Bài học về {lesson_title} trong khóa học AWS."'
    new = f'summary: "{new_summary}"'
    
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"Updated: {lesson_title[:40]}...")
        
        # Also update explanation
        old_exp = f'explanation: `<p>Bài học về {lesson_title}. Xem video để hiểu chi tiết.</p>`'
        new_exp = f'explanation: `<p>{new_summary} Xem video de hieu them.</p>`'
        if old_exp in content:
            content = content.replace(old_exp, new_exp)

with open('data.js', 'w') as f:
    f.write(content)

print(f"\nTotal updated: {count} lessons")
