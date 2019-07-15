import random
print("Welcome to the dice game!")
def sc():
    n = input("Enter a number\n")
    try:
        val = int(n)
        if val > 8 or val < 1:
            print('not valid input')
            sc()
        else:
            rollDice(val)
    except ValueError:
        print(f"{n} is not a number\n")
        sc()

def rollDice(n):
    i = 1
    sum = 0
    for n in range(n):
        dice = random.randint(1,6)
        print('dice', i, ':', dice)
        sum+= dice
        i +=1
    print(i)

sc()
