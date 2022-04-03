## About The Project

[![Product Name Screen Shot][product-screenshot]](#about-the-project)

The application is built in accordance with <a href="https://github.com/meddyco/Backend-Assignment">Problem Statement</a> document. All of the features are implemented. All the contraints are implemented, along with project documentation and unit-tests.

<br>

### Built With

- [Python](http://python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

<br>

### Prerequisites

To run this project, should install project dependencies:

1. Python3
2. pip
3. Intsall Python packages

4. Clone the repo

```sh
git clone https://github.com/Baronchibuikem/news_aggregator
```

2. Open terminal in project folder

```sh
cd news_aggregator
```

3. Create your virtual environment

```sh
python3 -m venv env
```

4. Activate your virtual environment

```sh
source env/bin/activate
```

5. Install python packages

```sh
pip3 install -r requirements.txt
```

6. Create your configurations file `.env` and add the code below.

```sh
NEWS_API_KEY = '547bb651f65d4e0bb202f468c1e96a07'
```

4. Run server

```sh
uvicorn main:app --reload
```

##### You can run tests with:

```sh
pytest
```

<br>

##### Steps to Add any New API

1. Go to `src/utils/external_lib_config`
2. Prepare API Mapping object
3. Navigate to `src/queries/run_queries` and add the query for the new api

<!-- CONTACT -->

## Contact

Baron Chibuikem - [Email](baronchibuike@gmail.com)

LinkedIn: [LinkedIn](https://www.linkedin.com/in/anozie-u-chibuikem)
