# Hacker News to Telegram Bot

A lightweight bot that fetches the latest story from [Hacker News](https://news.ycombinator.com/) and sends it to a Telegram chat.

> Personal project, running on AWS Lambda, triggered every 5 minutes via EventBridge.

## Deployment

Built for **AWS Lambda** using the `build.ps1` script:

- Installs dependencies in `package/`
- Copies `main.py`
- Zips everything into `bot.zip` for deployment

Triggering is handled by **EventBridge** (every 5 minutes).

## Environment Variables (`.env`)

Create a `.env` file with the following content:

```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

## Requirements

```text
requests==2.32.3
python-dotenv==1.0.1
python-telegram-bot==20.7
```

## Local Execution

You can run the bot locally for testing:

```bash
python main.py
```

## Notes

- The last_id.txt file is stored in /tmp, which works well within AWS Lambda's environment.
- The project is simple and was built mainly for learning and fun. Feel free to customize or extend it.
