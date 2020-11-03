# -*- coding: utf-8 -*-
# @Time : 2020/11/3 4:53 下午
# @Author : chenxiangan
# @File : main.py
# @Software: PyCharm
import kivy.app
import kivy.lang
import os
import requests
from PIL import Image

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
    def cam_size(self):
        """
        告诉服务器要发送的图片的大小
        """
        camera = self.root.ids["camera"]
        cam_width_height = {"width": camera.resolution[0],
                            "height": camera.resolution[1]}
        ip_addr = self.root.ids["ip_address"].text
        url = "http://" + ip_addr + ":9999/camSize"
        try:
            self.root.ids["cam_size"].text = "Trying to Establish a Connection...."
            requests.post(url, params=cam_width_height)
            self.root.ids["cam_size"].text = "Done."
            self.root.remove_widget(self.root.ids["cam_size"])
        except requests.exceptions.ConnectionError:
            self.root.ids["cam_size"].text = "Conneciton Error!Make sure" \
                                             "Server is Active."

    def capture(self):
        camera = self.root.ids["camera"]
        print(camera.x, camera.y)
        pixels_data = camera.texture.get_region(x=camera.x, y=camera.y, width=camera.resolution[0],
                                                height=camera.resolution[1]).pixels
        # 将数组转为图片
        # image = Image.frombytes(mode="RGBA",size=(int(camera.resolution[0]), int(camera.resolution[1])), data=pixels_data)
        # image.save('out.png')
        ip_addr = self.root.ids['ip_address'].text
        url = 'http://' + ip_addr + ':9999/'
        files = {'media': pixels_data}
        try:
            self.root.ids['capture'].text = "Trying to Establish a Connection..."
            requests.post(url, files=files)
            self.root.ids['capture'].text = "Capture Again!"
        except requests.exceptions.ConnectionError:
            self.root.ids['capture'].text = "Connection Error! Make Sure Server is Active."

    def build(self):
        pass  # 隐式加载当前目录下的pycam.kv
        # return kivy.lang.Builder.load_file("camera.kv")  # 文件形式加载


app = PycamApp()
app.run()
