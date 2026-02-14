# 25280028
# Rubina Noor

from pandas import json_normalize
def extract_data_API(url):

    import requests
    import pandas as pd
    import os

    # HealthData.gov API for "Access and Use of Telemedicine During COVID-19"
    # url = "https://data.cdc.gov/data.json"

    response = requests.get(url)

    df= pd.DataFrame()

    # if request is unsuccessful, give error
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return df
    else:
        data= response.json()
        print(f"DATA FETCHED SUCCESSFULLY: {len(data)} RECORDS ")

        df = json_normalize(data, sep='_')
        print(df.head())

        os.makedirs("data/raw", exist_ok=True)

        df.to_csv("data/raw/healthdata_raw.csv", index = False)
        df.to_json("data/raw/healthdata_raw.json", orient = "records")
        print("Data saved to data/raw/")

    return df    
