#Open a file  and read it
fileOpen= open("Pak.txt","r+")
str=fileOpen.read()
print(str)
#opning file 
fileOpen.close()


#Open a file and apend it

fileOpen= open("Pak.txt","a+")
fileOpen.write("\nIts hot today")
fileOpen.close()

fileOpen= open("Pak.txt","r+")
str=fileOpen.read()
print(str)
fileOpen.close()

fileOpen=open("Pak.txt","r+")
place=fileOpen.tell()
print("Position:",place)

