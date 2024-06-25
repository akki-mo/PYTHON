   # palindrome number 
'''1)  num= int (input("enter number:"))
i= num
rev=0

while(num >0):
      dig= num%10
      rev =rev *10 + dig
      num = num//10
if (i==rev):
    print(" the {0} is the palindrome".format(temp))
else:
    print("the {0} is the not palindrome".format(temp))'''  


'''my_str=int(input("enter a number:"))

reverse  = int (int (my_str[::-1]))
if my_str == reversed :      
    print ("it is palindrome")
else:
    print(" it is not palindrome") '''   
    
    
    
    #factorial number


'''num=int(input("enter a number"))
fact=1

for i in range(num,1,-1):
 
      fact=fact*i
 
 (while(num>= 1):   #using while loop
         fact=fact*num
          num-=1 ) 
     print("factorial",fact'''
     
     
     #prime number 
     
    

'''num=int (input("enter the number"))

if num==i:
    print("it is prime")
else :
    print("it is not prime")'''
     
   


 # combination of 3 digit
 # factorial number
'''def show(roll,name,percentage):
    print("Roll",roll)
    print("name",name)
    print("percentage",percentage)
    
    show(name="ramesh",roll=101,percentage=89.26)'''
    


#functions in python
'''def caldiscount(distper=2):
    price=int (input("priceof the product:"))
    dic=price*distper/100
    print("discount per:", distper)
    print("discount",dis)'''
    
    
    #string
    
'''def show(*args):
    print(args[3])
    
show(101,"MCA","PUNE", 89.99)'''

# function(code optimization)

'''def revnum(number):
    rem=number%10
    #if number!=0:
    print(rem,end="")
    if number!=1 :
        #print (rem,end="")
       revnum(number//10)
revnum(102)'''
       
 #reverse string
'''def strrev(str,len):
    if len!=0:
        
       print(str[len-1],end="")     
       strrev(str,len=len-1)
    
      
strrev("MITWPU",6)'''

# string
'''strvar =""
    
strvar="mitwpu pune"
print(strvar)
#print(type(strvar))
#print(strvar.upper())
#strvar="SOB pune"
#print(strvar)
temp=strvar.upper
print( "Reverse of",strvar,"is",temp)

#print(strvar[0])
#print(" No of char",len(strvar))
#for with in 
for ch in strvar:
    print(ch,end =" ")'''
# indexed access using for 
'''strlen=len(strvar)
for i in range(0,strlen,2):
    print(strvar[i], end=" ") 
strvar =""'''
    
'''strvar="mitwpu pune"
print(strvar)
flag=1
for ch in strvar:
    if flag==1:
         print(ch,end=" ")
         flag=0
    else:
        flag=1  '''
        
        #output: mitwpu pune
                #m t p   u e '''
        
        # slicing in string
#str   [i    :    j]
     #i=inclusing index   j=excluding index(n-1)        
'''str="MITWPU PUNE"
#temp=str[:6]
str=str[::-1]
print(str) '''             
         #********************************sting toknized****************************
'''def revword(word):
    print(word[::-1],end=" ")
    
userip=input("enter sentence")             
for word in userip.split():
    revword(word)'''
    
 #lists using pythons 
 
'''lvar=[101,"amit",89.90]

print(lvar[1])
print(lvar)
print(len(lvar))


for x in lvar:
    print(x, end =" ")
 
for x in range(0,len(lvar)):
    print(lvar[x])'''
    # 
    
'''alist=["amit",101,89.90,101,"abc@home.com"]
#print(alist[3:4])
#print(alist[:3])
#print(alist[-4:-2])
print(alist[::-1])'''
  
  #reversing the list
  
'''alist=["amit","mitwpu","MCA","pune","abc@home.com"]
for x in alist:
    print(x[::-1],end=" ")
    '''
    
    
 #extend list
 
'''alist = ["amit",101, "MCA"]
blist =list((89.98,"1 class", "Div A")) 
print(alist)
print(blist)
alist.extend(blist) 
print("after extend :", alist)''' 

           #output  :   ['amit', 101, 'MCA']
                       # [89.98, '1 class', 'Div A']
                       # after extend : ['amit', 101, 'MCA', 89.98, '1 class', 'Div A']
           

#remove

'''alist=["amit", 101 , "MCA","pune",101 ]
print("before remove 101" , alist )
alist.remove("amit")
print ("after remove pune ", alist ) '''  

           #  output   :before remove 101 ['amit', 101, 'MCA', 'pune', 101]
                        #after remove pune  [101, 'MCA', 'pune', 101]


'''def removewords(word,list):
    while word in alist:
        alist.remove(word)
    print(alist)
alist=["the","name", "of", "the" ,"school" ,"is", "the" ]        
removewords("the", list)'''


#output: ['name', 'of', 'school', 'is']'''


'''alist=["amit", 101 , "MCA","pune",101 ]
print("before pop(4)",alist)
alist.pop()            # pop a element using without index
#alist.pop(-1)
print("after pop(4)",alist)'''

#output :before pop(4) ['amit', 101, 'MCA', 'pune', 101]
        #after pop(4) ['amit', 101, 'MCA', 'pune']'''
        
#homework       
   # tuple 
    #set
    #dictionary    #file handling
#1) tuple
'''tvar=("ajay","MIT","MCA",89.90,101)
temp=("pune",)
print(type(tvar))
print(type(temp)) 
for var in tvar:
    print(var)'''   #output :  <class 'tuple'>
                            #<class 'tuple'>
                            #ajay
                            #MIT
                            #MCA
                            #89.9
                            #10)
'''for i in range (0,len(tvar)):
    print(tvar[i],end=" ") '''    #output  : ajay MIT MCA 89.9 101 

#using flag
'''flag=True
for var in tvar:
    if flag ==True:
        print(var)
        flag=False
    else:
        flag=True '''
        
               #output  : ajay
                        #MCA
                        #101
                
'''name="amit"
tvar[1]=name
print(tvar)'''
#
'''tvar1=(101,"ajay","MIT-MCA")
tvar2=(101,89.90)
tvar1=tvar1+tvar2
print(tvar1)'''

            #output : (101, 'ajay', 'MIT-MCA', 101, 89.9)

#
'''tvar=(101, 'ajay', 'MIT-MCA',"ajay", 101, 89.9,"pune")
#print(tvar[::-1])
#print(tvar.count("MIT-MCA"))
for var in tvar:
    
    print(var," ",tvar.count(var))'''
                    
                     #output  : 101   2
                                #ajay   2
                                #MIT-MCA   1
                                #ajay   2
                                #101   2
                                #89.9   1
                                #pune   1
    
    
    
'''tvar=(201,99,89,56,333,41,90)
print("tuple items :",tvar)
alist=list(tvar)
print(" list items sorted :",alist)
tvar=tuple(alist)
print("tuple item")'''

         #output :tuple items : (201, 99, 89, 56, 333, 41, 90)
                  #list items sorted : [201, 99, 89, 56, 333, 41, 90]
                     #tuple item


#set

'''sobj={1,2,3,"akshay","virajs","omkar","ajay"}
setvar=set()
print(type(sobj))
print("sobj : ",sobj)
for val in sobj:  
    print(val,end=" ") '''
        
        #output : akshay 1 2 3 ajay virajs omkar 
        
 #adding the element in set       
'''sobj={"amit"}
sobj.add("MCA")
sobj.add("PUNE")
sobj.add(101)
sobj.add(202)
print("set : ",sobj) '''

    #output  : set :  {101, 202, 'MCA', 'amit', 'PUNE'}

#removing the element in set


'''sobj={"amit",101,"MCA","PUNE",89.9}
print("before set : ",sobj)
sobj.remove("PUNE")
print("after set : ",sobj)'''


       #output  : before set :  {'amit', 101, 'MCA', 'PUNE', 89.9}
                  #after set :  {'amit', 101, 'MCA', 89.9}

# deleting the element from set

'''sobj={"amit",101,"MCA","PUNE",89.9}
print("set : ",sobj)
del sobj
print(" set after del : ",sobj) '''          


            #output  : output not generated because delete element is not allow
             
             
'''set1={1,2,3,4}
print("set : ",set1,"len : ",len(set1))
set2=("A","B","C","D",3,4)
print("set2 : ",set2,"len : ",len(set2))
set1.update(set2)


print("set : " ,set1,"len : ",len(set1))'''

                        #output  : set :  {1, 2, 3, 4} len :  4
                            #set2 :  ('A', 'B', 'C', 'D', 3, 4) len :  6
                            #len :  8


'''set1={1,2,3,4}
alist=["A","B","C","D",1,2,3]
strvar={"AB CD"}
tupvar={"ABCD" ,}
#temp,=tupvar
#set.update(temp)
#print(type(temp))

set1.update(strvar)
print("set1 : " ,set1,"len : " ,len(set1)) '''    #output :   set1 :  {1, 2, 3, 4, 'AB CD'} len :  5  




#string constant
#unique element from the list
#list items


'''set1={1,2,"A","B",3,4}
set2={2,"A","B","C",4}
set3=set1.union(set2)
print("set3 : ",set3,"len : ",len(set3))'''



                #output  :  set3 :  {1, 2, 3, 4, 'B', 'C', 'A'} len :  7
                
                
'''set1={1,2} 
set2={1,2,"A","B","C",4}

if set.issubset(set2):
    print("true sub set")
else:
    print("false not a sub set")'''
    
           #output :  File "e:\python\class program\classprogram.py", line 393, in <module>
           # if set.issubset(set2):
           # ^^^^^^^^^^^^^^^^^^
           # TypeError: set.issubset() takes exactly one argument (0 given)
    
    
#dictionary in pyhton
                  
                  
                                                                 #hybernet todays learning
                                                                
#dictionarty is muteable and
# it can be changeable 
# it does not allow duplicate element .
# it is collection is ordered 
#it shows that key:value pair     


     #todays leaen

#{#what is sheter and getter          
#data acess object      
#design pattern

#map data structure }


'''dictvar={"name":"amit","program":"MCA","per":89.90}   #refer to current key-value
#dictvar={1:"amit",2:"MCA",3:89.90,"city":["pune","kothrud","MIT"]}
print(dictvar)
#print(dictvar["name"])
dictvar["name"]="rajesh"
dictvar["city"]="pune"
print("after name change :",dictvar)

for key in dictvar:
    print(key, ":",dictvar[key])'''
    
            #output : {'name': 'amit', 'program': 'MCA', 'per': 89.9}
                     # after name change : {'name': 'rajesh', 'program': 'MCA', 'per': 89.9, 'city': 'pune'}
                     # name : rajesh
                     # program : MCA
                     # per : 89.9
                     # city : pune
    
    
    
'''dictvar={"name":"amit","program":"MCA","per":89.90 ,"city":"pune"}   #refer to current key-value
    
print(dictvar["city"])
print(dictvar.get(1))        #it is nonetype datatype



for  key  in dictvar.keys():
    print(key,":",dictvar.get(key))'''
                                  
                            #output : pune
                                   # None
                                    #name : amit
                                    # program : MCA
                                    # per : 89.9
                                    # city : pune
                                    
'''dictvar={"name":"amit","program":"MCA","per":89.90 ,"city":"pune"}  
#print(dictvar.keys())
for x in dictvar.keys():
    print(x,":",dictvar[x],"",dictvar.get(x))'''
    
                                     #ouputs  :name : amit  amit
                                              # program : MCA  MCA
                                              # per : 89.9  89.9
                                              #city : pune  pune
                                        
'''dictvar={"name":"amit","program":"MCA","per":89.90 ,"city":"pune"}  
print(dictvar.values())
dictvar2=dictvar.values()
for val in dictvar.values():
    print(val)'''
                                #output  : dict_values(['amit', 'MCA', 89.9, 'pune'])
                                           # amit
                                           # MCA
                                           # 89.9
                                           # pune

'''dictvar={"name":"amit","program":"MCA","per":89.90 ,"city":"pune"}  
print(dictvar.items())
for key,val in dictvar.items():
    print(key,":",val)
                

print(dictvar)
dictvar.update({"city":"pune"})
dictvar.update({"program ":"MBA"})
dictvar["city"]="delhi"
print("after update() :",dictvar)'''


                        #output : name : amit
                                    # program : MCA
                                    # per : 89.9
                                    # city : pune
                                    # {'name': 'amit', 'program': 'MCA', 'per': 89.9, 'city': 'pune'}
                                    #after update() : {'name': 'amit', 'program': 'MCA', 'per': 89.9, 'city': 'delhi', 'program ': 'MBA'}

                                    

'''s="mitwpupune"
b=""
for i in range(len(s)):
    if(i%2==0):
        b=b+s[i]
print(b)'''

# print alternate character in given string

#file handling


#Q1. file mode in python 
# Q2.open & read the file count and print total number of vowels 
# Q3 read file 1 and write the alternat line to file 2


# Open the file in read mode
'''with open('filename.txt', 'r') as file:
    # Read the entire file
    data = file.read()
    # Split the data into words
    words = data.split()
    # Count the number of words
    word_count = len(words)
    # Print the total number of words
    print("Total number of words:",(word_count))'''
    

'with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    lines = f1.readlines()
    for i in range(0, len(lines), 2):
        f2.write(lines[])
        
        
        
        
        
        
        
        