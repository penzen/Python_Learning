import requests
import bs4 # gives us the way to get the stuff from web

# grabbing a title 
result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

# lxml is used in the back end by beautifil sopu to understand what is what in the website 
# css idea and tags etc
soup = bs4.BeautifulSoup(result.text,'lxml') #converts the raw code into readable code 


print(soup.select('title')) # selects the HTML tag from the webpage 
print(soup.select('h1'))

# grab the actually text from the website
print(soup.select('title')[0].getText())
print(type(soup.select('h1')[0].getText())) # the .getText method converts it into a string 
print(soup.select('h1')[0].getText())

# Grabbing a class
# classess require to period to select .

print("The text 2 shows: ",soup.select('.toctext')[2].getText()) 
'''
for item in soup.select('.toctext'):
    print(item.text)
'''
# grabbing an image 
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup2 = bs4.BeautifulSoup(res.text,'lxml')

computer = soup.select('.thumbimage')[0]
print(computer['src'])

download = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Roosevelt_OConnor.jpg/220px-Roosevelt_OConnor.jpg")

print(download.content)

f = open('Image_download.jpg','wb') # wb is write binary
# remember to make the type of file it is and always remember it's in binary 
f.write(download.content) # writes the image to the file 

f.close()