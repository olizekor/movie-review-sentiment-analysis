import nltk
import os

# Create a directory to store NLTK data
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)

# Download required packages to the directory
nltk.download("punkt", download_dir="nltk_data")
nltk.download("stopwords", download_dir="nltk_data")
nltk.download("wordnet", download_dir=nltk_data_dir)
nltk.download("omw-1.4", download_dir=nltk_data_dir)

# Tell NLTK to use this directory
nltk.data.path.append("nltk_data")

print(nltk.__version__)
print(f"Downloaded NLTK data to {nltk_data_dir}")
print("nltk is in: ", nltk_data_dir)
print(nltk.data.find("tokenizers/punkt"))