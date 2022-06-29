
import openpyxl # after installing with pip it can be used.
import docx # only works after installing with pip 

class car(): # self bascially means this. in python
    #class object attribute 
    typ = 'NonLiving thing'
    # can also be refrenced as car.typ 
    # makes it more clear in the long run 

    
    def __init__(self,merc,model,make): # init is the constructor of the class 
        self.merc = merc
        self.model = model
        self.make = make
    #this part is the attribute of the car

    #object actions ---> methods 
    def con(self,contry):
         print("The car is a {}  and it's model name is {} and it was build in {} and it was built in{}".format(self.merc,self.model,self.make,contry))
    def fs():
        print("Override this method")




"""
Range_1 = car('Voks','Polo',2015) # two ways to pass into a class
Range_2 = car(merc = 'Honda',model = 'Brio',make = 2013) 
print (Range_1.typ)
Range_2.con("Germany")
"""


# Inheratace resuing classes that have already been defined. 

class trl(car): # passing the name should be enough for inheratacne 
    #def __init__(self):
     #   car.__init__(self, merc, model, make)
    
    car.typ = "New Shit here "
    def fs():
          print("Method overritren")

    def __init__(self,merc,model,make,kilo):
       # super().__init__ (merc,model,make) # the inherted class does it for us
        car.__init__(self,merc,model,make) # two ways to do it
        #the above method is usefull when using multiple inheritace classes
        self.kilo = kilo
    # theise are called dunder/magic methods in a class
    def __str__(self): # this is bascally a tostring method for python 
        return f"{self.merc} and the name of the model is: {self.model}"
    def __del__(self): # this will give a descriptiuon when the class is deleted 
        print("Your class has been deleted")

"""
dental = trl("mercasie","g-Wagon",2022,10000)
dental.con("Germany")
print(dental.typ)
print(dental)
#dental.con("New Zealand ")
del dental # deleted dental from the memory 
"""

class Line:
    pi = 3.17

    def __init__(self,corone):
        self.corone = corone

    def distance(self): 
        x1,x2 = self.corone # unpack the tuples
        return  x1 * x2 



distance = Line((3,4))
#print(distance.distance())       


class bank():

    def __init__(self,owner,balance):
        self.owner = owner 
        self.balance = balance

    print(f"OWNNNEzrrr: {self.owner}")
    def deposit(self,add):
        self.balance += add
        return f"The current Blance for {self.owner} is {self.balance}"

    def withdraw(self,widrw):
        if self.balance < widrw:
            print(f"Not enough money to withdraw:{self.balance}, withdraw amount: {widrw}")
        else:
            self.balance -= widrw
            return f"The current Blance for {self.owner} is {self.balance}" 


acc1 = bank("John",1200)
print(acc1.deposit(1000))

print(acc1.withdraw(100))


class wick():
    def __init__(self,name = None): 
        self.name = name
        print(f"Your name is {self.name}")


wick("JIOOOOO")
