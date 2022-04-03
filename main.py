from fastapi import FastAPI, HTTPException
from src.queries.run_queries import QueryManager
from typing import Optional

app = FastAPI()

@app.get('/news')
def list_news(q: Optional[str] = None, limit: int = 10):
    """
    This endpoint will serve for both getting the news listings and search functionality.

    :param q: search query to be passed to the request url.
    :param limit: Integer number to limit number of results to fetch from each dependent API.
    :return: JSON response of aggregated results.
    """
    manager = QueryManager(q, limit)
    try:
        if q:
            # call search endpoint
            result = manager.search_news_query()
        else:
            # call news listing endpoint
            result = manager.get_news_query()
            print("==========", result)
        return result
    except:
        raise HTTPException(400, "something went wrong/ Bad request")  



# @app.get("/blogs/{blog_id}", response_model=BlogSchema)
# def list_blog(blog_id: int, db: Session = Depends(create_get_session)):
#     blog_crud = BlogCrud(db)
#     response = blog_crud.get_blog(blog_id)
#     if response:
#         response = jsonable_encoder(response)
#         return JSONResponse(status_code=status.HTTP_200_OK, content=response)
#     raise HTTPException(400, "something went wrong/ Bad request")


# def get_news_query(self):
#         for api_sources in API_COLLECTION:
#             print(EXTERNAL_SOURCES_CONFIG[api_sources]['listing_url'].format(limit=self.limit), '=============', EXTERNAL_SOURCES_CONFIG[api_sources]['access_key'])
#             news_list: list = []
#             # try:
#             request_client = RequestClient('NewsList')
#             print(self.news_api_key, '$$$$$$$$$$$')
#             response = request_client.request(
#                 method='get',
#                 url=EXTERNAL_SOURCES_CONFIG[api_sources]['listing_url'].format(limit=self.limit),
#                 headers={'x-api-key': self.news_api_key, 'Content-Type': 'application/json'},
#             )
#             print('here now', response)
#             # if api_sources['source'] == 'news_api' and response is not None:
#             if response:
#                 print('running if -----------', response.response_data['articles'])
#                 for data in response.response_data['articles']:
#                     self.response_data.append({
#                         "title": data["title"],
#                         "link": data["url"],
#                         "source": api_sources['source']
#                     })
#                 print(news_list)
#                 self.response_data += news_list
#             # else:
#             #     print('running else -----------')
#             #     for data in response.response_data["data"]["children"]:
#             #         news_list.append({
#             #             "title": data["data"]["title"],
#             #             "link": data["data"]["url"],
#             #             "source": api_sources['source']
#             #         })
#             # self.response_data += news_list
#             #     try:
#             #         self.response_status = response.response_data['status']
#             #     except KeyError:
#             #         self.response_status = False
#             #     self.response_data = response.response_data['articles']
#             #     self.status_code = response.status_code
#             # except ThirdPartyAPIConnectionError as error:
#             #     self.response_data = error.response_data
#             # # print(response.response_data, '++++++++++++++++++')
#             # self.response_data = {"hi": "skdskskkd"}
#             print(self.response_data, '----------')
#             return self.response_data
