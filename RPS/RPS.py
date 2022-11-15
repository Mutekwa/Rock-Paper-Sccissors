import random


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
