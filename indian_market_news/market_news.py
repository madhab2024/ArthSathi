from gnews import GNews
import os
import json
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def fetch_newsapi_articles():
    """
    Fetch news from NewsAPI
    """
    try:
        base_url = "https://newsapi.org/v2/everything"
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        params = {
            'q': '(NIFTY OR Sensex OR "Bank NIFTY" OR BSE OR NSE) AND (India OR Indian)',
            'apiKey': NEWS_API_KEY,
            'language': 'en',
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d'),
            'sortBy': 'publishedAt',
            'pageSize': 100,
            'domains': 'moneycontrol.com,economictimes.indiatimes.com,livemint.com,business-standard.com,ndtv.com/business,financialexpress.com'
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        articles = news_data.get('articles', [])
        print(f"Fetched {len(articles)} articles from NewsAPI")
        return articles
    except Exception as e:
        print(f"Error fetching from NewsAPI: {str(e)}")
        return []

def fetch_gnews_articles():
    """
    Fetch news from Google News
    """
    try:
        google_news = GNews(language='en', country='IN', period='7d', max_results=50)
        
        # Define search queries for different sources
        sources = {
            'moneycontrol': 'site:moneycontrol.com (NIFTY OR Sensex OR "Bank NIFTY" OR BSE OR NSE)',
            'economictimes': 'site:economictimes.indiatimes.com (NIFTY OR Sensex OR "Bank NIFTY" OR BSE OR NSE)',
            'businessstandard': 'site:business-standard.com (NIFTY OR Sensex OR "Bank NIFTY" OR BSE OR NSE)',
            'livemint': 'site:livemint.com (NIFTY OR Sensex OR "Bank NIFTY" OR BSE OR NSE)'
        }
        
        all_articles = []
        for source_name, query in sources.items():
            try:
                news_items = google_news.get_news(query)
                for item in news_items:
                    article = {
                        'title': item['title'],
                        'description': item.get('description', 'No description available'),
                        'url': item['url'],
                        'publishedAt': item['published date'],
                        'source': {'name': item['publisher']['title']},
                        'sourceName': source_name
                    }
                    all_articles.append(article)
                print(f"Fetched {len(news_items)} articles from {source_name} via GNews")
            except Exception as e:
                print(f"Error fetching from {source_name}: {str(e)}")
                continue
        
        return all_articles
    except Exception as e:
        print(f"Error fetching from GNews: {str(e)}")
        return []

def fetch_market_news():
    """
    Fetch news from both NewsAPI and GNews
    """
    try:
        # Fetch from both sources
        newsapi_articles = fetch_newsapi_articles()
        gnews_articles = fetch_gnews_articles()
        
        # Combine articles
        all_articles = newsapi_articles + gnews_articles
        
        # Remove duplicates based on URL
        unique_articles = {article['url']: article for article in all_articles}.values()
        articles_list = list(unique_articles)
        
        # Sort by published date
        articles_list.sort(key=lambda x: x['publishedAt'], reverse=True)
        
        # Save to JSON file
        output_file = os.path.join(os.path.dirname(__file__), 'market_news.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(articles_list, f, ensure_ascii=False, indent=2)
        
        print(f"\nTotal unique articles saved: {len(articles_list)}")
        print(f"NewsAPI articles: {len(newsapi_articles)}")
        print(f"GNews articles: {len(gnews_articles)}")
        print(f"Saved to: {output_file}")
        return len(articles_list)
        
    except Exception as e:
        print(f"Error in fetch_market_news: {str(e)}")
        return 0

if __name__ == "__main__":
    fetch_market_news() 