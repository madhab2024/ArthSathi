import time
import schedule
from datetime import datetime
from market_news import fetch_market_news

def update_news():
    """Update the market news data"""
    print(f"\nUpdating market news at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    num_articles = fetch_market_news()
    print(f"Fetched {num_articles} articles\n")

# Run immediately on start
update_news()

# Schedule updates every 30 minutes
schedule.every(30).minutes.do(update_news)

print("Market news updater is running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1) 