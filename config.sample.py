# ─────────────────────────────────────────────
#   Reddit Keyword Bot — Sample Config
# ─────────────────────────────────────────────
# Copy this file, rename it to config.py, and fill in your credentials.

REDDIT_CLIENT_ID     = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDDIT_USERNAME      = "YOUR_REDDIT_USERNAME"
REDDIT_PASSWORD      = "YOUR_REDDIT_PASSWORD"

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID   = "YOUR_TELEGRAM_CHAT_ID"

SUBREDDIT = "all"

KEYWORD_GROUPS = {
    "jobs": [
        "internship", "hiring", "job opening",
        "fresher", "entry level", "remote job",
    ],
    "india_news": [
        "india", "modi", "bjp", "upsc",
        "rupee", "mumbai", "delhi",
    ],
    "programming": [
        "programming meme", "python vs", "vs code",
        "developer life", "coding meme", "learn to code",
    ]
}

REPLIED_LOG = "replied.txt"
