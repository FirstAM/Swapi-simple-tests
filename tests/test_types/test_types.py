import pytest
from src.request_helper import RequestHelper
from src.schema_helper import SchemeHelper


@pytest.mark.types
class TypesTests:

    scheme_helper = SchemeHelper()
    response = RequestHelper().get_response_with_id().json()

    def check_type(self, resource):
        resource_type = self.scheme_helper.get_resource_format(resource)
        return type(self.response[resource]).__name__ == resource_type

    def test_title_type(self):
        assert self.check_type("title")

    @pytest.mark.smoke
    def test_episode_id_type(self):
        assert self.check_type("episode_id")

    @pytest.mark.smoke
    def test_opening_crawl_type(self):
        assert self.check_type("opening_crawl")

    def test_director_type(self):
        assert self.check_type("director")

    def test_producer_type(self):
        assert self.check_type("producer")

    def test_release_date_type(self):
        assert self.check_type("release_date")

    @pytest.mark.smoke
    def test_characters_type(self):
        assert self.check_type("characters")

    def test_planets_type(self):
        assert self.check_type("planets")

    def test_starships_type(self):
        assert self.check_type("starships")

    @pytest.mark.smoke
    def test_vehicles_type(self):
        assert self.check_type("vehicles")

    @pytest.mark.smoke
    def test_species_type(self):
        assert self.check_type("species")

    @pytest.mark.smoke
    def test_created_type(self):
        assert self.check_type("created")

    @pytest.mark.smoke
    def test_edited_type(self):
        assert self.check_type("edited")

