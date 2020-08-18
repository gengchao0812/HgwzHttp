import requests
from rest_framework.utils import json


class TestWework:
    def get_token(self):
        """
        获取token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        request_params = {
            "corpid":"ww42ef0685704b0bef",
            "corpsecret":"csR7yfZ8d_hFznM5_p34WEaIsM4yeTXs9P2li3J18s4"
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=request_params)
        return r.json()['access_token']

    def test_create(self):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        access_token = self.get_token()
        request_body = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000001",
            "department": [1]}
        # 反序列化
        # json.loads()
        print(json.dumps(request_body))
        print(request_body)
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}",
                      json=request_body)
        #反序列化 等于json.loads
        print(r.json())

    def test_get(self):
        """
        读取
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.get_token()}&userid=zhangsan")
        print(r.json())

    def test_update(self):
        """
        更新
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": "zhangsan",
            "name": "李四",
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.get_token()}",
                          json=request_body)
        print(r.json())

    def test_delete(self):
        """
        删除
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zhangsan")
        print(r.json())