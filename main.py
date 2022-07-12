'''
Author: y
Date: 2022-07-12 19:34:38
LastEditors: y
LastEditTime: 2022-07-12 21:16:34
'''
# -*- coding: UTF-8 -*-

import paramiko
from PIL import ImageGrab
import threading
import time
import datetime
import os
import requests
from pathlib import Path


def func():
    # 目录不存在，则创建截图存放的目录
    if Path("images").is_dir() != 1:
        os.mkdir("images")

        # 开始截图
    # pic = ImageGrab.grab((200, 100, 1000, 800))  # 指定截取坐标(左边X，上边Y，右边X，下边Y)
    # using the grab method
    pic = ImageGrab.grab(None)
    pic_name = time.strftime('%Y%m%d%H%M%S') + '.jpg'
    pic.mode = 'RGB'
    pic.save("images/" + pic_name)
    # pic.show()
    print("show, now: ", datetime.datetime.now())

    # 通过sftp文件上传
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect("120.77.170.139", 22, "root", "Ss804806s")
    # sftp = ssh.open_sftp()
    # sftp.put(pic_name, "/www/wwwroot/images/" + pic_name)
    # print("完成发送")
    # os.remove(pic_name)
    # ssh.exec_command("python /www/wwwroot/ocr.py")  # 执行服务器上相应脚本

    # 模拟浏览器POST文件上传
    # files = {'file': (pic_name, open("images/" + pic_name, 'rb'), 'image/png')}
    # data = {
    #     # "computer": 1
    # }
    # result = requests.post(url='http://127.0.0.1:5000/index', data=data, files=files, headers={})
    # print(result.text)
    # os.remove("images/" + pic_name)


    # 开始定时任务
    timer = threading.Timer(60, func, [])
    timer.start()


func()
