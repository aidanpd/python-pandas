# This script reads a CSV file containing viewing data of a website and purchases
# made.
# See viewing_data.csv

import pandas as pd

outputFile = "viewing_data.csv"

# create a Pandas dataframe

df = pd.read_csv(outputFile)

# number of users

print(len(df.index))

# number of 640 x 960 devices

print(len(df[(df['device_width'] == 640) & (df['device_height'] == 960)]))

# first joined user

print(df[df['date_joined'] == df['date_joined'].min()]['user_id'].iloc[0])

# total spend by all of the users

print(df['spend'].sum())
