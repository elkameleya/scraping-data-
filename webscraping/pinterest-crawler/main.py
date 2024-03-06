import csv
import os
from src import PinterestScraper, PinterestConfig

# Function to save image information to a CSV file
def save_to_csv(image_info_list, filename="image_info.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "url"])

        for image_info in image_info_list:
            writer.writerow([image_info["file_name"], image_info["image_url"]])

# Configuration for PinterestScraper
configs = PinterestConfig(search_keywords=" bed",
                          file_lengths=10,
                          image_quality="orig",
                          bookmarks="")

# Initialize PinterestScraper and download images
scraper = PinterestScraper(configs)
scraper.download_images()

# Get information about downloaded images
image_info_list = []
for idx, url in enumerate(scraper.get_urls()):
    file_name = f"image_{idx + 1}.jpg"  # You can customize the file naming logic
    image_info_list.append({"file_name": file_name, "image_url": url})

# Save image information to a CSV file
filename = "image_info.csv"  # Define the filename here
save_to_csv(image_info_list, filename)

# Print confirmation message
print(f"Image information saved to {filename}")
