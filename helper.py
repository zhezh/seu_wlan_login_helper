import time
import requests
import re


class SeuHelper:
    def __init__(self, ykt, password, enable_mac_auth, connection_website, checking_interval=90):

        self.ykt = ykt
        self.pwd = password
        self.enable_mac_auth = enable_mac_auth
        self.connection_web = connection_website
        if len(self.connection_web) == 0:
            self.connection_web = 'http://www.baidu.com'
        self.every = checking_interval  # seconds

    def login(self):
        print(self.getCurrentTime(), "拼命连网中...")

        url="https://w.seu.edu.cn/index.php/index/login"
        headers={
            # 'Host':"xxxxxx",
            'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
            'Accept':"application/json, text/javascript, */*; q=0.01",
            'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding':"gzip, deflate",
            # 'Referer':"xxxxxx",
            'Content-Type':"application/x-www-form-urlencoded",
            'X-Requested-With':"XMLHttpRequest",
            # 'Content-Length':"291",
            'Connection':"close"
        }
        # 提交的信息
        payload={
            'username': str(self.ykt),
            'password': self.pwd,
            'enablemacauth': '1' if self.enable_mac_auth else '0'
        }
        try:
            requests.post(url, headers=headers, data=payload, verify=False)
            print(self.getCurrentTime(),'连上了.')
        except:
            print("error")

    def logout(self):
        print(self.getCurrentTime(), "logout...")

        url="https://w.seu.edu.cn/index.php/index/logout"
        headers={
            # 'Host':"xxxxxx",
            'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
            'Accept':"application/json, text/javascript, */*; q=0.01",
            'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding':"gzip, deflate",
            # 'Referer':"xxxxxx",
            'Content-Type':"application/x-www-form-urlencoded",
            'X-Requested-With':"XMLHttpRequest",
            # 'Content-Length':"291",
            'Connection':"close"
        }
        payload = {}
        try:
            requests.post(url, headers=headers, data=payload, verify=False)
            print(self.getCurrentTime(),'logged out.')
        except:
            print("error")

    def canConnect(self):
        try:
            q=requests.get(self.connection_web, timeout=5, verify=False)
            m=re.search(r'STATUS OK',q.text)
            if m:
                return True
            else:
                return False
        except:
            print('error')
            return False

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
