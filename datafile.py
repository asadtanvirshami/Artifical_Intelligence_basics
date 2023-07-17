import pandas as pd
# Read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

#first five rows of the dataframe
head = df.head()

# Read data from Excel File and print the first five rows
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df2 = pd.read_excel(xlsx_path)

#first five rows of the dataframe
head2 = df.head()

# Get the column as a series
x_series = df['Length']

# Get the column as a dataframe
x_dataframe = df[['Length']]

# Access to multiple columns
multiple_cols = df[['Artist','Length','Genre']]
print(multiple_cols)
