#Analyze the data to extract insights.
import pandas as pd
import requests
from io import StringIO

#Load dataset from Azure Blob Storage using URL
url = 'https://dataengineerv1.blob.core.windows.net/raw/tourism_dataset.csv?sp=r&st=2024-09-21T20:13:39Z&se=2024-09-22T04:13:39Z&spr=https&sv=2022-11-02&sr=b&sig=R%2FHzvgNzk9%2BFvtVnR1AJxHj2jF3%2BJatfb5iaritQuck%3D'
response = requests.get(url, verify=False)

#Load the dataset
data = pd.read_csv(StringIO(response.text))
print(data)
print("Column names:", data.columns.tolist())

#Clean the column names
data.columns = data.columns.str.strip()
data = data.rename(columns={'country': 'Country', 'Category': 'Category'})

#Initialize variables
country_avg_rating = None
top_categories = None

#Check if the 'Country' column exists and calculate average ratings
'''SELECT Country, AVG(Rating) AS Avg_Rating
FROM tourism_data
GROUP BY Country;'''

if 'Country' in data.columns:
    country_avg_rating = data.groupby('Country')['Rating'].mean().reset_index()
    country_avg_rating.columns = ['Country', 'Avg_Rating']  # Rename for clarity
else:
    print("Column 'Country' not found in the DataFrame.")

#Check if the 'Category' column exists and find top 3 categories
'''SELECT Category, AVG(Rating) AS Avg_Rating
FROM tourism_data
GROUP BY Category
ORDER BY Avg_Rating DESC
LIMIT 3;
'''
if 'Category' in data.columns:
    category_avg_rating = data.groupby('Category')['Rating'].mean().reset_index()
    top_categories = category_avg_rating.nlargest(3, 'Rating')
else:
    print("Column 'Category' not found in the DataFrame.")

if country_avg_rating is not None:
    print("\nAverage Rating by Country:")
    print(country_avg_rating)

if top_categories is not None:
    print("\nTop 3 Categories with Highest Average Rating:")
    print(top_categories)

#Save results to local VM as CSV 
if country_avg_rating is not None:
    country_avg_rating.to_csv('Sangramsing-Kayte.csv', index=False)

if top_categories is not None:
    top_categories.to_csv('top_categories.csv', index=False)

print("Results saved locally")