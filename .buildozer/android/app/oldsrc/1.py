from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# class TestApp(kivy.app.App):
#     def build(self):
#         return Label(text="Hello ")

class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.press_count = 1
        self.my_text = "Data inside TextInput"

    def button_press(self, button_pressed):
        # 信息显示在终端
        # print("Button Pressed", self.press_count, "Times")
        # print("文本框的内容:",self.text_input.text)
        self.press_count += 1
        # 通过text属性动态改变组建的值
        self.text_input.text = f"Button Pressed {self.press_count} Times"

        # 信息传递到label
        self.text_label.text = self.text_input.text

    def build(self):
        my_button = Button(text="Click me")
        my_button.bind(on_press=self.button_press)  # 给on_press事件绑定函数
        self.text_input = TextInput(text="text input")
        self.text_label = Label(text="waiting for button press")
        box_layout = BoxLayout(orientation="vertical")
        box_layout.add_widget(widget=self.text_label)
        box_layout.add_widget(widget=my_button)
        box_layout.add_widget(widget=self.text_input)
        return box_layout


app = TestApp(title="Hello")
app.run()
