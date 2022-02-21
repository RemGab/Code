import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.sncf-connect.com/app/home/shop/results/outward').read()

soup = bs.BeautifulSoup(source,'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)