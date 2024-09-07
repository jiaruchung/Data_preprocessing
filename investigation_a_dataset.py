#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:18:55 2024

@author: admin
"""
import pandas as pd

# Load the dataset
# Load the CSV file into a DataFrame
file_path = 'tmdb_5000_credits.csv'  # Replace with your correct file path
file_path
df = pd.read_csv(file_path)
df

print(df.head())

# Get the size of the DataFrame (rows, columns)
print("Size of the DataFrame:", df.shape)

# Get the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing data
print("\nCheck for missing data:")
print(df.isnull().sum())

# Get basic information about the DataFrame
print("\nBasic info about the DataFrame:")
print(df.info())


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
# 1. Remove duplicate rows if any
df_cleaned = df.drop_duplicates()
print("\nShape of the dataset after removing duplicates:", df_cleaned.shape)

# 2. Handle missing values (dropping rows with missing data)
df_cleaned = df_cleaned.dropna()  # You could also choose to fillna() if necessary
print("\nShape of the dataset after handling missing values:", df_cleaned.shape)

# 3. Convert data types if needed (example: convert a string column to datetime)
# For example, if you have a date column that is a string, convert it like this:
# df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

# After cleaning, inspect the data again
print("\nCleaned dataset:")
print(df_cleaned.head())


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Save the cleaned dataset if needed
df_cleaned.to_csv('cleaned_tmdb_5000_credits.csv', index=False)

print(df['movie_id'].describe())

# Visualize the distribution of 'budget'
plt.figure(figsize=(10,6))
sns.histplot(df['movie_id'], kde=True, bins=30)
plt.title('Distribution of Budget')
plt.xlabel('Budget')
plt.ylabel('Frequency')
plt.show()