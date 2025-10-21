# Reddit Sentiment Analyzer

Reddit Sentiment Analyzer is a Python-based tool that extracts posts from multiple subreddits using the Reddit API (PRAW), performs text cleaning and sentiment analysis using TextBlob, and outputs structured data for analytics.  

This script is designed for **dual use**:
- **Power BI Python Script**: Runs directly in Power BI to automatically refresh sentiment data in your dashboard.
- **VS Code or Terminal**: Runs as a standalone Python script and exports sentiment data to a CSV file (`reddit_sentiment_log.csv`).

---

## Features

- **Real-Time Reddit Scraping**  
  Fetches posts from major OpenAI subreddits (`r/OpenAI`, `r/ChatGPT`, `r/ArtificialInteligence`, etc.) on demand.
- **NLP Sentiment Analytics**  
  Python script applies TextBlob for polarity and subjectivity, classifies each post as "Positive", "Negative", or "Neutral".
- **Automatic Sentiment Mapping**  
  Sentiment labels are converted to numeric scores for dashboard metrics and KPIs.
- **Interactive Power BI Dashboard**  
  - Sentiment distribution bar charts  
  - Trend lines for average sentiment over time  
  - Stacked columns by subreddit and sentiment  
  - Table of top posts by score or comments
- **Conditional Visual Formatting**  
  Overall Sentiment Card/gauge changes color:  
  - **Green** for Positive  
  - **Red** for Negative  
  - **Yellow** for Neutral
- **Single-Click Refresh**  
  Refresh in Power BI Desktop triggers a live scrape so your visuals always show up-to-date sentiment.
- **Complete Customization**  
  Easily switch the topic, subreddit list, or query term for rapid brand or event sentiment tracking.
- **Exportable Data**  
  All processed posts and sentiment metadata export to CSV for reporting, archiving, or further analysis.

---

## Use Cases

- Analyzing public sentiment toward companies, topics, or technologies.
- Building Reddit-based social sentiment dashboards in Power BI.
- Academic or market research using Reddit data.
- Tracking real-time brand perception and user opinions.

## Visual
<img width="1138" height="643" alt="image" src="https://github.com/user-attachments/assets/d3cd35b1-691a-4ee5-884a-7e8046d18f19" />


