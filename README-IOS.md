#  前言：

   之前写了一个window版本的自动连接，现在发现ios的快捷指令功能很强大，很方便就能完成这个功能。老规矩外校也可以根据需求改，就改一下即可。

   

# 一、下载我分享的快捷指令



​    （这里没有处理连接超时、自动重连的问题，一般连上之后不会再有问题）

​    如果是第一次下载别人分享的快捷指令，还需要点下面的快捷指令首次安装配置一下。
 [快捷指令首次安装配置![img](https://csdnimg.cn/release/blog_editor_html/release2.3.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=O83A)https://www.rcuts.com/382.html](https://www.rcuts.com/382.html)

# 二、修改相关文本信息

​    我的快捷指令部分信息不完整需要自行填写

##    1.填写自己的教务系统账号

   ![62919c2153514d30843d582e0b85df90.png](https://i-blog.csdnimg.cn/blog_migrate/b2eb3127159782ab626a53ca00570d54.png)
##    2.填写教务系统密码

![083c8ae7a2904fd3991be51455dc43a6.png](https://i-blog.csdnimg.cn/blog_migrate/97533407aba0191a25369dfb1fb49f1d.png)
##    3.填写自己的运营商账户代码

   中国电信填写：telecom

   中国移动填写：cmcc

   中国联通填写：unicom

![55bf6222f18548ab9eaa77f43d6024f4.png](https://i-blog.csdnimg.cn/blog_migrate/a2cf508470e90a65fa68266fb38ad235.png)

#  三、打开自动化指令

​    这里只需要我们在自动化里面设置当连接到学校的wlan  JXUST-WLAN时自动运动上面的快捷指令就行

![f9c290041cd34be199b6cbea8bbb3a51.png](https://i-blog.csdnimg.cn/blog_migrate/0d8542db55df70684ce4025a206c4e4d.png)

# 四、注意事项

​    有各种连不上的问题可以把多试几次一般都可以，不行的话私信联系。

​    这里在设置里面**不要**把JXUST-WLAN的自动登录和自动加入打开，否则多次运行账号短期时间内会出现请求次数过多的异常！！！！

![826f1c266e534de59fab15b16382afbc.jpeg](https://i-blog.csdnimg.cn/blog_migrate/50bad2afd8e72af5218b3589a464e45a.jpeg)



# 五、修改日志：

1. 2023.12.5 增加重复运行，避免偶发问题导致运行有误，还增加了一个新发现的注意事项