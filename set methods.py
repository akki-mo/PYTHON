s1={1,2,3,4,5,6}
s2={2,4,6,8,7,10,17}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

# unioun() and update() method
# seperate the common element in both the set


cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
#cities3=cities1.union(cities2)
cities1.intersection_update(cities2)
print(cities1)



# symmatric_difference and symmtric_difference_update
# do not print same element
# 


cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
#cities3=cities1.symmetric_difference(cities2)
cities3=cities1.symmetric_difference_update(cities2)

print(cities3)



# isdisjoint
# do not satisfy same elements both sets elment are differrent 
cities1={"tokyo2","madrid2","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
print(cities1.isdisjoint(cities2))


#issuperset
#subset are present in the superset

cities1={"tokyo","madrid","berlin","delhi"}
#cities2={"seoul","kabul"}
cities2={"tokyo","delhi","berlin","madrid"}
print(cities1.issuperset(cities2))
#cities3={"seoul","kabul","madrid"}
cities3={"tokyo","delhi","madrid"}
print(cities1.issuperset(cities3))

# issubset 
# subset are present in the main set is compulsry 

cities1={"tokyo","madrid","berlin","delhi"}

cities2={"tokyo","delhi","berlin","madrid"}
print(cities1.issubset(cities2))

cities3={"tokyo","delhi","madrid"}
print(cities3.issubset(cities1))

#add()
# add new element in the set


cities1={"tokyo","madrid","berlin","delhi"}
cities1.add("india")
print(cities1)


#update 
# update he list and  add both list
cities1={"tokyo","madrid","berlin","delhi"}
cities2={"india ","america","iran"}
cities1.update(cities2)
print(cities1)

#remove() and discard()
#we can use remove() and discard() methods to remove item from list
cities1={"tokyo","madrid","berlin","delhi"}
cities1.remove("berlin")
#cities1.discard("berlin2")

print(cities1)



#pop()
#remove last element in the list
cities1={"tokyo","madrid","berlin","delhi"}
item=cities1.pop()
print(cities1)
print(item)


#del method in set 
# del is not a method , it is a keyword which is deletes the set entirely
'''cities1={"tokyo","madrid","berlin","delhi"}
del cities1
print(cities1)'''


#clear 
# this method clear all items in the set and prints an empty set
cities1={"tokyo","madrid","berlin","delhi"}
cities1.clear()
print(cities1)


#check if item exists
# you can check if an item exists in the set or not

info={"carla",19,False,5.9}
if "carla" in info:
    print("carla is present")
else:
    print("carla is not prasent" )   