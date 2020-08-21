import requests


class Util:
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