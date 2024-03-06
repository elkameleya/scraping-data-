import pandas as pd

# Read CSV files into DataFrames
df1 = pd.read_csv('baity.csv')
df2 = pd.read_csv('ikea_scrape.csv')
df3 = pd.read_csv('image_info.csv')
df4 = pd.read_csv('Meubles.csv')
# Concatenate or merge DataFrames
combined_df = pd.concat([df1, df2,df3,df4], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_data.csv', index=False)
