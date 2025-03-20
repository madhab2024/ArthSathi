# Indian Market News

A real-time news aggregator for Indian financial markets that combines data from NewsAPI and Google News. Get the latest updates about NIFTY, Bank NIFTY, Sensex, and the Indian stock market.

## Features

- Real-time news updates from multiple sources
- Modern, responsive web interface
- Live search functionality
- Source-based filtering
- Auto-refresh every 5 minutes
- News from trusted Indian financial sources:
  - MoneyControl
  - Economic Times
  - LiveMint
  - Business Standard
  - NDTV Business
  - Financial Express

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- NewsAPI key (get it from [NewsAPI.org](https://newsapi.org))

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd indian_market_news
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory with your NewsAPI key:
   ```env
   NEWS_API_KEY="your_newsapi_key_here"
   ```

## Usage

1. Start the news fetcher:
   ```bash
   python update_market_news.py
   ```
   This will:
   - Fetch news immediately
   - Continue to update every 30 minutes
   - Save news to `market_news.json`

2. Start the web server:
   ```bash
   python -m http.server 8000
   ```

3. Open your web browser and go to:
   ```
   http://localhost:8000
   ```

## Web Interface Features

- **Search**: Use the search box to find specific news
- **Filters**: Filter news by source using the buttons
- **Auto-refresh**: News updates automatically every 5 minutes
- **Responsive Design**: Works on both desktop and mobile devices

## News Sources

The system fetches news from:
1. **NewsAPI**: For real-time news updates
2. **Google News**: For additional coverage

## File Structure

- `market_news.py`: Main script for fetching news
- `update_market_news.py`: Script for periodic news updates
- `index.html`: Web interface
- `market_news.json`: Latest news data
- `requirements.txt`: Python dependencies
- `.env`: API key configuration

## Troubleshooting

1. If you see no news:
   - Check your NewsAPI key in `.env`
   - Ensure you have internet connectivity
   - Check the console for any error messages

2. If the web interface doesn't load:
   - Make sure the Python server is running
   - Check if `market_news.json` exists
   - Try clearing your browser cache

3. If dependencies fail to install:
   - Try updating pip: `pip install --upgrade pip`
   - Install dependencies one by one from `requirements.txt`

## Contributing

Feel free to:
- Report issues
- Suggest features
- Submit pull requests

## License

This project is open-source and available under the MIT License. 