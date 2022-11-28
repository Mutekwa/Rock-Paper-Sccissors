from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        # add widgets to window
        self.window.cols = 1

        # image widget
        self.window.add_widget(Image(source="logo.jpg"))

        # label widget
        self.greeting = Label(text="What is your name?")
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(text="GREET")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self,instance):
        self.greeting.text = "Hello" + self.user.text + "!"



if __name__ == "__main__":
    SayHello().run()
