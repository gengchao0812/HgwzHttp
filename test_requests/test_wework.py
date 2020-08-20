import pytest
import requests
from rest_framework.utils import json


class TestWework:

    #扩展到所有模块@pytest.fixture(scope="session")
    #获取一次 提高运行速度
    @pytest.fixture(scope="session")
    def token(self):
        request_params = {
            "corpid":"ww42ef0685704b0bef",
            "corpsecret":"csR7yfZ8d_hFznM5_p34WEaIsM4yeTXs9P2li3J18s4"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=request_params)
        return r.json()['access_token']
    # def get_token(self):
    #     """
    #     获取token
    #     https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
    #     :return:
    #     """
    #     request_params = {
    #         "corpid":"ww42ef0685704b0bef",
    #         "corpsecret":"csR7yfZ8d_hFznM5_p34WEaIsM4yeTXs9P2li3J18s4"
    #     }
    #     r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #                      params=request_params)
    #     return r.json()['access_token']

    def test_create(self,token,userid,mobile,name = "柯南" ,department= None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.get_token()
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}
        # 反序列化
        # json.loads()
        print(json.dumps(request_body))
        print(request_body)
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                      json=request_body)
        #反序列化 等于json.loads
        return r.json()

    def test_get(self,token,userid):
        """
        读取
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self,token,userid,name = "柯南" ,mobile = "15810111111"):
        """
        更新
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
            "mobile":mobile
            # **kwargs
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                          json=request_body)
        return r.json()

    def test_delete(self,token,userid):
        """
        删除
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    def test_wework(self,token):
        """
        整体测试
        :return:
        """
        userid = "kenan123"
        name = "柯南"
        assert "created" == self.test_create(token,userid,"15815100000")["errmsg"]
        # self.test_create(token, userid, "15815100000")
        assert name == self.test_get(token,userid)["name"]
        assert "updated" == self.test_update(token,userid,name="柯南555")["errmsg"]
        assert "柯南555" == self.test_get(token,userid)["name"]
        assert "deleted"== self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token,userid)["errcode"]