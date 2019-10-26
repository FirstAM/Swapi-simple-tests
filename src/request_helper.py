import requests


class RequestHelper:

    main_url = "https://swapi.co/api/"

    def get_response_with_id(self, id='1', target='films'):
        url = self.main_url + target + '/' + id + '?format=json'
        return requests.get(url)

    def get_response(self):
        return self.get_response_with_id('')

    def get_schema(self, method='films'):
        return requests.get(self.main_url+method+'/schema')
