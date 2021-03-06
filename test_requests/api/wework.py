import random
import re

import pytest
import requests
import yaml
from rest_framework.utils import json

from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util

class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/wework.yaml",encoding="utf-8") as f:
            self.data = yaml.load(f)

    #扩展到所有模块@pytest.fixture(scope="session")
    # #获取一次 提高运行速度
    # @pytest.fixture(scope="session")
    # def token(self):
    #     request_params = {
    #         "corpid":"ww42ef0685704b0bef",
    #         "corpsecret":"csR7yfZ8d_hFznM5_p34WEaIsM4yeTXs9P2li3J18s4"
    #     }
    #     r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #                      params=request_params)
    #     return r.json()['access_token']

    def test_create(self,userid,mobile,name = "柯南" ,department= None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.get_token()
        if department is None:
            department = "1"
        # 反序列化
        # # json.loads()
        # print(json.dumps(request_body))
        # print(request_body)
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #               json=request_body)
        # data = {
        #     "method":"post",
        #     "url" : f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json":{
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department
        #             }
        # }
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        #反序列化 等于json.loads
        return self.send(self.data["create"])

    def test_get(self,userid):
        """
        读取
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        # data = {
        #     "method":"get",
        #     "url":f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        # }
        self.params["userid"] = userid
        return self.send(self.data["get"])
        # return r.json()

    def test_update(self,userid,name = "柯南111" ):
        """
        更新
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # request_body = {
        #     "userid": userid,
        #     "name": name
        #     # **kwargs
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                   json=request_body)
        # data={
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json":{
        #         "userid": userid,
        #         "name": name
        #             }
        # }
        self.params["userid"] = userid
        self.params["name"] = name
        return self.send(self.data["update"])

    def test_delete(self,userid):
        """
        删除
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        # data = {
        #     "method":"get",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        # }
        self.params["userid"] = userid
        # 反序列化 等于json.loads
        return self.send(self.data["delete"])
        # return r.json()