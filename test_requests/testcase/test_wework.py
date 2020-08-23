import requests

from test_requests.api.util import Util
from test_requests.api.wework import WeWork


class TestWeork:
    def test_get_token(self):
        print(WeWork().test_get("GengChao"))

    def test_creat(self):
        print(WeWork().test_create("kenan100","15822266612"))

    def test_get(self):
        print(WeWork().test_get("kenan100"))

    def test_update(self):
        print(WeWork().test_update("kenan100"))

    def test_delete(self):
        print(WeWork().test_delete("kenan100"))

    def test_session(self):
        s = requests.session()
        s.params = {'access_token': Util().get_token()}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=kenan100")
        print(res.json())