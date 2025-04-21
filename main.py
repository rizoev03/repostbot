import os
import requests
import asyncio
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

LAST_ID_PATH = "/tmp/last_id.txt"  

def get_last_posted_id():
    try:
        with open(LAST_ID_PATH, "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return None

def save_last_posted_id(story_id):
    with open(LAST_ID_PATH, "w") as f:
        f.write(str(story_id))

def get_latest_stories():
    url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    response = requests.get(url)
    return response.json() if response.ok else []

def get_story_details(story_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url)
    return response.json() if response.ok else None

async def post_to_telegram(title, url):
    bot = Bot(token=os.getenv("7876957892:AAFUi1CUjc6ikY6yQal3yfyMDvI-Ql6h0Ys")) 
    chat_id = os.getenv("-1002595201491")
    message = f"{title}\n{url}"
    await bot.send_message(chat_id=chat_id, text=message)
    print("Sent to Telegram:", message)

async def run_bot():
    last_post_id = get_last_posted_id()
    latest_news = get_latest_stories()

    for story_id in latest_news:
        if last_post_id and story_id <= last_post_id:
            continue

        story = get_story_details(story_id)
        if not story or story.get("type") != "story" or "url" not in story:
            continue

        await post_to_telegram(story["title"], story["url"])
        save_last_posted_id(story_id)
        break

if __name__ == "__main__":
    asyncio.run(run_bot())

def handler(event=None, context=None):
    asyncio.run(run_bot())
