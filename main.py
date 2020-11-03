# -*- coding: utf-8 -*-
# @Time : 2020/11/3 4:53 下午
# @Author : chenxiangan
# @File : main.py
# @Software: PyCharm
import kivy.app
import kivy.lang

try:
    # 这个只有在手机上有用
    from android.permissions import request_permissions, Permission

    request_permissions([
        Permission.CAMERA,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])
except ImportError:
    pass

"""
如果编译成app
需要在buildozer.spec文件加入
android.permissions=Camera
来获取权限
"""


class TestApp(kivy.app.App):
    def build(self):
        return kivy.lang.Builder.load_file("camera.kv")  # 文件形式加载


app = TestApp()
app.run()
