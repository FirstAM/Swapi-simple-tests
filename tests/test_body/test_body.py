import pytest
from src.request_helper import RequestHelper


@pytest.mark.body
class BodyTests:

    response = RequestHelper().get_response().json()

    @pytest.mark.smoke
    def test_body_response(self):
        count = self.response["count"]
        list_count = self.response["results"].__len__()
        assert count == list_count

    def test_check_text_wrong_response(self):
        count = self.response["count"]
        response = RequestHelper().get_response_with_id(str(count + 1)).json()
        assert response['detail'] == 'Not found'
