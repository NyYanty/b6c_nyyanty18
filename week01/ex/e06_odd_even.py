import re
exit= False
while(exit==False):
    user_input = input("Enter a number: \n>> ")
if(user_input.lower()=="exit"):
    break
elif(re.findall("[a-zA-Z.]",user_input)):
    print(f"{user_input} is not a valid number.")
    continue
else:
   intNumber = int(user_input)
   if(intNumber %2 == 0):
    print(f"{intNumber} is EVEN")
   else:
       print(f"{intNumber} is ODD")


