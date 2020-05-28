import requests
import bs4

# now declare object which stores code of website we want to scrap 
# for this we need to request website some websites don't allow scraping on them 
# because of privacy issue so we here selecting any website from on 
# which it is allowed to scrap
# and web info is stored in object named res

res= requests.get ('https://learncodeonline.in')

# write websites name whose title we want to scrap

soup =bs4.BeautifulSoup(res.text , 'lxml')

# we should take care of case sensititvity
# lxml is structure supported by BeautifulSoup like html parser to handle basic html websites
# now object soup is of class BeautifulSoup now we can extract information
# we want from object soup


# Here  we will find title 
#let's store tiltle in object webtitle

webtitle =soup.select('title')

# now in object webtitle all there will be array of all elemnts with tag title in code

  print (webtitle)
#above form will print array something like [<title> Learn  Code </title>]

print ( webtitle[0] )
#above form will print first element array something like <title> Learn  Code </title>

print ( webtitle[0].text )
#above form will print first element array without title  tag something like  'Learn  Code'

# Here was demonstration how to scrap basic info from website