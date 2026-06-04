#!/usr/bin/env python3
"""Deep check: compare lesson titles against YouTube video titles."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Parse playlist
lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
playlist = []
for line in lines:
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Za-z0-9_-]{11}$", parts[0]):
        vid_id, title = parts[0], parts[1].strip()
        playlist.append((vid_id, title))

# Normalize text for matching
def normalize(s):
    s = s.lower()
    # Extract number at start if any
    m = re.search(r'\d+', s)
    num = m.group(0) if m else ""
    # Remove common noise
    words = re.findall(r'\w+', s)
    noise = {
        'aws', 'tutorials', 'in', 'hindi', 'the', 'a', 'an', 'is', 'are',
        'to', 'of', 'and', 'or', 'what', 'how', 'why', 'for', 'with',
        'aws', 'amazon', 'your', 'you', 'first', 'create', 'how', 'to'
    }
    words = [w for w in words if w not in noise]
    return num, frozenset(words), s

def similarity(lesson_norm, vid_norm):
    num1, words1, raw1 = lesson_norm
    num2, words2, raw2 = vid_norm
    common = words1 & words2
    # Bonus if same number at start
    num_bonus = 10 if num1 and num1 == num2 else 0
    # Length penalty for very different lengths
    len_penalty = 0 if abs(len(raw1) - len(raw2)) < 40 else 2
    return len(common) * 2 + num_bonus - len_penalty

# Extract all lessons from data.js
text = DATA_PATH.read_text(encoding="utf-8")

# Find all lesson blocks
lesson_blocks = re.findall(
    r'id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"',
    text
)

print(f"Total lessons found: {len(lesson_blocks)}")
print("=" * 100)

issues = []
updates = []

for lesson_id, lesson_title, current_vid in lesson_blocks:
    norm_lesson = normalize(lesson_title)
    
    # Find best matching video
    best_score = 0
    best_match = None
    for vid_id, vid_title in playlist:
        score = similarity(norm_lesson, normalize(vid_title))
        if score > best_score:
            best_score = score
            best_match = (vid_id, vid_title)
    
    if best_match:
        vid_id, vid_title = best_match
        if current_vid != vid_id or best_score < 3:
            issues.append((lesson_id, lesson_title, current_vid, vid_id, vid_title, best_score))
            updates.append((lesson_id, lesson_title, current_vid, vid_id))

print(f"\nPotential mismatches (score < 3 or ID differs): {len(issues)}")
print("=" * 100)
for lesson_id, lesson_title, curr, expected, vid_title, score in issues[:30]:
    match_str = "MISMATCH" if curr != expected else "LOW CONF"
    print(f"[{match_str}] {lesson_id}: {lesson_title}")
    print(f"  Current: {curr}")
    print(f"  Expected: {expected} ({vid_title[:80]}) [score: {score}]")
    print()

if len(issues) > 30:
    print(f"... and {len(issues) - 30} more")
