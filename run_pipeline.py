# 25280028
# Rubina Noor

from Part1_extraction import extract_data_API
from load import load_local_dataset
from trends import fetch_google_trends
import json

def main():

    with open("config.json") as f:
        config = json.load(f)


    
    extraction_API_url = config["data_url"]
    local_dataset_path = config["local_dataset"]
    keywords = config["keywords"]


    # for API data extraction
    df_health = extract_data_API(extraction_API_url)
    
    # for loading local dataset
    df_local = load_local_dataset(local_dataset_path)
    
    # for fetching google trends data
    iot = fetch_google_trends(keywords)

if __name__ == "__main__":
    main()
