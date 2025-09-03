import os
import time
import json
import requests
from django.conf import settings
from pathlib import Path


MAX_ANIME = 4000
LIMIT = 50
DELAY = 10


def fetch_and_cache_anime():
    from django.conf import settings
    CACHE_FILE = Path(settings.BASE_DIR) / "anime_cache.json"

    anime_list = []
    seen_ids = set()
    offset = 0

    while len(anime_list) < MAX_ANIME:
        url = f"https://api.myanimelist.net/v2/anime/ranking?ranking_type=tv&limit={LIMIT}&offset={offset}"
        headers = {"X-MAL-CLIENT-ID": settings.MAL_CLIENT_ID}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"failed request at offset {offset}. status {response.status_code}")
                offset += LIMIT
                time.sleep(DELAY)
                continue


            data = response.json()
            page_added = 0

            for item in data.get("data", []):
                node = item["node"]


                if "season" in node["title"].lower():
                    continue

                anime_entry = {
                    "id": node["id"],
                    "title": node["title"],
                    "main_picture": node.get("main_picture"),
                    "type": node.get("type")
                }

                if node["id"] not in seen_ids:
                    anime_list.append(anime_entry)
                    seen_ids.add(node["id"])
                    page_added += 1

                if len(anime_list) >= MAX_ANIME:
                    break

            print(f"Offset {offset}: added {page_added} TV anime (total: {len(anime_list)})")

            offset += LIMIT

            if "paging" not in data or "next" not in data["paging"]:
                break

            time.sleep(DELAY)
        except Exception as e:
            print(f"Exception occurred at offset {offset}: {e}")
            offset += LIMIT
            time.sleep(DELAY)
            continue

    if anime_list:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(anime_list, f, ensure_ascii=False, indent=2)
        print(f"Successfully cached {len(anime_list)} anime to {CACHE_FILE}")
    else:
        print("No anime fetched, no changes made")

