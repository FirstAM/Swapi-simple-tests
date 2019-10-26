import pytest
from src.request_helper import RequestHelper


@pytest.mark.response
class ResponseTests:

    response = RequestHelper().get_response()

    @pytest.mark.smoke
    def test_check_response_code(self):
        assert self.response.status_code == 200

    def test_wrong_parameter(self):
        content = self.response.json()
        count = content["count"]
        response = RequestHelper().get_response_with_id(str(count+1))
        assert response.status_code == 404

