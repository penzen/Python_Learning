import random
def say_hello(name):
    print("Hey {}".format(name))

#say_hello('monkey')

# python is dynimical type meaning you don't have to speciffy the data tyepe 
def calulate_random(num):
    number = random.randint(1, 1000)
    print(number)
    print(number + num)

#calulate_random(10)

def is_even(num):
    return num % 2 == 0

#print(is_even(10))

def check_list(lol):
     for x in lol:
         if x  % 2 == 0:
             print("This is an even number {}".format(x))
         else:
            print("This is an odd number {}".format(x))



#example = list(range(1,101))
#check_list(example)
# Return breaks the startment inside the funtion. 

tup_example = [('Abby', 130), ('Billy', 2000),('John',100),("Wayne", 9000)]

# now we have to compare the objectives of the tupples
def emp_month(tup):
    itter = 0 
    emply = None
    hours = 0

    for x,y in tup:
        if itter == 0: # unnessary step 
             hours = y
             emply = x
        elif itter != 0: 
            #another nested if statement. 
            if(hours > y):
                continue
            else:
                hours = y
                emply = x
        itter += 1
    
    return emply, hours


employee, hours = emp_month(tup_example)
#print("The employee is {} and the hours are {}".format(employee, hours))

game = ['','O','']

def shu(gam):
    shuffle(gam)  # shuffle doens't return anything so it has to been in differnt lines. 
    return gam


def guess(gam):
    ans = input("Guess the cup 0 1 or 2")
    int(ans) # have to type case because the input does not return a string
    if(gam[ans] == 'O'):
        print("You got it!!!")
    else:
        print ("It was the wrong one")




#yellow = input("ENter ")

# args and kwargs 


   

def arguments(*args): # args allows as many vaiables as possible 
    return sum(args) * 0.05 # args come in a list of tuples

#tup = (1,2,3,4,5,6,7,8,(9,22))
#print(tup[8][1])

def trail(*args):  # as long as their is a star it will be args so any variable name will work
    for a in args:
        print(a)
    print(args[1])


def kwgs(**kwargs): # kwargs are in dictionary form
    for name in kwargs:
        if name == 'Penzen':
            print("Your name is {}".format(kwargs['Penzen'])) # put in the key
        else:
            print("Your name is  {}".format(name))
    

#kwgs(Penzen = 'Apple', Lama = 'Mango')

def combie(*args, **kwargs): # these can be combined together  
    print(args)
    print(kwargs)

#trail(1,2,3,4,5,6)

def even(*args):
    lit = []
    for a in args:
        if a % 2 == 0:
            lit.append(a)
    
    print(lit)

def led(s):
    letter = ""
    counter = 0

    for a in s: # add a counter. 
        if  counter % 2 == 0:
             letter += a.upper()
        else:
             letter += a.lower()
        counter += 1 
    
   
    return letter
    #return values
    
#print(led("Helloworld"))


