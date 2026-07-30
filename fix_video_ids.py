#!/usr/bin/env python3
"""Map YouTube playlist videos to lessons by title similarity."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Parse playlist videos
lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
playlist = []
for line in lines:
    
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Za-z0-9_-]{11}$", parts[0]):
        vid_id, title = parts[0], parts[1].strip()
        playlist.append((vid_id, title))

print(f"Playlist videos: {len(playlist)}")

# Parse data.js lessons
text = DATA_PATH.read_text(encoding="utf-8")

# Extract all lesson titles and their current videoIds
lesson_pattern = re.compile(
    r'\{\s*id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"'
)
lessons = []
for m in lesson_pattern.finditer(text):
    lesson_id, title, video_id = m.groups()
    lessons.append({"id": lesson_id, "title": title, "videoId": video_id})

print(f"Total lessons: {len(lessons)}")

# Find lessons with "example" videoId
example_lessons = [l for l in lessons if l["videoId"].lower() == "example"]
print(f"Lessons with 'example' videoId: {len(example_lessons)}")

# For each example lesson, try to find matching video by keywords
# Strategy: match keywords between lesson title and video title
for lesson in example_lessons:
    lesson_keywords = set(re.findall(r'\w+', lesson["title"].lower()))
    # Remove common words
    stop_words = {"trong", "và", "của", "là", "cho", "với", "từ", "để", "tại", "các", "cách", "bài", "video", "aws"}
    lesson_keywords -= stop_words
    
    best_match = None
    best_score = 0
    
    for vid_id, vid_title in playlist:
        vid_keywords = set(re.findall(r'\w+', vid_title.lower()))
        vid_keywords -= {"in", "hindi", "aws", "tutorials", "the", "a", "an", "is", "are", "to", "of", "and", "or", "what", "how", "why"}
        
        common = lesson_keywords & vid_keywords
        score = len(common)
        
        if score > best_score:
            best_score = score
            best_match = vid_id
    
    if best_match and best_score >= 1:
        lesson["new_videoId"] = best_match
        print(f"  {lesson['id']}: '{lesson['title']}' -> {best_match} (score: {best_score})")
    else:
        print(f"  WARNING: No match for {lesson['id']}: '{lesson['title']}'")

# Now update data.js
update_count = 0
for lesson in example_lessons:
    if "new_videoId" in lesson:
        old = f'id: "{lesson["id"]}"\n                title: "{lesson["title"]}"\n                videoId: "example"'
        new = f'id: "{lesson["id"]}"\n                title: "{lesson["title"]}"\n                videoId: "{lesson["new_videoId"]}"'
        
        if old in text:
            text = text.replace(old, new, 1)
            update_count += 1
        else:
            # Try case-insensitive
            old_ci = f'videoId: "example"'
            # Find the specific occurrence for this lesson
            pattern = rf'(id:\s*"{re.escape(lesson["id"])}"[^}}]*?videoId:\s*")(example)(")'
            replacement = rf'\1{lesson["new_videoId"]}\3'
            new_text, n = re.subn(pattern, replacement, text, count=1)
            if n > 0:
                text = new_text
                update_count += 1
                print(f"  Updated {lesson['id']} via regex")

print(f"\nUpdated {update_count} lessons")
DATA_PATH.write_text(text, encoding="utf-8")
print("Done!")
