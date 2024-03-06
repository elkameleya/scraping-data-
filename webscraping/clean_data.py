import pandas as pd
from PIL import Image
import requests
from io import BytesIO
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load CSV file into a DataFrame
df = pd.read_csv('combined_data.csv')

# Strip column names of any leading/trailing whitespaces
df.columns = df.columns.str.strip()

# Remove duplicates based on 'Title' column
df = df.drop_duplicates(subset='Title')

df=df.drop(columns="Unnamed: 0")


# Save the filtered DataFrame to a new CSV file
df.to_csv('filtered_combined_data_.csv', index=False)
