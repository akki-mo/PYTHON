'''list1=[1,2,3,4,5,6,7]
list2=["red","green","blue","yellow"]
print(list1)
print(list2)'''


'''marks=[3,5,6,"akshay",True]
marks.append("akshay")
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

print(marks)
print(marks[1:])
print(marks[1:4])
print(marks[1:4:2])'''



'''if "akshay" in marks:
    print("yes")
else:
     print("no")   

if "sha" in "akshay":
    print("yes")
else:
    print("no")'''
    
    
    
    #list comprehension

'''list1=[i*i for i in range(10)]
print(list1)    

list2=[i*i for i in range(10) if i%2==0]
print(list2)'''



names=["akshay","pratik","virajas","shyam","kevin","yash","achyut","kshudhanshu"]
nanmewith_0=[item for item in names if (len(item)>6)]
print(nanmewith_0)