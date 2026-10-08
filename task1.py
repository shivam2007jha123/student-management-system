# This is for write data in a file
text=open("file.txt","w")
text.write("python is an programming language")  #Expalaination:- write should always be in string
text.close()

#This is for read and display data
text=open("file.txt","r")
data=text.read() #explaination:- read() is used to read the content of the file
print(data)
text.close()

#This is for appending a new data
text=open("file.txt","a") #explaination:- append mode is used to add new data to the existing file without overwriting the existing content
text.write("\nHELLO WORLD")
text.close()

#This is updated file content after appending
text=open("file.txt","r")
data=text.read()
print(data)
text.close()