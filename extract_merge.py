import pandas as pd
import requests

# List of file download links
links = ['https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Blood%20Pressure%20Quesstionnaire.csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Demographics.csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Diabetes%20Questionnaire.csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Individual%20Food%20Consumption%20Day%201%20(Reduced).csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Individual%20Food%20Consumption%20Day%202%20(Reduced).csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Total%20Nutrients%20Day%201.csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/NHANES%20Total%20Nutrients%20Day%202.csv',
         'https://raw.githubusercontent.com/CSSEHealthcare/Dietary-Behavior-Dataset/master/Data/USDA%20Food%20Codes.csv',
         # Add more file links as needed
        ]

# Helper function to download and read a csv file from a link
def download_and_read_csv(link):
    response = requests.get(link)
    response.raise_for_status()
    return pd.read_csv(link)

# Download and read all the datasets
dataframes = [download_and_read_csv(link) for link in links]

# Merge the datasets on the 'id' column
merged_dataset = pd.concat(dataframes, axis=0, ignore_index=True)

# save the output to a csv file
merged_dataset.to_csv('merged_dataset.csv')
