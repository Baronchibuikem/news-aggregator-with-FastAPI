from ..utils.external_libs_config import EXTERNAL_SOURCES_CONFIG

class RedditManager:
    def __init__(self):
        self.all_data_list: list = []
        self.reddit_list:list = []
        self.response = None

    def reddit_fetch_data():
        """Calls to reddit api."""
        request_client = RequestClient("Reddit")
        self.response = request_client.request(
            method="get",
            url=EXTERNAL_SOURCES_CONFIG[api_sources]["listing_url"].format(
                limit=self.limit
            ),
            headers={
                "x-api-key": EXTERNAL_SOURCES_CONFIG[api_sources]["access_key"],
                "Content-Type": "application/json",
                "User-agent": "your bot 0.1",
            },
        )

    def reddit_fetch_news(self):
        """list of news from reddit."""

        # make the call to reddit api
        self.reddit_fetch_data()

        print(self.response)

        # check if the response is not none and display the news
        if self.response is not None and self.response.response_data["data"]["children"] is not None:
            for data in self.response.response_data["data"]["children"]:
                self.reddit_list.append(
                    {
                        "title": data["data"]["title"],
                        "link": data["data"]["url"],
                        "source": EXTERNAL_SOURCES_CONFIG[api_sources][
                            "source"
                        ],
                    }
                )
            self.all_data_list += self.reddit_list
        else:
            all_data_list = []
        return all_data_list