# 🤖 Reddit Keyword Bot

A Python bot that monitors Reddit in real-time for specific keywords and automatically replies to matching comments + sends instant Telegram notifications.

Built for tracking **jobs/internships**, **India news**, and **programming discussions** across r/all.

---

## ✨ Features

- 🔍 **Real-time monitoring** — watches Reddit 24/7 using PRAW's stream API
- 💬 **Auto-reply** — replies to matching comments with helpful resources
- 📲 **Telegram alerts** — instant notification on your phone when a keyword is found
- 📁 **CSV logging** — saves every match with timestamp, author, subreddit, and link
- 🛡️ **No double replies** — tracks replied comment IDs so it never replies twice
- ⚙️ **Easy config** — change keywords, subreddit, and messages in one file

---

## 📂 Project Structure

```
reddit-keyword-bot/
│
├── bot.py              # Main bot script
├── config.py           # Your credentials and keywords (not pushed to GitHub)
├── config.sample.py    # Template config — copy and rename to config.py
├── requirements.txt    # Python dependencies
├── replied.txt         # Auto-generated: tracks replied comment IDs
├── matches_log.csv     # Auto-generated: log of all keyword matches
└── .gitignore          # Keeps sensitive files out of GitHub
```

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/reddit-keyword-bot.git
cd reddit-keyword-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Reddit API credentials
1. Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **"Create App"**
3. Choose type: **script**
4. Copy your `client_id` and `client_secret`

### 4. Get Telegram Bot credentials
1. Open Telegram → search **@BotFather**
2. Send `/newbot` → follow steps → copy your **bot token**
3. Search **@userinfobot** → send any message → copy your **chat ID**

### 5. Configure the bot
```bash
cp config.sample.py config.py
```
Open `config.py` and fill in all your credentials.

### 6. Run the bot!
```bash
python bot.py
```

---

## ⚙️ Configuration

Open `config.py` to customize:

```python
# Monitor all of Reddit or a specific subreddit
SUBREDDIT = "all"

# Add/remove keywords per category
KEYWORD_GROUPS = {
    "jobs": ["internship", "hiring", "fresher", ...],
    "india_news": ["india", "modi", "upsc", ...],
    "programming": ["python vs", "coding meme", ...]
}
```

---

## 📲 Telegram Notification Example

When a keyword is found, you get a message like:

```
🔔 Reddit Bot Alert!

📂 Category: jobs
🔑 Keyword: internship
👤 User: u/some_user
📌 Subreddit: r/india
🔗 View Comment
```

---

## 📋 CSV Log Example

| Timestamp | Category | Keyword | Author | Subreddit | URL |
|---|---|---|---|---|---|
| 2024-01-15 10:23:45 | jobs | internship | u/dev_guy | r/india | reddit.com/... |
| 2024-01-15 10:31:12 | programming | python vs | u/coder99 | r/programming | reddit.com/... |

---

## ⚠️ Important Notes

- **Don't spam** — Reddit bans bots that reply too aggressively. The bot has a 0.5s delay built in.
- **Keep config.py private** — it's in `.gitignore` for a reason. Never push your credentials.
- **Reddit rules** — make sure auto-replies follow the subreddit rules you're monitoring.
- **Rate limits** — PRAW handles Reddit's rate limits automatically.

---

## 🛠️ Built With

- [Python 3.x](https://www.python.org/)
- [PRAW](https://praw.readthedocs.io/) — Python Reddit API Wrapper
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Requests](https://docs.python-requests.org/)

---

## 📜 License

MIT License — feel free to use, modify, and share!

---

## 🙋‍♂️ Author

Made by **Ekanshi** — feel free to connect!

[![GitHub](https://img.shields.io/badge/GitHub-Ekanshigangkas-black?logo=github)](https://github.com/Ekanshiganglas)
