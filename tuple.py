tuple1=(1,2,3,4,5,6,7)
tuple2=("red","green","blue")
print(tuple1)
print(tuple2)

#check for items in tuple

country=("spain","italy","india","england","germany")
if "germany"in country:
    print("germany is present")
else:
    print("germany is absent")
    
    
  #range for index in tuple

  #tuple manipulating (tuples)
  
countries=("spain","italy","india","england")
temp=list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)


countries=("pakistan ","afganistan","bangladesh","shrilanka")
countries2=("vietnam","india","china")
southeastasia=countries+countries2
print(southeastasia)
    