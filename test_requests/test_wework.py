import random
import re

import pytest
import requests
from rest_framework.utils import json


def test_created_data():
    """
    [(1,2,3),(1,2,3),(1,2,3)]
    :return:
    """
    #"138%08d"%x 补齐8位
    data = [("kenanxxx"+str(x),
             "柯南",
             "138%08d"%x) for x in range(20)]
    print(data)
    return data

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
        # # json.loads()
        # print(json.dumps(request_body))
        # print(request_body)
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

    def test_update(self,token,userid,name = "柯南" ):
        """
        更新
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name
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


    @pytest.mark.parametrize("userid,name,mobile",test_created_data())
    def test_wework(self,token,userid,name,mobile):
        """
        整体测试
        :return:
        # # """
        # userid = "kenan123"
        # name = "柯南"
        # mobile = "15815100000"
        try:
            assert "created" == self.test_create(token,userid,mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                #e.__str__ == print(e) e的实际内容就是报错信息
                #":(.*)'$" 正则
                re_userid = re.findall(":(.*)'",e.__str__())[0]
                self.test_delete(token,re_userid)
                assert "created" == self.test_create(token, userid, "15815100000")["errmsg"]
        assert name == self.test_get(token,userid)["name"]
        assert "updated" == self.test_update(token,userid,name="柯南555")["errmsg"]
        assert "柯南555" == self.test_get(token,userid)["name"]
        assert "deleted"== self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token,userid)["errcode"]
