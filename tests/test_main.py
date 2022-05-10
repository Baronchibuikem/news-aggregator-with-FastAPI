from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_list_news():
    response = client.get("/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_list_news_no_empty_results():
    response = client.get("/")
    assert len([obj for obj in response.json() if not obj]) == 0


def test_list_news_required_fields():
    response = client.get("/")
    objects_with_missing_fields = []
    for obj in response.json():
        if any(field not in obj.keys() for field in ["title", "link", "source"]):
            objects_with_missing_fields.append(obj)
    assert len(objects_with_missing_fields) == 0
