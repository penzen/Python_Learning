import requests
import bs4

'''
res = requests.get('http://quotes.toscrape.com/')
'''
# could convert it into a string and then check if No qoutes found is in it 
# get the names of the author in the first page of

authors = set() # used set because it uses uniqe stucture 
#print(soup.select('.author')[0].text) 



count = 0
# to get the names of author
'''
for author in range(len(soup.select('.author'))):
    authors.add(soup.select('.author')[count].text)
    count += 1
print(authors)
'''
# Create a list of all the quotes on the first page
# the text are inside of the quite class 
# the main qoutes are inside of the qoutes 
'''
print(soup.select('.text')[0].text)

qoute = [] 
for q in range(len(soup.select('.text'))):
    qoute.append(soup.select('.text')[count].text)
    count += 1
print(qoute)
'''

# getting the tags 
'''
print(soup.select('.tag-item')[1].text)
tag = []
for t in range(len(soup.select('.tag-item'))):
    tag.append(soup.select('.tag-item')[count].text)
    count += 1
print(tag)
'''

# This task will require two for loops one for to navigate the pages and the other to navigate the authors 

state = True
count_page = 1

while state == True:
    print('Going in the loop')
    res = requests.get(f'http://quotes.toscrape.com/page/{count_page}/')
    soup = bs4.BeautifulSoup(res.text,'lxml')
    if soup.select('.text') != []:# Use this to loop through the pages
        count = 0 
        for a in range(len(soup.select('.author'))):
             print("The count is :",count)
             authors.add(soup.select('.author')[count].text)
             count += 1
    elif soup.select('.text') == []:
        state = False
        break 

    count_page += 1

     
print(authors)

     
# project Idea make a web scraper that let's you find the most repeted words in the document,
# could be done using a list with the names 
# Also this code could be used to make an efficent algorithm 
