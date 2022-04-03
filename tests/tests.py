from fastapi.testclient import TestClient
from api import app

import responses


#
# Some Unit Tests
client = TestClient(app)


def test_list_news():
    response = client.get("/news")
    assert response.status_code == 200
    assert type(response.json()) == list   # list object is returned


def test_list_news_no_empty_results():
    response = client.get("/news")
    assert len([obj for obj in response.json() if not obj]) == 0   # response has no empty objects/ {}


def test_list_news_required_fields():
    response = client.get("/news")
    objects_with_missing_fields = []
    for obj in response.json():
        print(obj.keys())
        if any(field not in obj.keys() for field in ["title", "link", "source"]):
            objects_with_missing_fields.append(obj)
    assert len(objects_with_missing_fields) == 0   # make sure 3 essential fields are present


@responses.activate
def test_view()
    def test_validator_bvn__failure__api_error_with_response(self):
        """Ensure BVN Validator works."""
        validator = SmileIdentityBVNValidator()

        responses.add(
            responses.POST,
            SMILE_BVN_API_URL,
            json={'error': 'System Error', 'code': '2401'},
            status=status.HTTP_400_BAD_REQUEST,
            content_type='application/json',
        )

        self.assertFalse(validator.validate('12345678901', self.user))
        self.assertEqual(
            validator.errors, ['We are unable to validate your BVN at this time, please try again shortly.']
        )
        self.assertEqual(UserVerification.objects.all().count(), 0)