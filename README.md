# Daily Leetcode POTD

Queries Leetcode GraphQL as well as populate Telegram ([link ](https://t.me/+KukNOrH9lgI0YmNl)) with the corresponding Leetcode Question.

There is a file which automatically fetches LeetCode's Daily Problem of the Day and creates a Python starter file for users to quickly begin working on the solution.

## Features

- Fetches the latest daily problem directly from LeetCode.
- Converts the problem description into clean Markdown format (code blocks, lists, etc.).
- Automatically forwards the problem to a Telegram bot/chat.
- Runs on a GitHub Actions scheduler every day at 01:00 UTC (no local setup required).
- Also supports manual trigger from GitHub Actions for testing.

## Tech Stack

- Python (Requests, BeautifulSoup4)
- Telegram Bot API
- GitHub Actions (cron-based scheduling)


## Contributing

Feel free to submit your solutions as pull requests or open issues for improvements!

## Automation Details

- The scheduler is implemented via GitHub Actions in `.github/workflows/daily-leetcode.yml`.
- The fetching logic is in `fetch_leetcode_daily.py`, which scrapes the LeetCode daily question using their public GraphQL endpoint.
