#Some userdefined Functions in python

def calculateArea(radius):#function to calculate area
    pie=3.1415
    area=radius*radius*pie
    print("Area:"+str(area))
    return
    r=input("Enter the radius:")
    r=int(r)
    calculateArea(r)
    

    def calculateSq(num):#function to calculate square
     square=num*num
     print("Square is:"+str(square))
     return
    
     n=input("Enter the number:")
     n=float(n)
     calculateSq(n)
     
     
#Some lambda functions
def calculateSquare(x):
    return x*x;

print(calculateSquare(9))

#Map function
sentence = 'I am hungry' 
words = sentence.split()
print (words)
lengths = map(lambda word: len(word), words) 
list(lengths)

#Some filter function

data=[1,2,3,4,5,6,7,7,8,9,10,11,22,334,465,334,566,2345]
result=filter(lambda x:x%2==0,data)
print(list(result))


