import pandas as pd
import numpy as np

# Load the CSV
df = pd.read_csv('data/merged_hourly_data.csv')

# Shortlist the desired columns
df = df[[ 'M_Trans', 'W_PH', 'W_ECppm500', 'A_CO2ppm', 'A_RH', 'L_r', 'M_Accum']]
df = df.rename(columns={
    'M_Trans': 'Transpiration', 
    'W_PH': 'Water PH', 
    'W_ECppm500': 'Water Conductivity', 
    'A_CO2ppm': 'Air CO2', 
    'A_RH': 'Air Humidity', 
    'L_r': 'Red Light', 
    'M_Accum': 'BioMass'})

# Shortlist 100 values from middle of the dataframe
df = df[520:620]

# Generate a "Batch" column, starting from 1
df['Batch'] = range(1, len(df) + 1)

# Move the Batch column to the first position
first_column = df.pop('Batch')
df.insert(0, 'Batch', first_column)

# Replace NaNs with a desired value, here I replace with 0
df.fillna(0, inplace=True)



# Save the cleaned dataframe to a new CSV file
df.to_csv('data/cleaned_merged_hourly_data.csv', index=False)