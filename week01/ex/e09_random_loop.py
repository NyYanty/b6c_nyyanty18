a= input("Enter a number:")
if a=="":
    import random
    print(random.randint(0,99))
else:
    import random
    for x in range (0, int(a)):
        print(random.randint(0,99))
