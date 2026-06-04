#!/usr/bin/env python3
"""Match lessons to YouTube videos intelligently."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Parse playlist - build index by video number and by keywords
playlist_by_num = {}  # video number -> (id, title)
playlist_by_keyword = {}  # keyword -> list of (id, title, num)

lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
for line in lines:
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Za-z0-9_-]{11}$", parts[0]):
        vid_id = parts[0]
        vid_title = parts[1].strip()
        
        # Extract video number from title
        m = re.match(r"AWS Tutorials?\s*-\s*(\d+)", vid_title)
        if m:
            num = int(m.group(1))
            playlist_by_num[num] = (vid_id, vid_title)
            
            # Index by keywords
            words = set(re.findall(r'\w+', vid_title.lower()))
            noise = {'aws', 'tutorials', 'in', 'hindi', 'the', 'a', 'an', 'is', 'are',
                    'to', 'of', 'and', 'or', 'what', 'how', 'why', 'for', 'with',
                    'amazon', 'your', 'you', 'first', 'create', 'service', 'using'}
            keywords = words - noise
            for kw in keywords:
                if kw not in playlist_by_keyword:
                    playlist_by_keyword[kw] = []
                playlist_by_keyword[kw].append((vid_id, vid_title, num))

print(f"Playlist videos indexed: {len(playlist_by_num)}")
print(f"Keywords indexed: {len(playlist_by_keyword)}")

# Parse lessons from data.js
text = DATA_PATH.read_text(encoding="utf-8")
lessons = re.findall(
    r'id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"',
    text
)

print(f"Lessons found: {len(lessons)}")
print()

# Matching strategy:
# 1. Try to extract number from lesson title and match with video number
# 2. Use keyword matching as fallback

def extract_number(title):
    """Extract the first number from title."""
    m = re.search(r'\d+', title)
    return int(m.group(0)) if m else None

def match_lesson_to_video(lesson_title, current_vid, used_videos):
    """Find best matching video for a lesson."""
    lesson_num = extract_number(lesson_title)
    
    # Strategy 1: Match by video number
    if lesson_num and lesson_num in playlist_by_num:
        vid_id, vid_title = playlist_by_num[lesson_num]
        if vid_id not in used_videos:
            return vid_id, vid_title, f"number match ({lesson_num})"
    
    # Strategy 2: Keyword matching
    lesson_words = set(re.findall(r'\w+', lesson_title.lower()))
    noise = {'trong', 'và', 'của', 'là', 'cho', 'với', 'từ', 'để', 'tại', 'các', 'cách',
            'bài', 'video', 'aws', 'amazon', 'tập', 'về', 'như', 'khi', 'nên', 'có'}
    lesson_keywords = lesson_words - noise
    
    best_match = None
    best_score = 0
    
    for kw in lesson_keywords:
        if kw in playlist_by_keyword:
            for vid_id, vid_title, vid_num in playlist_by_keyword[kw]:
                if vid_id in used_videos:
                    continue
                score = 1
                # Bonus for matching number
                if lesson_num and vid_num == lesson_num:
                    score += 10
                if score > best_score:
                    best_score = score
                    best_match = (vid_id, vid_title, f"keyword '{kw}' + num match")
    
    if best_match:
        return best_match
    
    # Strategy 3: Broader keyword match
    for kw in lesson_keywords:
        if kw in playlist_by_keyword:
            for vid_id, vid_title, vid_num in playlist_by_keyword[kw]:
                if vid_id not in used_videos:
                    return vid_id, vid_title, f"keyword '{kw}'"
    
    return None, None, "no match"

# Process all lessons
used_videos = set()
mapping = {}
unmatched = []

for lesson_id, lesson_title, current_vid in lessons:
    vid_id, vid_title, reason = match_lesson_to_video(lesson_title, current_vid, used_videos)
    
    if vid_id:
        mapping[lesson_id] = (vid_id, vid_title, reason)
        used_videos.add(vid_id)
        status = "CHANGED" if vid_id != current_vid else "OK"
        print(f"[{status}] {lesson_id}: '{lesson_title[:50]}' -> {vid_id} ({reason})")
    else:
        unmatched.append((lesson_id, lesson_title, current_vid))
        print(f"[UNMATCHED] {lesson_id}: '{lesson_title[:50]}'")

print(f"\nMapped: {len(mapping)}/{len(lessons)}")
print(f"Unmatched: {len(unmatched)}")

if unmatched:
    print("\nUnmatched lessons:")
    for lesson_id, lesson_title, current_vid in unmatched:
        print(f"  {lesson_id}: {lesson_title}")
