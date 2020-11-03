# -*- coding: utf-8 -*-
# @Time : 2020/11/3 4:24 下午
# @Author : chenxiangan
# @File : main.py
# @Software: PyCharm

"""
using kv language
需要注意的是，如何在Python代码中访问在KV文件中创建的小部件。给小部件一个ID后，您可以使用root引用它。
ids是个字典。关键字root指的是KV文件中的根框布局小部件。通过按所需小部件的ID为字典建立索引，它将被返回，因此我们能够访问它的属性并覆盖它
注意 kv文件的层级结构不能写错 必须对其。换行等写法类似python
"""
import kivy.lang
from kivy.app import App

kv_string = """
BoxLayout:
    orientation: "vertical"
    Label:
        text: "Waiting for Button Press"
        id: text_label
    BoxLayout:
        orientation: "horizontal"
        TextInput:
            text: "TextInput 1"
            id: text_input1
        Button:
            text: "Click me"
            on_press: app.button1_press()
    BoxLayout:
        orientation: "horizontal"
        TextInput:
            text: "TextInput 2"
            id: text_input2
        Button:
            text: "Click me"
            on_press: app.button2_press()
"""


class TestApp(App):
    def button1_press(self):
        self.root.ids["text_label"].text = self.root.ids["text_input1"].text

    def button2_press(self):
        self.root.ids["text_label"].text = self.root.ids["text_input2"].text

    def build(self):
        # return kivy.lang.Builder.load_file("1.kv")  #文件形式加载
        return kivy.lang.Builder.load_string(kv_string)  # 字符串形式加载


app = TestApp()
app.run()
