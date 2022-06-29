from PIL import Image
from array import *

# more studing required if needed. 


mac = Image.open('example.jpg')
print(mac.size)
num_list =[1,2,3,4,5,6,7,8,9]

num_list.remove(2)
print(num_list)

print(list(range(10,1,-1)))
#mac.show()

# cropiing the image 
print(mac.size)

mac.crop((0,0,100,100))
# array in Python 

arr = array('i',[10,203])

print(arr[1])