import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class RPS(App):
    def build(self):
        self.window = GridLayout
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # self.window.add_widget(Image(source="RPS.jpg"))

        self.img = Image(source="RPS.jpg")
        self.window.add_widget(self.img)

        self.rps = Label(text="Rock Paper Scissors!",
                         font_size=18,
                         color='#00ff00'
                         )
        self.window.add_widget(self.rps)

        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.user.add_widget(self.user)

        self.button = Button(
            text="Play",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE"
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


if __name__ == "__main__":
    RPS().run()


def rock_paper_scissors():
    while_playing = True
    while while_playing is True:
        user_input = input("Enter r,p or s for rock, paper, and scissors respectively:  ")
        possible_values = ["r", "p", "s"]
        # computer makes its choice
        computer_input = random.choice(possible_values)

        print(f'Computer chose {computer_input} and you chose {user_input}')

        # same inputs
        if user_input == computer_input:
            print(f'Both players chose {user_input}, Its a tie')
        # different inputs
        elif user_input == 'r':
            if computer_input == 's':
                print("Rock smashes scissors, You win!")
            else:
                print("Paper covers rock, Computer wins!")
        elif user_input == 'p':
            if computer_input == 'r':
                print("Paper covers rock, You win!")
            else:
                print("Scissors cuts paper, Computer wins!")
        elif user_input == 's':
            if computer_input == 'p':
                print("Scissors cuts paper, You win!")
            else:
                print("Rock smashes Scissors, Computer wins")
        choice = input("Would you like to keep playing?(y or n)")
        if choice == 'y':
            while_playing = True
        elif choice == 'n':
            while_playing = False


rock_paper_scissors()
