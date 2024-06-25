'''def average(a=9,b=1):
    print("the average is :",(a+b)/2)
    
average(b=9)  '''


def average(*numbers):
    sum=0 
    for i in numbers: 
        sum=sum+i
    print("average is : ",sum/len(numbers))
    
    
    
    
average(5,6,1)

# variable length argument

'''def name(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])  
    
    
name(mname="jagannath",lname="mohite",fname="akshay")'''    
    
            