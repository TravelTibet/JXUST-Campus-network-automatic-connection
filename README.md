# 江西理工大学校园网开机自动连接加断网重连保姆级教程（Window版本） 2023.5.20

# 前言：

  本教程也可适用于不同校园网用 GET 方法发送网页请求的高校，可按需修改。

# 前期准备：



1. 已经配置好python环境，这里采用的是python 3.10版本
2. 最好能有一个适合开发的IDE，这里用到的是pycharm最新版
3. 谷歌/微软浏览器，能够打开开发人员工具就行（非必选），这里用的是最新版的edge浏览器

# 一、打开学校的登录认证平台

​    这里附上网址：http://10.17.8.18/

![3adebcb7af0f4415ab9835619b9f01e6.png](https://i-blog.csdnimg.cn/blog_migrate/9144410a46482637f57f117e59c08efe.png)

​     打开之后先别登录，右键空白区域点击“检查”或者按“f12”打开开发人员工具，选到“网络”，把下面的“保留日志”给选上

​    

![a2229d67e3cb4242971cd1c3434aa058.png](https://i-blog.csdnimg.cn/blog_migrate/b41c4fd6f253436ad88919e198c93f55.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑



​    这时我们输入我们的账号密码，选择正确的运营商登录，然后就能在右边看到一堆信息，然后找到我们需要的“login”开头的登录信息，这个信息不一定在第一行，只要找到就行，然后点击表头，把那个“请求URL”后面的东西复制备用：

![c7ac1ba79674432bbb97b50a2f7438f8.png](https://i-blog.csdnimg.cn/blog_migrate/fd6c8996c9265d177582a12675a0c84f.png)



![7e47aef232aa4b8ca4454705f0ab928b.png](https://i-blog.csdnimg.cn/blog_migrate/04a71b3d52c3ec9f597300763b079e22.png)

​     经过观察发现，这个网页用get方法去响应，我们只需修改user_account，user_password，wlan_user_ip为自己的信息就能登录了。

# 二、打开PyCharm

​    新建一个python文件名为：“InternetConnect”

![d50ecac565434ea18696a2f45e573a6b.png](https://i-blog.csdnimg.cn/blog_migrate/aa3a17ea37b00f17c345bc86078ca1db.png)


​    因为我们的IP地址不一定不变，这里直接采用socket.gethostbyname()方法

```python
import socket
hostname = socket.gethostname() #获取本机计算机名称
ip = socket.gethostbyname(hostname) #获取本机ip
```


​    然后再把我们刚才的ULR地址处理一下，里面的user_account：

​    电信账号是：一卡通号@telecom

​    移动账号是：一卡通号@cmcc

​    联通账号是：一卡通号@unicom

​    密码就是一卡通密码

![e0460978c9bc4bb890ff808649b94794.png](https://i-blog.csdnimg.cn/blog_migrate/b3f0626a21441456a5b86ab628d289f9.png)

​     下面的代码要在“user_account=”后面加上自己的账号，“user_password=”后面接自己的密码

```python
a = 'http://eportal.jxust.edu.cn:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=&user_password=&wlan_user_ip='
```


```python
b = '&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=3995&lang=zh'
```

​     这时候我们在“a”和“b”这两个字符串中加入我们之前获得的ip地址，拼接成一个新的字符串ULR地址：

```python
url = a + ip + b
```

​     最后我们把这个ulr作为requests.get()的参数就可以了

```python
import requests  #用于向目标网站发送请求
r = requests.get(url) #ulr为你刚才复制的地址
r.close() 
```

​    这里附上（未完善的）代码：

```python
import requests  # 用于向目标网站发送请求
import socket
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
r.close()
```

​     如果第一行有报错的可以使用pip命令去安装我们的requests库，这里提供两个安装的办法：

##   1.直接在Pycharm里面安装

​      我们把鼠标放旁边就会提示我们去安装这个包

![f77550ef12994389923643e3f52a05fd.png](https://i-blog.csdnimg.cn/blog_migrate/6b61a4899998f06d164cb7f3f3dc858f.png)

##   2.采用pip命令下载

​    同时按下win+r键，输入cmd，打开我们黑漆漆的窗口后直接输入下面命令，如果有其他错误可以先试着升级一下pip，具体百度

```python
pip install requests
```

##    3.采用Pycharm终端下载

​     这一步和上面两步大同小异，就是下载的地方不一样。

​     终端具体位置如下图所示：

![fd69853c3dc84310ad57a81fd309987f.png](https://i-blog.csdnimg.cn/blog_migrate/5f9dba842d80a7ff6f6f82ccb292cc8e.png)

​    但是我们的代码还没完善，可能会有max retires error 11001 等错误信息（我一开始就是这里一直报错，虽然后面能正常联网，但是会弹出一个错误窗口，非常不美观！），这里我们还需要做一个异常的处理，代码如下，自行修改a的值（看上面）

​    附代码：

```python
try:
    import requests  # 用于向目标网站发送请求
    import socket
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
    r.close()
except requests.exceptions.ConnectionError:
    print("requests.exceptions.ConnectionError")
```



​    然后我们先去网页把账号注销，然后直接运行这个程序，刷新页面如果能正常显示“你已经成功登录”就能进行下一步，或者去前面找原因

![ad36e86279d5403ea3a15e02c6787de6.png](https://i-blog.csdnimg.cn/blog_migrate/f07d431f84deed4e7301defa6207b3f1.png)

# 三、断网检测部分

   利用ping指令与百度官网测试是否联通，直接给上最后代码，记得加上自己的用户名和密码，前面提到

##   完整代码

```python
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
```

# 四、打包python文件（可跳过）

​    如果不介意开机会弹出一个黑色框（所谓的“终端”），这步可跳过，不过可能**有点影响美观！**

​    用pip命令安装pyinstaller工具包来打包，win+r弹出输入cmd，直接输入：

```python
pip install pyinstaller
```

​    期间有问题都可以百度自行解决，等待安装好之后我们可以在PyCharm下面找到“终端”打开

![f1b2f7e54f2e44d193c25b522c93acd0.png](https://i-blog.csdnimg.cn/blog_migrate/31b02eff7f0bc0901fbf1a1b4e9768ce.png)

​     在这里面输入:

```python
pyinstaller -F -w InternetConnect.py
```
​     其中-F表示对单个python文件打包，-w表示不显示终端窗口(这一步可以增强体验)然后“InternetConnect”就是我们的python源文件    

![e5c3d679947841a5bd0a71d8fce07eb7.png](https://i-blog.csdnimg.cn/blog_migrate/ca12954951d4532cfa66aed2103b48b3.png)
​     然后在PyCharm找到我们的InternetConnect.py文件右键>打开于>文件资源管理器

![d9f36b0452364aeea2ad37999a392827.png](https://i-blog.csdnimg.cn/blog_migrate/800c682f453319d13c1c81a03f58c19c.png)

​     然后打开“dist”文件夹里面就有一个打包好的名为“InternetConnect.exe"的文件![11a4c90957bd4663a78c03e746fd672e.png](https://i-blog.csdnimg.cn/blog_migrate/7a612ebfda8a9e8b1884246417ce40ba.png)
​     右键复制文件地址备用

![b21b6950e8ce414e8eb932eb59cdcdb8.png](https://i-blog.csdnimg.cn/blog_migrate/1d10db88e2e7fd6193972d58d94002b8.png)

#  五、添加到开机启动项

##    打开我们的“计算机管理”

##     win10：

​    方法一：

　　1、快捷键Window徽标键+R键，打开“运行”程序。

　　2、运行，打开:输入compmgmt.msc敲回车。

　　3、就可以打开“计算机管理”。

　　方法二：

　　计算机右单击弹出快捷菜单选择管理，就可以打开计算机管理。

　　方法三：

　　任务栏搜索框里搜索计算机单击计算机管理，就可以打开计算机管理。

　　方法四：

　　开始右单击弹出快捷菜单选择计算机管理就可以打开计算机管理。

##     win11:

​    按win+x打开“计算机管理”，选择>系统工具>任务计划程序

​    

​    然后执行下面操作

![4fe0aadd74c440d9ab5d95ddecdf5a30.png](https://i-blog.csdnimg.cn/blog_migrate/2267900c7cef151a2e01ab7a3b3a2e6b.png)



​     在右边点击“创建任务”

![32958b003a104f1bb68f0ca46068091e.png](https://i-blog.csdnimg.cn/blog_migrate/192bedd7b5697380d0d6eabb2ca4a7bf.png)

​     \>常规 这里名称还是改为“InternetConnect”，注意勾选“只在用户登录时运行”，下图配置可改为windows10

![4ea3259e98b943b79222f3c314bb8429.png](https://i-blog.csdnimg.cn/blog_migrate/d80abd6af5c9702baa8da9457a0ac92d.png)

 \>触发器>新建一个触发器，按如下设置：

![e6e79922214a464591b760f3086d32c6.png](https://i-blog.csdnimg.cn/blog_migrate/bf0c5751b18307829956d2effc0a7751.png)

 \>操作>新建一个操作 按下图操作，图中的程序或脚本下面的空行是我们刚才复制的InternetConnect.exe文件的地址，（如果第三步跳过的，这里就是你python文件的路径），粘贴进去就行

![51428f3ce2a5471da8caeb8f2ac0406f.png](https://i-blog.csdnimg.cn/blog_migrate/d1609e16edb8838826d5a8bed915cad8.png)

 \>操作 注意这里要勾选：只有在以下网络连接可用是才启动”>任何网络，这样我们只要连上网络就会自动进行一个校园网的认证操作，（或者选择为连上学校WiFi“JXUST-WIFI”，仅适用于用WiFi连接校园网）

![e33e2dec888c4fa699ea9d65aa772547.png](https://i-blog.csdnimg.cn/blog_migrate/e42984c09184066780b5f36767d35a63.png)
 \>设置 设置可以根据情况修改，但是第一个必须勾选

![e208b6d1366f4c6bbeb3de1a3d8a16d6.png](https://i-blog.csdnimg.cn/blog_migrate/c556f6c4ea51ee06e1c8427a0ab472dd.png)

##     

​    至此，大功告成，我们重启一下电脑登录以后等待几秒就能连上网络，大家快去试试吧~

# 注意事项：

  本人文章转载注明出处!

   全文的代码都没添加用户名和密码，需要自己添加

​    能力有限目前只能满足三江校区需求！！！

​    程序一旦启动就会一直自动认证，想要注销认证信息的同学先通过任务管理器把 InternetConnect.exe 的程序关闭！！！

​    
# 修改日志：

   2023.5.24 增加了断网重连部分代码，修改部分错误

   2023.6.22 把异常捕获的具体删除，能够捕获更多的异常类型，避免偶尔因为校园网已经连上了一台设备而引起的异常

   2023.12.3 第二部分多增加了第三种下载requests库方法

   2023.12.4  增加前言部分，扩大本教程适用范围

# 参考文章：

- http://t.csdn.cn/HRIuz
- https://blog.csdn.net/m0_67829475/article/details/130782935
