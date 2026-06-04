#!/usr/bin/env python3
"""Update videoId='Example' with real YouTube IDs from playlist."""
import re
from pathlib import Path

BASE_DIR = Path("/Users/macbook_345/Documents/learning/AWS/aws-course")
DATA_PATH = BASE_DIR / "data.js"
PLAYLIST_PATH = BASE_DIR / "youtube_playlist.txt"

YT_ID_RE = re.compile(r"\b[A-Za-z0-9_-]{11}\b")

lines = PLAYLIST_PATH.read_text(encoding="utf-8").splitlines()
valid_ids = []
for line in lines:
    m = YT_ID_RE.search(line)
    if m:
        vid_id = m.group(0)
        title = YT_ID_RE.sub("", line).strip()
        valid_ids.append((vid_id, title))

print(f"Extracted {len(valid_ids)} valid video IDs")
if not valid_ids:
    raise SystemExit("No valid IDs found")

# Read data.js
text = DATA_PATH.read_text(encoding="utf-8")

# Replace first N occurrences of Example with real IDs
count = 0
for vid_id, _ in valid_ids:
    old = 'videoId: "Example"'
    new = f'videoId: "{vid_id}"'
    if old in text:
        text = text.replace(old, new, 1)
        count += 1
    if count >= 63:
        break

print(f"Updated {count} lessons")
remaining = text.count('videoId: "Example"')
print(f"Remaining Example placeholders: {remaining}")

DATA_PATH.write_text(text, encoding="utf-8")
print("Done! data.js updated.")
