'''
Author: y
Date: 2022-07-12 19:34:38
LastEditors: y
LastEditTime: 2022-07-12 21:16:34
'''
# -*- coding: UTF-8 -*-

import datetime
import os
import paramiko
import requests
import threading
import time
import win32api
import win32con
import win32gui
from PIL import ImageGrab
from pathlib import Path


def match_windows(win_title):
    """
    查找指定窗口
    :param win_title: 窗口名称
    :return: 句柄列表
    """

    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            win_text = win32gui.GetWindowText(hwnd)
            # 模糊匹配
            if win_text.find(win_title) > -1:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)  # 列出所有顶级窗口，并传递它们的指针给callback函数
    return hwnds


# 获取窗口信息
def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)    # 类名，标题
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle


def func():
    # 获取坐标
    (x1, y1, x2, y2), handle = get_window_pos('vscode')
    # 发送还原最小化窗口的信息
    # win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # 设为高亮
    win32gui.SetForegroundWindow(handle)
    # 目录不存在，则创建截图存放的目录
    if Path("images").is_dir() != 1:
        os.mkdir("images")

    # 开始截图
    # using the grab method
    pic = ImageGrab.grab((x1, y1, x2, y2))  # 指定截取坐标(左边X，上边Y，右边X，下边Y)
    # pic = ImageGrab.grab(None)
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
    # result = requests.post(url='http://127.0.0.1:5000/upload/img', data=data, files=files, headers={})
    # print(result.text)
    # os.remove("images/" + pic_name)

    # 开始定时任务
    timer = threading.Timer(60, func, [])
    timer.start()


func()
