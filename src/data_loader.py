import pandas as pd
import os

def load_raw_data(filename="IMDB_Dataset.csv"):
    filepath = os.path.join("data", "raw", filename)
    return pd.read_csv(filepath)

# def load_processed_data(filename="cleaned_reviews.csv"):
#    filepath = os.path.join("data", "processed", filename)
#    return pd.read_csv(filepath)