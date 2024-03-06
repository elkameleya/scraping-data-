import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed 
from PIL import Image
import requests
from io import BytesIO


def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Update the class name for the outer wrapper
    product_wrappers = soup.find_all('div', class_='product-image-wrapper')

    results = []

    for product_wrapper in product_wrappers:
        # Update the class name for the individual product container
        article = product_wrapper.find('div', class_='product-image-wrapper')

        # Check if 'article' is found
        if article:
            image = article.find('img')

            # Check if 'img' tag is present
            if image:
                url = image.attrs.get('src', '')
                alt = image.attrs.get('alt', '')
                title = image.attrs.get('title', '')
                width = image.attrs.get('width', '')
                height = image.attrs.get('height', '')

                results.append([title, url, alt, width, height])

    return results



urls = ["https://www.my-furniture.com/fr/salon/", "https://www.my-furniture.com/fr/salle-a-manger/","https://www.my-furniture.com/fr/chambre-a-coucher/","https://www.my-furniture.com/fr/salon/canapes/","https://www.my-furniture.com/fr/chaises/","https://www.my-furniture.com/fr/chaises/","https://www.my-furniture.com/fr/chambre-a-coucher/lits/","https://www.my-furniture.com/fr/salle-de-bain/"]

myfurniture = []

with ThreadPoolExecutor(max_workers=8) as executor:
    # Download content from both URLs concurrently
    futures = {executor.submit(requests.get, url): url for url in urls}

    for future in as_completed(futures):  # Use as_completed directly
        url = futures[future]
        try:
            response = future.result()
            html_content = response.content
            results = extract_data(html_content)
            myfurniture.extend(results)
        except Exception as e:
            print(f"Error processing {url}: {e}")


# Create DataFrame and save to CSV
df = pd.DataFrame(myfurniture, columns=['Title', 'url','alt',  'width', 'height'])
df.to_csv('myfurniture.csv', index=False)
