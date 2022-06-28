import re # importing regular expressions

text = "The agends phone number is 333-4333-433"

print("phone" in text) # this is very limted as it only looks at specic word and not the pattern 

# now we can do this using regurlar expression. 

'''
pattern = 'phone'
sa = "Not "
match = re.search(pattern, text)
match.span()
match.start()
match.end()
match= re.search('phone',text) # the search only shows the first output,meaning it will only show where it finds it first
print(match)
match= re.findall('phone', text) # basically finds all the matches of the charecter and turns it into a list
print(len(match))

for mat in re.finditer('phone', text):
    print(mat.group())
'''

#f = open("Testing.txt","w+")

# the /d is for the numerical charecters 
# this is search only for the pattern not exactly the number 
# quantifiers make sure you don't have to write the whole thing
text =" The agends phone number is 333-4333-433"
#phone = re.search(r"\d\d\d-\d\d\d\d-\d\d\d",text) # the r signifies for the regular expression 
phone = re.search(r"\d{3}-\d{4}-\d{3}",text) # regular expression with quantifiers
#print(phone.group()) # the .group gives you the exact phone number 
phone_pattern = re.compile(r'(\d{3})-(\d{4})-(\d{3})') # specic grouping of the numbers 
result = re.search(phone_pattern,text)
#print(result.group())
#print("Using colpiler pattern: ",result.group(1)) # the indexes start at 1 for group


print (re.search(r'cat|dog','The dog is here '))  # the pip operator | bascially means or 

print(re.findall(r'.at', 'The cat in the hat in bat has to be fat ')) # "." is the wild card and will return anything attached to at 

print(re.findall(r'^\d',"1 is the game")) # the string I'm seacrhing through is a number 
# starts with ^\d
# ends with \d$

# exclution 
pharse = " There are 3 numbers in 56 this phrase 32"
pattern = r'[^\d]+' #excludes numbers 
print(re.findall(pattern,pharse))
test = " This is a test phrase. How are we gonna remove all the puntuations !!!! "
print(re.findall(r'[^.! ]+',test)) # adding stuff after the ^ will remove all the unwanted symboles 
''.join(test)
print(test)

