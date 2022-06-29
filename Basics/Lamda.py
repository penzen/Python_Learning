def square(number):
    return number ** 2 

lop = [1,2,3,4,5,6,7,8,9,10,11,12]
#map(square,lop)  the map funtion basicallu runs the code with the funtion. This

#qua = list(map(square,lop))
#print (qua) # can also be typed caseted into a list. 

def names(nam):
    if len(nam) % 2== 0:
        return 'Even'
    else:
        return 'Odd' 


peps = ["Penzen","Lama","Advit","joker","Batman"]
op = list(map(names,peps)) # in maps don't input the () in methods because map does it for you 
#print(op)

def truth(num):
    return num % 2 == 0 


ds = [1,2,3,4,5,6]
#filter(truth, ds)  filter funtion only returns the true variables 
example = list(filter(truth, ds))
#print(example)

''' This converted to a landa expersssion will look something like below
def square(number):
    return number ** 2 
'''
#ans = lambda num =  num + 2 

def vol(num):
    return 4/3 * 22/7 * num ** 3

#print(vol(2))

def unique_list(ssa):
    return set(ssa)

lopo = [1*3,2,3,3,4,5,6,7]

print(unique_list(lopo))

