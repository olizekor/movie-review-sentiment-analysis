import nltk
import os

nltk_path = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.insert(0, nltk_path)

from nltk.tokenize import word_tokenize

text = "This is a test sentence."
tokens = nltk.word_tokenize(text)
print(tokens)

#print("NLTK paths:", nltk.data.path)