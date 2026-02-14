# 25280028
# Rubina Noor

def load_local_dataset(file_path):
    import pandas as pd

    # loading the downloaded kaggle dataset 
    df = pd.read_csv(file_path)

    # printing first 5 entries of the loaded dataset
    print(df.head())

    return df