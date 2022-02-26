#sets in Python

List={1,2,3,3,4,5}
print(type(List))

my_set=set(List)#set function will remove the duplicates 
print(my_set)
print(type(my_set))#this method will return the type 

myList={12,34,"Mati"}
print(myList)

#This method will add an entry in the set
myList.add('Ali')
print(myList)

myList.update(List);

print(myList)

myList.discard('Ali')#This function will remove the element in the set

print(myList)

myList.remove('Mati');

print(myList)

#union of sets

set1={1,2,3}
set1=set(set1)
set2={2,3,4,5,6}
set2=set(set2)
set3=set1.union(set2)
set3=set(set3)
print("Union of set1 and set2 is: "+str(set3))

#Intersection of sets

set1={1,2,3}
set1=set(set1)
set2={2,3,4,5,6}
set2=set(set2)
set3=set1.intersection(set2)
set3=set(set3)
print("Intersection of set1 and set2 is: "+str(set3))
