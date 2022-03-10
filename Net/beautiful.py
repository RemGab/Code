import requests
from bs4 import BeautifulSoup
 
req = requests.get('https://fr.bazarchic.com/recherche?search=costume%20homme')
soup = BeautifulSoup(req.text, "lxml")
print(soup.title)