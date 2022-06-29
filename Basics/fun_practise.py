
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0: #even
        if a > b:
            return a  # can use the min funtion, for clearner code.
        else:
            return b 
    elif  a % 3 == 0 and b % 3 == 0: # odd 
        if a > b:
            return a 
        else:
            return b 
    else:
        if a > b:
            return a 
        else:
            return b 


#print(lesser_of_two_evens(21,51))


""" Method one this one is long and have to work out the spacing thing. 
def animal_crackers(text): # have to remember the space between
    letone = text[0]
    counter = 0 
    letwo = ""

    for a in text: 
        if  a.isspace()  : # when there is a space check the parameter
            counter += 1 
            letwo = text[counter] 
            break
        else: 
            continue 
        counter += 1 
    print("Second one:",letwo)
    print("First one: ",letone)
    #return letone == letwo 
"""

def animal_crackers(text): # simple method. 
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
#animal_crackers("Pznzen Pama")
#print (animal_crackers("Penzen Pama"))

def old_macdonald(name):
    update = ""

    for a in name: 
        if(a == name[0]):
            update += a.capitalize()  
        elif (a == name[3]):
             update += a.capitalize()  
        else:
            update += a

    return update 
    
#print( old_macdonald("lenzen"))

""" Shorter way to do it. 
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
"""

def master_yoda(text): # reverses the text
    return ' '.join(text.split()[::-1])



def spy_game(nums): 
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]: # it pops off everytime it gets to a 7 or a one
            code.pop(0)
    return code[0] == 'x'
    
lo = [0,0,0,7]
print(spy_game(lo))

"""
The iter funtion can be used to itterate throgg the list 
lo = iter(lo) 
The Iter funtion uses the next method to go to the next element/ 
print(next(lo))
print(next(lo))
print(lo[::2])
"""

# A prime number can only be divisiable by one, 
def prime_number(number): 
    count = 0
    for a in range(2, number+1):
        if  length_factors(a) == 2:
            count += 1
    return count

def length_factors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(x)
    return len(factors)


print(prime_number(100))

    
    