import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed 

def scrape_url(url):
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find(class_='product-list')
    articles = ol.find_all('article', class_='product-container product-style')
    results = []
    for article in articles:
        image = article.find('img')
        url = image.attrs['src']
        alt = image.attrs['alt']
        title = image.attrs['title']
        width = image.attrs['width']
        height = image.attrs['height']
        results.append([title,url, alt, width, height])
    return results

urls = ["https://baity.tn/130-canape-lit", "https://baity.tn/88-bureau","https://baity.tn/242-salon-jardin","https://baity.tn/112-chambre-complete","https://baity.tn/187-luminaire","https://baity.tn/54-etagere-et-rangement","https://baity.tn/143-lit-enfant"]

baity = []

with ThreadPoolExecutor(max_workers=7) as executor:
    # Download content from both URLs concurrently
    futures = {executor.submit(scrape_url, url): url for url in urls}

    for future in as_completed(futures):  # Use as_completed directly
        url = futures[future]
        try:
            results = future.result()
            baity.extend(results)
        except Exception as e:
            print(f"Error processing {url}: {e}")

# Create DataFrame and save to CSV
df = pd.DataFrame(baity, columns=['Title', 'url','alt',  'width', 'height'])
df.to_csv('baity.csv', index=False)
