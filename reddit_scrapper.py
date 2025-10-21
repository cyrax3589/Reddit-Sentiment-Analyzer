import praw
import pandas as pd
from datetime import datetime, timedelta
import re
from textblob import TextBlob

# ==== CONFIGURATION ====
REDDIT_CLIENT_ID = ""            # Paste from your Reddit app
REDDIT_CLIENT_SECRET = ""    # Paste from your Reddit app
REDDIT_USER_AGENT = ""  # Any identifier

SUBREDDITS = ["OpenAI", "ChatGPT", "Artificial", "ArtificialInteligence", "ChatGPTPro", "AIPromptProgramming", "AGI"]    # List your target subreddits 
SEARCH_KEYWORD = "OpenAI"       # Your brand/keyword
MAX_POSTS = 1000                 # Total posts to fetch
DAYS_BACK = 300                  # Historical window in days
SAVE_TO_CSV = True             # Set True to output logs
CSV_FILENAME = "reddit_sentiment_log.csv"

# ==== SENTIMENT FUNCTIONS ====
def clean_text(text):
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#(\w+)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def get_sentiment(text):
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    except:
        return 0, 0

def categorize(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    return "Neutral"

# ==== REDDIT SCRAPER ====
def fetch_reddit_posts():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    since_time = datetime.utcnow() - timedelta(days=DAYS_BACK)
    posts = []
    for subreddit_name in SUBREDDITS:
        for post in reddit.subreddit(subreddit_name).search(SEARCH_KEYWORD, sort="new", time_filter="all", limit=MAX_POSTS):
            created_at = datetime.utcfromtimestamp(post.created_utc)
            if created_at < since_time:
                continue
            posts.append({
                "post_id": post.id,
                "created_at": created_at,
                "subreddit": subreddit_name,
                "title": post.title,
                "selftext": post.selftext[:800],  # Optional: truncate long posts
                "author": str(post.author),
                "score": post.score,
                "num_comments": post.num_comments,
                "permalink": post.permalink
            })
    return pd.DataFrame(posts)

# ==== MAIN SCRIPT ====
def analyze_and_log():
    df = fetch_reddit_posts()
    if df.empty:
        print("No data found. Check your subreddit or keyword.")
        return pd.DataFrame()

    # Text prepping and sentiment
    df["cleaned_text"] = (df["title"].fillna("") + " " + df["selftext"].fillna("")).apply(clean_text)
    df["sentiment_score"], df["sentiment_subjectivity"] = zip(*df["cleaned_text"].map(get_sentiment))
    df["sentiment_category"] = df["sentiment_score"].map(categorize)
    df["brand"] = SEARCH_KEYWORD
    df["date"] = df["created_at"].dt.date
    df["hour"] = df["created_at"].dt.hour
    df["day_of_week"] = df["created_at"].dt.day_name()
    df["fetch_time"] = datetime.utcnow()

    output_columns = [
        "post_id", "created_at", "date", "hour", "day_of_week", "brand", "subreddit",
        "author", "title", "selftext", "cleaned_text", "sentiment_score",
        "sentiment_subjectivity", "sentiment_category", "score", "num_comments", "permalink", "fetch_time"
    ]
    df = df[output_columns]

    # Print summary
    print(f"\nReddit Sentiment Analysis for '{SEARCH_KEYWORD}' on r/{', '.join(SUBREDDITS)}")
    print("=" * 50)
    print(df["sentiment_category"].value_counts(normalize=False).to_string())
    print(f"\nAverage sentiment: {df['sentiment_score'].mean():.3f}")
    print(f"Total posts analyzed: {len(df)}")
    print("=" * 50)

    if SAVE_TO_CSV:
        df.to_csv(CSV_FILENAME, index=False)
        print(f"\nSaved results to {CSV_FILENAME}")

    return df

# ==== FOR VS CODE OR POWER BI ====
if __name__ == "__main__" or "dataset" not in locals():
    dataset = analyze_and_log()
