# we are going to use BeautifulSoup for extraction of data from Flipkart
# data extracted will be  price of item product name and it's rating

# first we see data we want to extract by inspecting Flipkart's official page
# after we see under which tag data is stored 
# and afte understanding it we can use it to extract dta from website

# First, let us import all the necessary libraries:
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd


# To configure webdriver to use Chrome browser, we have to set the path to chromedriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# below code is to open the url

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")


# Now that we have written the code to open the URL, it’s time to extract the data from the website. 
# As mentioned earlier, the data we want to extract is nested in <div> tags. So, I will find the div tags with those 
# respective class-names, extract the data and store the data in a variable.

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 


# now just run code to extract data and  we can store data  in file if we want 
# so let's write code to write info in csv file 
# it will make 3 columns price product name and it's rating and data will be written there


df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

#now data will wrote in product.csv file





