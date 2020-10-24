# -*- coding: utf-8 -*-
# @Time : 2020/10/19 22:48


import os
from datetime import datetime


def filePath(fileDir="data", fileName="login.yaml"):
    base_root = os.path.dirname(os.path.dirname(__file__))

    return os.path.join(base_root, fileDir, fileName)


# print(filePath("data", "login.yaml"))
# print(filePath("config", "config.yaml"))


def writeContent(content):
    # print("写的时间:", datetime.now())
    with open(filePath(fileName="bookID"), "w") as f:
        f.write(str(content))


# writeContent("1")

def readContent():
    # print("读的时间:", datetime.now())
    with open(filePath(fileName="bookID"), "r") as f:
        return f.read()
