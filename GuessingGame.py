import random

def welcome():
    print("Welcome to the guessing game!")
    print("You will have to guess the randomly generated number before you run out of lives.")
    print("Got what it takes? Good luck!\n")

def player_options():
    print("Please select your desired difficulty:")
    print("1. Easy (10 lives)\n2. Medium (5 lives)\n3. Hard (3 lives)")
    global lives
    lives = 0

    while True:
        try:
            choice = int(input("\nEnter your choice between 1-3: "))
            if choice == 1:
                lives = 10
                print("\nEasy Mode Selected: 10 Lives")
                break
            elif choice == 2:
                lives = 5
                print("\nMedium Mode Selected: 5 Lives")
                break
            elif choice == 3:
                lives = 3
                print("\nHard Mode Selected: 3 Lives")
                break
            else:
                print("Please enter a valid number between 1 and 3.")
        except ValueError:
            print("That was an invalid input, try again.")

def game():
    global lives
    rand_num = random.randint(1, 100)

    while lives > 0:
        try:
            guess = int(input("Guess: "))

            if guess == rand_num:
                print(f"\n Congrats! You correctly guessed the number with {lives} lives remaining.")
                break
            elif guess > rand_num:
                print("Your guess is greater than the number, try going lower.")
            elif guess < rand_num:
                print("Your guess is lower than the number, try going higher.")

            lives -= 1
            if lives == 0:
                print("\n You ran out of lives :(")
                print(f"The correct number was {rand_num}. Better luck next time!")
                break
            else:
                print(f"You have {lives} lives remaining.\n")

        except ValueError:
            print("That was an invalid input, try again.")

def guessing_game():
    welcome()
    player_options()
    game()

guessing_game()
