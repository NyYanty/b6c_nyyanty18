str = input("Enter your secret message:")
temp = ""
if len(str) == 0:
    print("Nothing to encode!!")
else:
    for x in str:
        if ord(x) > 64 and ord(x) <= 77 or ord(x) > 96 and ord(x) <=109:
            temp = temp + chr(ord(x) - 13)
        elif ord(x) > 77 and ord(x) < 91 or ord(x) > 109 and ord(x) < 123:
            temp = temp + chr(ord(x) + 13)
        else:
            temp = temp + x
    print(temp)
