import pandas as pd
import os

def load_raw_data(filename="IMDB_Dataset.csv"):
    # Go up one directory from notebooks/ → root, then into data/raw/
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath = os.path.join(base_dir, "data", "raw", filename)
    return pd.read_csv(filepath)

# def load_processed_data(filename="cleaned_reviews.csv"):
#    filepath = os.path.join("data", "processed", filename)
#    return pd.read_csv(filepath)