from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

"""
创建一个label来接收button点击之后的结果
总布局：vertical 也就是一行一行的

这里一共三行

第一行是label，显示button点击之后的结果
第二行是一个layout，然后这个layout又进行了竖排的拆分，左边子元素是input，右边是button，button点击之后就是获取左边子元素的text内容
第三行一样


"""


# class TestApp(kivy.app.App):
#     def build(self):
#         return Label(text="Hello ")

class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.press_count = 1
        self.my_text = "Data inside TextInput"

    def button1_press(self, button_pressed):
        self.text_label.text = self.text_input1.text

    def button2_press(self, button_pressed):
        self.text_label.text = self.text_input2.text

    def build(self):
        self.text_label = Label(text="waiting for button press")
        self.text_input1 = TextInput(text="TextInput 1")
        my_button1 = Button(text="Click me")
        my_button1.bind(on_press=self.button1_press)

        self.text_input2 = TextInput(text="TextInput 2")
        my_button2 = Button(text="Click me")
        my_button2.bind(on_press=self.button2_press)

        box_layout = BoxLayout(orientation="vertical")  # 竖直方向
        box_layout1 = BoxLayout(orientation="horizontal")  # 水平方向的
        box_layout1.add_widget(widget=self.text_input1)
        box_layout1.add_widget(widget=my_button1)

        box_layout2 = BoxLayout(orientation="horizontal")
        box_layout2.add_widget(widget=self.text_input2)
        box_layout2.add_widget(widget=my_button2)

        box_layout.add_widget(self.text_label)
        box_layout.add_widget(box_layout1)
        box_layout.add_widget(box_layout2)
        return box_layout


app = TestApp(title="Hello")
app.run()
