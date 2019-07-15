arr=[]
i=0
while True:
    s=input("Enter a String:")
    if s=="GEN":
        if arr==[]:
            print("Nothing to display.")
            break
        else:
            for i in range(len(arr)):
                print("<p>"+ arr[i]+"</p>")
                i+=1
                break
            else:
                if s =="":
                    arr.append("Nothing to display.")
                else:
                    arr.append(s)
