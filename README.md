# Reddit Sentiment Analyzer

Reddit Sentiment Analyzer is a Python-based tool that extracts posts from multiple subreddits using the Reddit API (PRAW), performs text cleaning and sentiment analysis using TextBlob, and outputs structured data for analytics.  

This script is designed for **dual use**:
- **Power BI Python Script**: Runs directly in Power BI to automatically refresh sentiment data in your dashboard.
- **VS Code or Terminal**: Runs as a standalone Python script and exports sentiment data to a CSV file (`reddit_sentiment_log.csv`).

---

## Features

- Fetches Reddit posts from multiple subreddits.
- Filters by a keyword or brand name.
- Cleans and preprocesses text data.
- Calculates sentiment polarity and subjectivity using `TextBlob`.
- Categorizes posts as **Positive**, **Negative**, or **Neutral**.
- Outputs a ready-to-use CSV dataset for visualization or machine learning.
- Compatible with both **Power BI** and **VS Code** environments.

---

## Use Cases

- Analyzing public sentiment toward companies, topics, or technologies.
- Building Reddit-based social sentiment dashboards in Power BI.
- Academic or market research using Reddit data.
- Tracking real-time brand perception and user opinions.
