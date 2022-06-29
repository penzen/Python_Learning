#importing the os module
import os
import shutil # can be used to move files in diffrent locations 
#to get the current working directory
directory = os.getcwd() 
ldict = os.listdir() # this command will list everything in the current working directory
#print(directory)
#print(os.listdir('C:\\Users\\penze')) 
print(os.listdir()) 
f = open("Practise.txt",'w+')
f.write("THis is a practise file ")
f.close()
# move files around
shutil.move("Practise.txt","C:\\Users\\penze\\OneDrive\\Desktop\\python_learning\\Basics") # takes in the sourse and the destination

# there is a bunch of more os funtionality can be used to make a file extractor or a file maker 
