import os
from typing import Dict, Any
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NEWS_API_CONFIG = 1
REDDIT_API_MAPPING = 2



EXTERNAL_SOURCES_CONFIG: Dict[int, Dict[str, Any]] = {
    NEWS_API_CONFIG: {
        "api_name": "newsapi",
        "source": 'news_api',
        "listing_url": "http://newsapi.org/v2/top-headlines?category=general&pageSize={limit}&page=1",
        "search_url": "http://newsapi.org/v2/everything?q=f'{query}'&pageSize=f'{limit}'&page=1",
        "access_key": os.getenv("NEWS_API_KEY")
    },
    REDDIT_API_MAPPING : {
        "api_name": "reddit",
        "source": "reddit",
        "listing_url": ('https://www.reddit.com/r/news/top.json?''limit={limit}'),
        "search_url": 'https://www.reddit.com/r/news/search.json?''q={query}&''limit={limit}',
        'access_key': ""
    }
}

API_COLLECTION = [
    NEWS_API_CONFIG,
    REDDIT_API_MAPPING
]
