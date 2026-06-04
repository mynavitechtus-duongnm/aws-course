#!/usr/bin/env python3
"""Count lessons and unique videoIds."""
import re
from pathlib import Path

text = Path("/Users/macbook_345/Documents/learning/AWS/aws-course/data.js").read_text()
lessons = re.findall(r'id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"', text)
print(f"Total lessons: {len(lessons)}")

unique_ids = set(vid for _, _, vid in lessons)
print(f"Unique videoIds: {len(unique_ids)}")

# Show all unique videoIds
for vid in sorted(unique_ids):
    print(f"  {vid}")

# Count by videoId
from collections import Counter
counts = Counter(vid for _, _, vid in lessons)
print("\nMost used videoIds:")
for vid, count in counts.most_common(10):
    print(f"  {vid}: {count} times")
