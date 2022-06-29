# goals get the tile of book with 2 star rating 
import requests
import bs4

# for the page number use a string so that it's more flexiable 

'''
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
base_url.format('12')
print(base_url)
'''



'''
req =requests.get(f'http://books.toscrape.com/catalogue/page-1.html')
soup = bs4.BeautifulSoup(req.text,'lxml')
products = soup.select('.product_pod')
# the product[0] lets us check the speicic elements 
example = products[0]
example.select(".star-rating.Three") # use . for the space if there is any in the class name 

print(example.select('a')[1]["title"]) # go in the set and then experiment a bit to see where the title lies, so second list and then title 


'''
two_star_title = []

for n in range(1,51):
    req =requests.get(f'http://books.toscrape.com/catalogue/page-{n}.html')
    soup = bs4.BeautifulSoup(req.text,'lxml')
    products = soup.select('.product_pod') 
 
 # basically this example = products[0] to check for the specific product 
    for book in products:
        if len(book.select('.star-rating.Three')) != 0:
            two_star_title.append(book.select('a')[1]['title'])
            
           

print(two_star_title)



#print("star-rating Three" in str(products)) # quick way to do it 



