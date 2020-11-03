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

size_hint_y属性指定相机组件的高度是按钮的2倍。
类似的还有个size_hint_x可以设置宽度的。
"""


class PycamApp(kivy.app.App):
    def capture(self):
        camera = self.root.ids["camera"]
        camera.export_to_png("/storage/emulated/0/captured_image_kivy.png")

    def build(self):
        pass  # 隐式加载当前目录下的pycam.kv
        # return kivy.lang.Builder.load_file("camera.kv")  # 文件形式加载


app = PycamApp()
app.run()
