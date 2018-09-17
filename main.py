import time
import requests
import re
import yaml
import base64
from helper import SeuHelper


if __name__ == '__main__':
    with open('./config.yaml') as f:
        config = yaml.load(f)
        # print(config)
    pwd64 = base64.b64encode(config['PASSWORD'].encode('ascii'))
    # print(pwd64)

    helper = SeuHelper(config['YKTBH'], pwd64, config['MACAUTH'],
                       config['CONNECTIONTEST_WEBSITE'],
                       config['CONNECTIONTEST_INTERVAL'])

    print(helper.getCurrentTime(), "Hi，欢迎使用自动登陆系统")
    while True:
        helper.login()
        while True:
            can_connect = helper.canConnect()
            if not can_connect:
                print(helper.getCurrentTime(), "断网了...")
                helper.logout()
                time.sleep(2)
                helper.login()
            else:
                print(helper.getCurrentTime(), "一切正常...")
            time.sleep(helper.every)
        time.sleep(helper.every)