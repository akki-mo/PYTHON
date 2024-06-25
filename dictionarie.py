
#Accessing dictionary items



'''dict={
    
'name ':"akshay",
"age":19,
"eligible":True,}

print(dict['name '])
print(dict.get('eligible'))'''



#Accessing multipal values on dictionaries


'''dict={'name':'akshay','age':19,'eligible':True}
print(dict.values())
print(dict.keys())

for key in dict.keys():
    print(dict[key])'''
    
    
# dict={'name':'','age':19,'eligible':True}
# print(dict.items())



#dictionary methods in python

# 1) update()


'''ep={122:45,123:89,567:69,670:67}
ep2={222:68,566:90}
ep.update(ep2)
print(ep)'''


# 2)  clear()

'''ep={122:45,123:89,567:69,670:67}
ep.clear()
print(ep)'''

#3)  pop()

'''dict={'name':'akshay','age':19,'eligible':True}
dict.pop('eligible')
print(dict)'''



# 4) popitem()

'''dict={'name':'akshay','age':19,'eligible':True}
dict.popitem()
print(dict)'''


#5)  del()

'''dict={'name':'akshay','age':19,'eligible':True}
del dict['age']
print(dict)'''










