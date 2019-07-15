import random

win_num = random.randint(1, 88)
name = input("Hello, what is your name?\n")
print(f"Well {name}, try to guess the number I have in mind!")
count_guess = 0

def k():
    global count_guess
    guess_num = int(input())
    count_guess += 1
    if guess_num < win_num:
        print("Too low, try again")
        k()
    elif guess_num > win_num:
        print('Too high, try again')
        k()
    else:
        if count_guess == 1:
            print("You won in 1 turn only, that's amazing!")
        else:
            print(f"It took you {count_guess} turns to guess my number which was {win_num}!")
            play_again = input("Do you want to play again?[Y/N]\n")
            if play_again.upper() == "N":
                print(f"Ok, bye{name}! See you later!")
            elif play_again.upper() == 'Y':
                count_guess = 0
                k()
            else:
                print("Sorry, I did not understand.Let me repeat:")


k()
