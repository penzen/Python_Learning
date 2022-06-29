"""
a = True
b = 11 

# Indentation in python is super importment 


 # another way to comment or just use ctrl + /
if a == False :
    print("It's working")
elif a == True: 
    print("Elfi working")
else:
    print("This is else ")

# for loop iteration

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
add = 0

for num in my_list:
    if num % 2 == 0:
         print("Even number") # num becomes part of the for loop. 
    else:
        print ("Odd ")

    add = add + num 
    print(add)

for letter in "Hello world":
    print(letter)

 # tupple unpacking the

tup = [(1,2),(3,4),(5,6),(7,8)]
dup_list =  []

for a,b in tup: # tuple unpacking bascially duplicates the tuple inside the list, kind of like a nested for loop
    c = 0 
    c = a + 1
    print(a)
    dup_list.insert(c,a) # add stuff to the list. 
   # print(b)

print("Duplicate List here: ",dup_list)

# dictionaries  are the same as tuble unpacking, use a and b to get key and value 
# Also dictinaries are unorder so make sure you don't confuse it. 

# while loop 
# while some boolean condition is true 

p = 0 
l = 5
while p < l:
    p += 1
    print("P is greater ")

for o in "Penzen":
    if o == 'e':
        continue # basically starts the loop over 
    print(o)
"""

for num in range(1,10,2): #(start,stop,step-size)
    print(num)

# enumarate takes in any ittratable object. 
for item in enumerate("Hello"): # enumarate funtion bascially gives the index numbers. 
    print(item)

onelist = [1,2,3,4]
twolist = ['a','b','c','d'] 

# has to be used in a for loop 
zip(onelist,twolist) # zip basically puts the list together. 

threelist = list(zip(onelist,twolist)) # way to combine two lists.
onelist += twolist # another way to combine lists.
# the zip wat makes it into a 2d array 
print("One list: ",onelist)
print("Three list: ",threelist)
# remember to type cast the list if you want to use it 
print(threelist[0][1]) # 2d array using a zip

# itterateds through the list and can report back the list. 
z = 'a' in twolist
# min(onelist)  minimum 
# max(onelist)  maximum 
print(z)

#ui = input("Enter you faviorte number")
# input also exeps theing as strings so it needs to be tupe casted 
#int(ui)

# list comprehention, this method reduces the space required to make an object into list 

uni = "Aut"
#flattend out the for loop
#gunit = [x for x in uni] # list comperhenstion
#gunit = [x**10 for x in range(1,10)]
gunit = [x**10 for x in range(1,10) if x % 2 == 0] # can add for loop 
print(gunit)

# when the for loop is flattened it assumes your gonna add stuff in the list 
# so it's bascially doing append
celcusi = [10,20,30,40]
ferenhite = [((9/5) * temp + 32) for temp in celcusi]

conversion = list(zip(celcusi,ferenhite))

print(conversion)

"""
for x in range(1,100):
    if x % 3 == 0 and x % 5 == 0:
        print("fizBuzz")
    elif x % 5 == 0:
        print ("Buzz")
    elif x % 3 == 0: 
        print("Fizz")
    else:
        print(x)
"""

st = "Create a  list of first words using this string"

testlist =[ x[0] for x in st.split()] # this prints the first letter.
print(testlist)

 # help(celcusi.append) gives the doucment of the object/ method or funtion you might use
 

    