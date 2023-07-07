import pandas as pd

# Read the hacker_news.csv file from data directory
df = pd.read_csv("./day_19/hacker_news.csv")
print(df)

# Get the first five rows
print(df.head())

# Get the last five rows
print(df.tail())

# Get the title column as pandas series
panda_series = df.columns
print(panda_series)

# Count the number of rows and columns
shape = df.shape
print(shape)

# Filter the titles which contain python
python_titles = df[df["title"].str.contains("python", case = False)]
print(python_titles)

# Filter the titles which contain JavaScript
javascript_titles = df[df["title"].str.contains("javascript", case = False)]
print(javascript_titles)

# Explore the data and make sense of it
df.pop("id")
df.pop("num_points")
df.pop("num_comments")
print(df)