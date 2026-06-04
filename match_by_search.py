#!/usr/bin/env python3
"""Match lessons to YouTube videos by searching."""
import re
import subprocess
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

# Parse playlist
lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
playlist = {}
for line in lines:
    parts = line.split(" ", 1)
    if len(parts) == 2 and re.match(r"^[A-Za-z0-9_-]{11}$", parts[0]):
        vid_id, title = parts[0], parts[1].strip()
        playlist[vid_id] = title

# Parse lessons
text = DATA_PATH.read_text(encoding="utf-8")
lessons = re.findall(
    r'id:\s*"([^"]+)"\s*,\s*title:\s*"([^"]+)"\s*,\s*videoId:\s*"([^"]+)"',
    text
)

print(f"Playlist: {len(playlist)} videos")
print(f"Lessons: {len(lessons)}")
print()

# For each lesson, search YouTube and find matching video
mapping = {}

for lesson_id, lesson_title, current_vid in lessons[:10]:  # Test with first 10
    # Search for the lesson title on YouTube
    search_query = f"AWS Tutorials {lesson_title}"
    
    try:
        result = subprocess.run(
            ["python3", "-m", "yt_dlp", 
             "--flat-playlist",
             "--print", "%(id)s %(title)s",
             f"ytsearch5:{search_query}"],
            capture_output=True, text=True, timeout=30
        )
        
        if result.returncode == 0:
            # Find best match from playlist
            best_match = None
            best_score = 0
            
            for line in result.stdout.strip().split("\n"):
                parts = line.split(" ", 1)
                if len(parts) == 2:
                    vid_id = parts[0]
                    vid_title = parts[1]
                    
                    # Check if this video is in our playlist
                    if vid_id in playlist:
                        # Simple keyword matching
                        lesson_words = set(re.findall(r'\w+', lesson_title.lower()))
                        vid_words = set(re.findall(r'\w+', vid_title.lower()))
                        
                        common = lesson_words & vid_words
                        score = len(common)
                        
                        if score > best_score:
                            best_score = score
                            best_match = vid_id
            
            if best_match and best_score >= 1:
                mapping[lesson_id] = best_match
                print(f"✓ {lesson_id}: '{lesson_title[:50]}' -> {best_match}")
            else:
                print(f"✗ {lesson_id}: '{lesson_title[:50]}' - No good match")
        else:
            print(f"✗ {lesson_id}: Search failed")
    except Exception as e:
        print(f"✗ {lesson_id}: Error - {e}")
