## 东南大学校园网自动登录辅助程序

### 依赖环境:
- Python 3
- [yaml](https://pypi.org/project/PyYAML/) : `pip install pyyaml`


### 特性:
- 自动登录校园网
- 断线自动重连

### 配置文件说明:
- YKTBH: 一卡通号
- PASSWORD: 密码
- MACAUTH: 是否启用
- CONNECTIONTEST_WEBSITE: 用来检查联网情况的网页,默认百度首页(完全符合百度的主要功能)
- CONNECTIONTEST_INTERVAL: 检查联网情况的时间间隔,默认90s