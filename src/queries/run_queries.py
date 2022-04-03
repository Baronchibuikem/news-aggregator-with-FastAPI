
import os
from dotenv import load_dotenv, find_dotenv
from typing import Optional, Any
from src.utils.external_api_call import RequestClient
from src.queries.news_api_utils import EXTERNAL_SOURCES_CONFIG, API_COLLECTION




class QueryManager:
    def __init__(self, query: Optional[str] = None, limit: int = 10) -> None:
        self.query = query
        self.limit = limit
        self.response_data = []
        self.response_status: bool = False
        self.news_api_key = os.getenv("NEWS_API_KEY", None)

    def search_news_query(self):
        print('this is the search functionality')


    def get_news_query(self):
        all_data_list: list = []
        reddit_list = []
        news_api_list = []

        for api_sources in API_COLLECTION:
            # try:
            request_client = RequestClient('NewsList')
            response = request_client.request(
                method='get',
                url=EXTERNAL_SOURCES_CONFIG[api_sources]['listing_url'].format(limit=self.limit),
                headers={'x-api-key': EXTERNAL_SOURCES_CONFIG[api_sources]['access_key'], 
                'Content-Type': 'application/json',
                'User-agent': 'your bot 0.1'},
            )

            if EXTERNAL_SOURCES_CONFIG[api_sources]['source'] == 'news_api' and response:
                for data in response.response_data['articles']:
                    news_api_list.append({
                        "title": data["title"],
                        "link": data["url"],
                        "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                    })
                all_data_list += news_api_list
            else:
                for data in response.response_data["data"]["children"]:
                    reddit_list.append({
                        "title": data["data"]["title"],
                        "link": data["data"]["url"],
                        "source": EXTERNAL_SOURCES_CONFIG[api_sources]['source']
                    })
                all_data_list += reddit_list
        self.response_data += all_data_list
        # print(news_api_list)
            #     try:
            #         self.response_status = response.response_data['status']
            #     except KeyError:
            #         self.response_status = False
            #     self.response_data = response.response_data['articles']
            #     self.status_code = response.status_code
            # except ThirdPartyAPIConnectionError as error:
            #     self.response_data = error.response_data
            # # print(response.response_data, '++++++++++++++++++')
            # self.response_data = {"hi": "skdskskkd"}
        return self.response_data
