import random

def welcome():
    print("Welcome to the guessing game! You will have to guess the randomly generated word before you run out of lives.\nGot what it takes? Good Luck")
def rand_number():
    rand_num = random.randint(1, 100)

def player_options():
    difficulty = input("What level of difficulty would you like to use? \nEasy (10 lives)\nMedium (5 Lives)\nHard (3 Lives)\n")
    
    while True:
        lives = 0
        if difficulty == 'Easy':
            lives = 10
            print("Easy Mode Selected: 10 Lives")
            break
        elif difficulty == 'Medium':
            lives = 5
            print("Medium Mode Selected: 5 Lives")
            break
        elif difficulty == 'Hard':
            lives = 3
            print("Hard Mode Selected: 3 Lives")
            break
        else:
            print("That was an invalid input, try again!")




def guessing_game():
    welcome()
    rand_number()
    player_options()

guessing_game()