
# exception handling for try and  expect block

'''a=input("enter a number")
print(f"Multiplication table of {a} is ")

try:
   for i in range(1,11):
       print(f"{int (a)}x{i}={int (a)*i}")
    
    
except Exception as e:
    print(e)    
    
print("some imp line of code ")
print("end of program")    '''



try:
    num=int(input("enter an integer"))
    
    a=[6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")
    
    
except IndexError:
    print("IndexError")        
    
    