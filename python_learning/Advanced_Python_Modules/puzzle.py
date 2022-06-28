import shutil
#shutil.unpack_archive('unzip_me_for_instructions.zip','open_seseme','zip')
f = open('C:\\Users\\penze\\OneDrive\\Desktop\\python_learning\\Advanced_Python_Modules\\extracted_content\\Instructions.txt','r')
#print(f.read())

list_of_lists = []
# this can be used to find the speific word in a text 
# you could also use yield a generator to save memory 
# that way doing . next will not consume as much memory as reqiored
for line in f:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

f.close()
# this funtion can also be used to find multiple words in python
# there is already a funtion that does this it's just for good practise
# there is also a module that finds out how many words are repeted in a certain text .
def find_word(word): # using a list and a for loop to find the speific word in list 
    for ds in range(len(list_of_lists)):
        for twod in range(len(list_of_lists[ds])):
         if list_of_lists[ds][twod] == word:
            print(f"The word {word} has been found.\n")
         else:
            pass 



find_word("Python")

#print(list_of_lists)
# first unzip the file contents
