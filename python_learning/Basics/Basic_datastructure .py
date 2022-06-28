x = 2 + 4
print (x + 4)

# power in python is denoted by ** for example 

z = 3 ** 4
print("Value of z is ",z)
print (type(z))

# Indexing and slicing in Python, can be done with strings and there  are also reverse strings in Python

z = "This is a string "

print("Hello \n world ") # \t is used for space 
print("The funtion len will give you the length of the string/variable",len(z))
print("Normal Indexing",z[2]) # indexing in strings
print("Reverse indexing if the value is -1 then it will give you last name letter of the string",z[-3]) # reverse indexing 

print("Slicng: ",z[0:4:2]) # slicing
print("Slicing with the start: ", z[1:]) #everything inluded except the first letter of the string
print("Slicing with the end: ",z[:3])
print ("Reverse the string:",z[::-1] ) 

print(z + "hope") # concantination 
print 

print(z.upper())

print(z.split) # turns it into a list 
print(z)

print("Hello monkey {}".format('Donkey')) # .format lets you add sting, {} you can also add the index here. 

name = 'penzen'
last = 'lama'
print(f" Hello my name is {name} also {last}") # alternate to .format method

example_list =["sds",213,0.33] # list can hold pretty much any data type 

# can be sliced and indexed and concatinated 
print(example_list[2])
example_list.append("new position") # allows you to add any item at the end of the list 
example_list.pop() # pop removes the end of the list 
example_list.pop(2) # removes the index of the string 
#example_list.sort() # sorts the list.
example_list.reverse() #lets you revers the string 

# dictanarioes need key and values, in this exaple Penzen is the key and Lama is the value 
my_dict = {'Penzen':'Lama'}

# To access the value, you need to enter the key which is Penzen
#Dictionaryies cannot be sorted because they are not ordered. 

print(my_dict['Penzen'])

# dictionaries can also hold lists and pretty much any data types. 

prices = {'Apple':'9.00','orange':'99','Price_list':[32,45,64,34,54],'k3':{'inside_key':'Hidden key'}}

print(prices['Price_list'])
print(prices['k3']['inside_key']) # dictionary within Dictionaries. 
prices['k4'] = 'Asign new keys this way '
# to extract the list from the distionary 
z = prices['Price_list'][2] # get the specific value from the list
li = prices['Price_list']
print(type(z))
print(li)
prices.values() # gets value 
prices.keys() # gets key

# tuples are immutable 

t = (1,2,3) # these braces are tuples 
t.count(1) # checks how many times it's been repeted
#t.index('a') #checks index
print(type(t))

# sets are unorded collection of elemetns 

# sets have uniqe values 

lis =(1,2,2,2,3,3,3,3)
my_set = set()
my_set.add(lis) # will only show 1,2 and 3 no repetition.
my_set.add(1)

# %% writefile myfile.txt 
# The above command works in Juypeter note book, this creates a txt file 

myfile = open('testing.txt')

print(myfile.read())
myfile.seek(0) # this is reset the  cureser and will  let you start reading from the start
myopening = open("c:\\Users\\penze\\OneDrive\\Desktop\\testing.txt") # open from diffrent dicrectory 
print(myfile.read())

# r = only read 
# W = overwrite files 
# a = will add  on to the file 

#with open ('testing.txt',mode = a) as F:
  # F.write("Will let you write stuff in the file")

myfile.close()

print(2 == 2  and 1 == 2 )
print (1 == 1 or 1 != 2)

