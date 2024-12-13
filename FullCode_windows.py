import re
import requests  # 用于向目标网站发送请求
import socket
 
 
def Statu():  # 监测是否断网
    try:
        q = requests.get("http://www.baidu.com", timeout=500)
        m = re.search(r'STATUS OK', q.text)
        if m:
            print("Connect Success")
            return 0
        else:
            print("Connect Failed")
            return 1
    except :
        pass
def login():
    try:
        # 获取本机计算机名称
        hostname = socket.gethostname()
        # 获取本机ip
        ip = socket.gethostbyname(hostname)
        a = 'http://eportal.jxust.edu.cn:801/eportal/portal/login?callback=dr1003&login_method=1&' \
            'user_account=&user_password=&wlan_user_ip='
        b = '&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=' \
            '&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=3995&lang=zh'
        url = a + ip + b
        r = requests.get(url)
    except :
        pass
 
 
while True:
    if Statu():
        login()
    else:
        print("ConnectSuccess")
