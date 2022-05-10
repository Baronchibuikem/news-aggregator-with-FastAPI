from typing import Optional
from mangum import Mangum

from fastapi import FastAPI, HTTPException

from src.queries.run_queries import QueryManager

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
        return result
    except:
        raise HTTPException(400, "something went wrong/ Bad request")

@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)

handler = Mangum(app=app)
