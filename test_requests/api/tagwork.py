import yaml
import requests

from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util

class TagWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/tagwork.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def test_tag_create(self,tagid,tagname="标签默认名"):
        # request_params = {
        #     "tagname": "UII",
        #     "tagid": 112
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
        #                   json=request_params)
        self.params['tagid'] = tagid
        self.params['tagname'] = tagname
        return (self.send(self.data['create']))

    def test_tag_update(self,tagid,tagname="修改默认名"):
        # request_params = {
        # "tagid": 112,
        # "tagname": "UI design"
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
        #                   json=request_params)
        self.params['tagid'] = tagid
        self.params['tagname'] = tagname
        return(self.send(self.data['update']))
        # print(r.json())

    def test_tag_delete(self,tagid):
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}")
        # print(r.json())
        self.params['tagid'] = tagid
        return(self.send(self.data['delete']))

    def test_tag_get(self,tagid):
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        # print(r.json())
        self.params['tagid'] = tagid
        return(self.send(self.data['get']))

