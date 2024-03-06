from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




# Ensure you have chromedriver installed and in your PATH or specify its location directly
driver = webdriver.Chrome()

# Define your product categories here
productlist = [
    "sofas-and-armchairs/sofa-beds",
    "beds/single-beds",
    # Add other categories as needed
]

def scrape_ikea_products(productlist):
    all_products = []  # List to hold all product dictionaries

    for product_category in productlist:
        URL = f"https://www.ikea.com.hk/en/products/{product_category}"
        driver.get(URL)
          # Wait for the page to fully load (example)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, '//img[(@alt="")]')))
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Iterate through products and extract details
        for item in soup.find_all(class_="card"):
            print("item+++", item)
            try:
                details = json.loads(item.find(class_='itemInfo').input['value'])
                item_name = details['name']
                item_price = details['price']
                item_cat = details['category']
                item_url = item.find(class_='productImg').img['data-src']
                prod_url = "https://www.ikea.com.hk" + item.find(class_='card-header').a['href']

                product_dict = {
                    "Title": item_name,
                    "url": item_url,
                    "item_price": item_price,
                    "item_cat": item_cat,
                    "prod_url": prod_url
                }
                all_products.append(product_dict)
            except Exception as e:
                print(f"Error processing product: {e}")

    return pd.DataFrame(all_products)

# Function call to scrape products and save to CSV
df = scrape_ikea_products(productlist)
df.to_csv('ikea_scrape.csv', index=False)

driver.quit()  # Close the browser window