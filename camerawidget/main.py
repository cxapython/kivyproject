# -*- coding: utf-8 -*-
# @Time : 2020/11/3 4:53 下午
# @Author : chenxiangan
# @File : main.py
# @Software: PyCharm
import kivy.app
import kivy.lang

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
