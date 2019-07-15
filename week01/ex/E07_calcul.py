total=0
while True:
   a=input("Enter a number:")
   if a=="exit":
       break
   else:
       try:
           a=int(a)
           total+= a
           print(total)
       except:
           print(total)
