import pandas as pd
import re

# function to extract number from a string
def extract_number(s):
    return int(re.findall(r'\d+', s)[0])

# read data from the csv file
df = pd.read_csv('data/wu_dsm.csv')

# apply the function to each cell in the selected columns
df['Temperature'] = df['Temperature'].apply(extract_number)
df['Dew Point'] = df['Dew Point'].apply(extract_number)
df['Humidity'] = df['Humidity'].apply(extract_number)
df['Wind Speed'] = df['Wind Speed'].apply(extract_number)
df['Wind Gust'] = df['Wind Gust'].apply(extract_number)
df['Pressure'] = df['Pressure'].apply(extract_number)
df['Precip.'] = df['Precip.'].apply(extract_number)

# convert conditions to numerical values
conditions = df['Condition'].unique()
conditions_dict = {conditions[i]: i for i in range(len(conditions))}
df['Condition'] = df['Condition'].map(conditions_dict)

# Generate a "Batch" column, starting from 1
df['Batch'] = range(1, len(df) + 1)

# Select columns and rename them to match the manufacturing data
df = df[['Batch', 'Temperature', 'Dew Point', 'Humidity', 'Wind Speed', 'Wind Gust', 'Pressure', 'Precip.', 'Condition']]

# replace periods in column names with an empty string
df.columns = df.columns.str.replace('.', '')

# save to new csv
df.to_csv('data/transformed_data.csv', index=False)

print("Ended")