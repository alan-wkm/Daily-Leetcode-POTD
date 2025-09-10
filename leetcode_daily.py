# leetcode_daily.py
import os
import requests
from bs4 import BeautifulSoup

LEETCODE_API_URL = "https://leetcode.com/graphql"
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def html_to_markdown(html: str) -> str:
    """Convert LeetCode's HTML problem description into Markdown-like text."""
    soup = BeautifulSoup(html, "html.parser")

    # Inline formatting
    for code in soup.find_all("code"):
        code.replace_with(f"`{code.get_text()}`")

    # Examples and code blocks
    for pre in soup.find_all("pre"):
        text = pre.get_text().strip()
        pre.replace_with(f"\n```\n{text}\n```\n")

    # Lists
    for li in soup.find_all("li"):
        li.insert_before("• ")
        li.append("\n")

    # Convert everything to text
    text = soup.get_text()
    # Collapse multiple newlines into max 2
    text = "\n".join([line.strip()
                     for line in text.splitlines() if line.strip()])
    return text


def fetch_daily_question():
    """Fetch today's LeetCode daily challenge directly from their GraphQL API."""
    query = {
        "query": """
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            date
            link
            question {
              title
              content
              topicTags { name }
            }
          }
        }
        """
    }

    response = requests.post(LEETCODE_API_URL, json=query)
    response.raise_for_status()
    data = response.json()["data"]["activeDailyCodingChallengeQuestion"]

    description_text = html_to_markdown(data["question"]["content"])

    return {
        "date": data["date"],
        "title": data["question"]["title"],
        "description": description_text,
        "topics": [tag["name"] for tag in data["question"]["topicTags"]],
        "link": f"https://leetcode.com{data['link']}"
    }


def pretty_format(daily: dict) -> str:
    """Return a nicely formatted string for printing or sending to Telegram."""
    output = []
    output.append(f"📅 Date: {daily['date']}")
    output.append(f"📝 Title: {daily['title']}\n")
    output.append("📖 Description:\n")
    output.append(daily["description"])
    output.append("\n🏷 Topics: " + ", ".join(daily["topics"]))
    output.append(f"🔗 Link: {daily['link']}")
    return "\n".join(output)


def send_to_telegram(bot_token: str, chat_id: str, message: str):
    """Send a message to a Telegram chat."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Telegram API error: {response.text}")
    return response.json()


if __name__ == "__main__":
    daily = fetch_daily_question()
    message = pretty_format(daily)
    print(message)

    if BOT_TOKEN and CHAT_ID:
        send_to_telegram(BOT_TOKEN, CHAT_ID, message)
        print("✅ Sent to Telegram")
    else:
        print("⚠️ BOT_TOKEN or CHAT_ID not set, skipping Telegram send")
