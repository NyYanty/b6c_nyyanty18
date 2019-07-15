b= input("Enter a String:")
temp=""
if len(b)==0:
    print("Empty")
else:
    for x in b:
        if ord(x)>64 and ord(x)<91:
            temp=temp+x.lower()
        elif ord(x)>96 and ord(x)<123:
            temp=temp+x.upper()
        else:
            temp=temp+x
            print(temp)

