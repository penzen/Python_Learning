import time 
import timeit
def fun_one(number):
    return[str(num) for num  in range(number)]

def fun_two(number):
    return  list(map(str,range(number)))

# current time before 
start = time.time()
# run code 
result = fun_two(1000000)
# current time after
end = time.time()

eplasped = end - start

print(eplasped)

st1 = '''
fun_two(1000000)
'''
setup = '''
def fun_two(number):
    return  list(map(str,range(number)))
'''
print(timeit.timeit(st1,setup,number = 100))