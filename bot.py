import praw
import requests
import csv
import os
import time
from datetime import datetime
from config import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
    REDDIT_USERNAME, REDDIT_PASSWORD,
    TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
    KEYWORD_GROUPS, SUBREDDIT, REPLIED_LOG
)

# ─── Connect to Reddit ───────────────────────────────────────────────
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent="reddit-keyword-bot by u/" + REDDIT_USERNAME
)

# ─── Load already-replied IDs ────────────────────────────────────────
def load_replied():
    if not os.path.exists(REPLIED_LOG):
        return set()
    with open(REPLIED_LOG, "r") as f:
        return set(line.strip() for line in f.readlines())

def save_replied(comment_id):
    with open(REPLIED_LOG, "a") as f:
        f.write(comment_id + "\n")

# ─── Send Telegram Notification ──────────────────────────────────────
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
        print("  📲 Telegram notification sent!")
    except Exception as e:
        print(f"  ❌ Telegram error: {e}")

# ─── Log to CSV ───────────────────────────────────────────────────────
def log_to_csv(category, keyword, comment):
    file_exists = os.path.exists("matches_log.csv")
    with open("matches_log.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Category", "Keyword", "Author", "Subreddit", "URL"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            category,
            keyword,
            str(comment.author),
            str(comment.subreddit),
            f"https://reddit.com{comment.permalink}"
        ])

# ─── Get Reply Message ────────────────────────────────────────────────
def get_reply(category):
    replies = {
        "jobs": (
            "👋 Hey! Looks like you're discussing jobs/internships.\n\n"
            "Here are some helpful resources:\n"
            "- [LinkedIn Jobs India](https://www.linkedin.com/jobs/)\n"
            "- [Internshala](https://internshala.com/)\n"
            "- [Naukri.com](https://www.naukri.com/)\n\n"
            "*Good luck with your search! 🚀*\n\n"
            "---\n*^(I am a bot. | Made by u/YOUR_USERNAME)*"
        ),
        "india_news": (
            "🇮🇳 Looks like you're discussing something related to India!\n\n"
            "Stay updated with:\n"
            "- [The Hindu](https://www.thehindu.com/)\n"
            "- [NDTV](https://www.ndtv.com/)\n"
            "- [r/india](https://www.reddit.com/r/india/)\n\n"
            "---\n*^(I am a bot. | Made by u/YOUR_USERNAME)*"
        ),
        "programming": (
            "😄 Ah, a fellow programmer! Great discussion here.\n\n"
            "Some fun places for programmers:\n"
            "- [r/ProgrammerHumor](https://www.reddit.com/r/ProgrammerHumor/)\n"
            "- [r/learnprogramming](https://www.reddit.com/r/learnprogramming/)\n"
            "- [Dev.to](https://dev.to/)\n\n"
            "---\n*^(I am a bot. | Made by u/YOUR_USERNAME)*"
        )
    }
    return replies.get(category, "Thanks for posting! 🤖")

# ─── Main Bot Loop ────────────────────────────────────────────────────
def run_bot():
    print("🤖 Reddit Keyword Bot is running...")
    print(f"📡 Monitoring: r/{SUBREDDIT}")
    print(f"🔍 Keywords: {KEYWORD_GROUPS}\n")

    replied_ids = load_replied()
    subreddit = reddit.subreddit(SUBREDDIT)

    for comment in subreddit.stream.comments(skip_existing=True):
        if comment.id in replied_ids:
            continue

        body = comment.body.lower()

        for category, keywords in KEYWORD_GROUPS.items():
            for keyword in keywords:
                if keyword.lower() in body:
                    print(f"\n✅ [{category.upper()}] Found '{keyword}'")
                    print(f"   👤 u/{comment.author} in r/{comment.subreddit}")
                    print(f"   🔗 https://reddit.com{comment.permalink}")

                    # Auto-reply
                    try:
                        comment.reply(get_reply(category))
                        print("   💬 Replied successfully!")
                    except Exception as e:
                        print(f"   ❌ Reply failed: {e}")

                    # Telegram notification
                    tg_msg = (
                        f"🔔 *Reddit Bot Alert!*\n\n"
                        f"📂 Category: `{category}`\n"
                        f"🔑 Keyword: `{keyword}`\n"
                        f"👤 User: u/{comment.author}\n"
                        f"📌 Subreddit: r/{comment.subreddit}\n"
                        f"🔗 [View Comment](https://reddit.com{comment.permalink})"
                    )
                    send_telegram(tg_msg)

                    # Log it
                    log_to_csv(category, keyword, comment)

                    # Mark as replied
                    replied_ids.add(comment.id)
                    save_replied(comment.id)
                    break  # don't double-reply for multiple keywords

        time.sleep(0.5)  # be nice to Reddit's servers

if __name__ == "__main__":
    run_bot()
