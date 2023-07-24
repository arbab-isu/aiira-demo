import pandas as pd
import numpy as np

# Load the CSV
df = pd.read_csv('data/merged_hourly_data.csv')

# Shortlist the desired columns
df = df[[ 'M_Trans', 'W_PH', 'W_ECppm500', 'A_CO2ppm', 'A_RH', 'L_r', 'M_Accum']]

# Generate a "Batch" column, starting from 1
df['Batch'] = range(1, len(df) + 1)

# Move the Batch column to the first position
first_column = df.pop('Batch')
df.insert(0, 'Batch', first_column)

# Replace NaNs with a desired value, here I replace with 0
df.fillna(0, inplace=True)

#shortlist dataframe to 200 rows
df = df.head(200)

# Save the cleaned dataframe to a new CSV file
df.to_csv('data/cleaned_merged_hourly_data.csv', index=False)