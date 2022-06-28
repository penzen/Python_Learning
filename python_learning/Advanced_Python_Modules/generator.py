"""
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

""" 

def create_cubes(n): # you have to iterrate through it to get the numbers 
    for x in range(n):
        yield x ** 3 # bascially a return system  statement with an iteerator 
# yield is very memeory effiecnet as it does not save the whole thing 

'''
for x in create_cubes(20): 
    print(x)
'''

def gen_febo(n):
    a = 1 
    b = 1
    for x in range(n):
        yield a 
        a,b = b, a+b
'''
for x in gen_febo(20):
    print(x)
'''

def simple_gen():
    for x in range(3):
        yield x 
        
gen = simple_gen()

# ittrates through  the values 
print(next(gen))
print(next(gen))

s = "hello"
s_iter = iter(s)# itterates throug normal object  
# makes a normal object iteeratble 

#print(next(s)) # gives an error because it's not yet itteratble can be done using
# for loop but using itter gives it the change to use next in the object 
print(next(s_iter)) #objects that are irreatble into iteerators 
 