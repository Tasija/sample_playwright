import requests


class Https(object):
    def __init__(self, base_url):
        self.headers = {'Content-Type': 'application/json',
                        'Accept': '*/*'}
        self.base_url = base_url
        self.timeout = 3

    @staticmethod
    def get_result(response):
        return {'data': response.json(),
                'status_code': response.status_code,
                'headers': response.headers}

    def set_headers(self, **kwargs):
        for key, value in kwargs:
            self.headers[key] = kwargs[key]

    def get(self, resource):
        response = requests.get(url=f'{self.base_url}/{resource}',
                                headers=self.headers,
                                timeout=self.timeout,
                                verify=False)
        return self.get_result(response)

    def post(self, resource, **json_body):
        response = requests.post(url=f'{self.base_url}/{resource}',
                                 headers=self.headers,
                                 timeout=self.timeout,
                                 json=json_body)
        return self.get_result(response)

    def put(self, resource, **json_body):
        response = requests.put(url=f'{self.base_url}/{resource}',
                                json=json_body,
                                headers=self.headers,
                                timeout=self.timeout,
                                verify=False)
        return self.get_result(response)

    def delete(self, resource):
        response = requests.delete(url=f'{self.base_url}/{resource}',
                                   headers=self.headers,
                                   timeout=self.timeout,
                                   verify=False)
        return {'status_code': response.status_code}