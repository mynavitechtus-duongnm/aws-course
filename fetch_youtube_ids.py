#!/usr/bin/env python3
"""Extract YouTube video IDs and titles from a playlist."""
import re
import sys
import urllib.request

PLAYLIST_URL = (
    "https://www.youtube.com/playlist?list=PL6XT0grm_TfgtwtwUit305qS-HhDvb4du"
)


def fetch_playlist_page(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_videos(html: str):
    pattern = re.compile(
        r'"videoId":"([^"]+)",\s*"title":\{"runs":\[\{"text":"([^"]+)"\}\}\]'
    )
    seen = []
    for vid_id, title in pattern.findall(html):
        if vid_id not in {v for v, _ in seen}:
            seen.append((vid_id, title))
    return seen


def main():
    print(f"Đang tải playlist: {PLAYLIST_URL}")
    html = fetch_playlist_page(PLAYLIST_URL)
    videos = extract_videos(html)
    if not videos:
        print("Không tìm thấy video nào. Có thể YouTube đã chặn truy cập.")
        sys.exit(1)

    print(f"Tìm thấy {len(videos)} video.\n")
    print("=" * 90)
    print(f"{'#':<5} {'videoId':<12} {'title'}")
    print("=" * 90)
    for idx, (vid_id, title) in enumerate(videos, 1):
        print(f"{idx:<5} {vid_id:<12} {title}")

    out_path = "/Users/macbook_345/Documents/learning/AWS/aws-course/youtube_ids.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        for idx, (vid_id, title) in enumerate(videos, 1):
            f.write(f"{idx}\t{vid_id}\t{title}\n")
    print(f"\nĐã lưu danh sách video vào: {out_path}")


if __name__ == "__main__":
    main()
