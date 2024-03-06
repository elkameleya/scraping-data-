# pip3 install requests
import requests

#pip3 install beautifulsoup4
from bs4 import BeautifulSoup

#pip3 install pandas
import pandas as pd

Meubles= []

for i in range(0,5):
  url = f"https://www.lemeuble.tn/2-accueil?page=2-{i}"
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  ol = soup.find(class_='products row')
  articles = ol.find_all('article', class_='product-miniature js-product-miniature')
  for article in articles:
    image = article.find('img')
    title = image.attrs['alt']
    url =  image.attrs['data-full-size-image-url']
    
    Meubles.append([title,url])
    

df = pd.DataFrame(Meubles,columns=['Title', 'url'])
df.to_csv('Meubles.csv')
