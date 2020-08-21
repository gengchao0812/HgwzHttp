from test_requests.api.util import Util
from test_requests.api.wework import WeWork


class TestWeork:
    def test_get_token(self):
        print(WeWork().test_get("GengChao"))

    def test_creat(self):
        print(WeWork().test_create("kenan888","15822266654"))