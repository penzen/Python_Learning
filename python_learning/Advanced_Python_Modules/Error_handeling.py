def add(one,two):
    return one + two

#number_one = 21 
#number_two = input("Please enter a number")
'''
try:
    ds = add(number_one,int(number_two))
    print(ds)
except:
    print("The input is not an int")
finally:
    print("Done")
'''


'''
try:
    top = open('testfile','r') # only read file 
    top.write("Hello world") # written here so we get an os error message
except TypeError:    # only goes in the code if there is an type error 
    print("There was a type error")
except OSError: # specidicaly os errors
    print("OS error")
finally:
    print("Done")
''' 
# to indendednt a block of code prese tab  

while True:
    try:
       duel = int(input("Please enter a number"))
    except:    
        print("Not a number")
        continue
    else:
        print("You did print a number")
        break
    finally:
        print("Done")
