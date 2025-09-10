# Daily Leetcode POTD

Queries Leetcode GraphQL as well as populate Telegram with the corresponding Leetcode Question.

There is a file which automatically fetches LeetCode's Daily Problem of the Day and creates a Python starter file for users to quickly begin working on the solution.

## Features

- **Daily Scheduler:** Uses GitHub Actions to fetch and generate a telegram message for LeetCode's daily question every day at 01:00 UTC.
- **Problem Description:** The problem description and all relevant fields are parsed into the telegram message.

## Contributing

Feel free to submit your solutions as pull requests or open issues for improvements!

## Automation Details

- The scheduler is implemented via GitHub Actions in `.github/workflows/daily-leetcode.yml`.
- The fetching logic is in `fetch_leetcode_daily.py`, which scrapes the LeetCode daily question using their public GraphQL endpoint.
