
# sort method

'''list=[1,2,3,4,5,6,5,3,5,3,2,8,5,5,9,5]
#list.append(7)
#print(list)
list.sort(reverse=True)
print(list)'''

colours=["voilet","indigo","blue","red","green","yellow"]
colours.sort(reverse=True)
print(colours)

#we can send parameter in sort method
#reverse method

num=[4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
#num.reverse()
#print(num)


#index method

num=[4,2,5,3,6,1,2,1,2,8,9,7]
print(num.index(1))

 #index is the display accurate index position
 
 #count method
 
num=[4,2,5,3,6,1,2,1,2,8,9,7]
print(num.count(1))


#copy method

colours=["voillet","green","blue","yellow","red"]
newlist=colours.copy()
print(colours)
print(newlist)



#append method


num=[1,2,3,4,5,6]
num.append(7)
print(num) 


#insert method

colours=["voilet","indigo","blue"]
colours.insert(3,"green")
print(colours) 

#extend method

colours=["voilet","indigo","blue"]
rainbow=["yellow","orange","green","red"]
colours.extend(rainbow)
print(colours)

#concatinating method

colours1=["voilet","indigo","blue"]
colours2=["yellow","orange","green","red"]
print(colours1+colours2)



 
 