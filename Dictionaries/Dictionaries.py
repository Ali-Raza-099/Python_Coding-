#Dictionaries in Python

#creating dictionaries in python
Info={
      "Name":"Matiz",
      "email":"iammatiz00@gmail.com",
      "age":21,
      "Batch":"SP20",
      "Class":"BSE-B",
      "Id":"42"
     
    }

#printing value in dictionary
print(Info["age"])
print(Info["Batch"])

#Updating values
Info["age"]=22
print(Info)

#Adding value in Dictionary

Info["Reg"]="SP20-BSE-042"
print(Info)

#Deleting Dictionary elements
del Info["Reg"];
print(Info)

#Deleting Dictionaries
#del Info will delete the dictionary

#Clearing Dictionaries
Info.clear()

print(Info)

