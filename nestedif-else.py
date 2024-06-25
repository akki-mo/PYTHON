num=int(input("enter a number"))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<10):
        print("num is between 1-10" )
    elif(num>10 and num<=20):
        print("num is between 11-20" )
    else:
        print("number is greater then 20")
else:
    print("number is zero")                    