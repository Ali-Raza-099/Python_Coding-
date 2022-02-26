#Lists in Python

list=['Matiz','Roberts','Stephanie',1,22,34,455,34.45]
#list is just like arrays in python language
print(list)

#we can access any element in a list by accessing its index.
#Here id the code
print(list[3])#it is important to remember that index starts from 0.

#Updating a particular index in Lists

list[3]="Boats"
print(list)

#adding values in List
list.append("Brown")
print(list)

#Deleting values in lists using index
del list[2]

print(list)

#Removing particular value using value
list.remove("Brown")
print(list)