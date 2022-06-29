from collections import Counter
from collections import defaultdict
from collections import namedtuple

l = [1,2,3,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,4]

op = Counter(l)
print(Counter(l)) # counts how many numbers there are in the list.
# counter are dictionaries


print(op.most_common())

d = {'a':10} #  normal dictionaries
print(d['a'])

# if you ask for a key that isn't present in a normal dictionaly the defaultdict will provide a value 
d = defaultdict(lambda:0) 
print(d["Decorator"]) # gives the defalut value 

#named tuple  can be used like dictionaries with values that


mytuple = (10,20,30)
Dog = namedtuple('Dog',['Age','height','type']) # pass in the parameters 
Pogo = Dog(Age = 11, height = 2.2 , type = 'pug')
print(type(Pogo))
print(Pogo.Age)