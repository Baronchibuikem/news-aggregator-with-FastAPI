
import os
from dotenv import load_dotenv, find_dotenv
from typing import Optional, Any
from src.utils.external_api_call import RequestClient
from src.utils.external_libs_config import EXTERNAL_SOURCES_CONFIG, API_COLLECTION
from src.utils.exceptions import ThirdPartyAPIConnectionError

class QueryManager:
    def __init__(self, query: Optional[str] = None, limit: int = 10) -> None:
        """Initialization values."""
        self.query: str = query
        self.limit: int = limit
        self.response_data: list = []
        self.response_status: bool = False
        self.news_api_key: str = os.getenv("NEWS_API_KEY")

    def search_news_query(self):
        """function to get search results for a given QUERY from all registered APIs (in API_COLLECTION)."""
        all_data_list: list = []
        reddit_list = []
        news_api_list = []

        for api_sources in API_COLLECTION:
            try:
                request_client = RequestClient('NewsList')
                response = request_client.request(
                    method='get',
                    url=EXTERNAL_SOURCES_CONFIG[api_sources]['search_url'].format(query=self.query, limit=self.limit),
                    headers={'x-api-key': EXTERNAL_SOURCES_CONFIG[api_sources]['access_key'], 
                    'Content-Type': 'application/json',
                    'User-agent': 'your bot 0.1'},
                )

                # if the source of data is new_api and response is not false
                if EXTERNAL_SOURCES_CONFIG[api_sources]['source'] == 'news_api' and response:
                    for data in response.response_data['articles']:
                        news_api_list.append({
                            "title": data["title"],
                            "link": data["url"],
                            "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                        })
                    all_data_list += news_api_list
                
                # since we are only fetching from 2 third-parties libraries, this runs if the source of data wasn't news_api
                else:
                    for data in response.response_data["data"]["children"]:
                        reddit_list.append({
                            "title": data["data"]["title"],
                            "link": data["data"]["url"],
                            "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                        })
                    all_data_list += reddit_list
            except ThirdPartyAPIConnectionError as error:
                # self.response_data = error.response_data
                pass

        self.response_data += all_data_list
        return self.response_data



    def get_news_query(self) -> list[dict[str, Any]]:
        """For fetching list of data from any Reddit and News_Api endpoints"""
        all_data_list: list = []
        reddit_list = []
        news_api_list = []

        for api_sources in API_COLLECTION:
            try:
                request_client = RequestClient('NewsList')
                response = request_client.request(
                    method='get',
                    url=EXTERNAL_SOURCES_CONFIG[api_sources]['listing_url'].format(limit=self.limit),
                    headers={'x-api-key': EXTERNAL_SOURCES_CONFIG[api_sources]['access_key'], 
                    'Content-Type': 'application/json',
                    'User-agent': 'your bot 0.1'},
                )

                # if the source of data is new_api and response is not false
                if EXTERNAL_SOURCES_CONFIG[api_sources]['source'] == 'news_api' and response:
                    for data in response.response_data['articles']:
                        news_api_list.append({
                            "title": data["title"],
                            "link": data["url"],
                            "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                        })
                    all_data_list += news_api_list
                
                # since we are only fetching from 2 third-parties libraries, this runs if the source of data wasn't news_api
                else:
                    for data in response.response_data["data"]["children"]:
                        reddit_list.append({
                            "title": data["data"]["title"],
                            "link": data["data"]["url"],
                            "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                        })
                    all_data_list += reddit_list
            except ThirdPartyAPIConnectionError as error:
                pass

        self.response_data += all_data_list
        return self.response_data
