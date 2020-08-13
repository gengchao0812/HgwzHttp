import requests
import pytest

class TestDemo():
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com', auth=('user', 'pass'))
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json)
        assert r.status_code == 200

