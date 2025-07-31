import os
import numpy as np

def load_glove_embeddings(filename):
    embeddings = {}
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath = os.path.join(base_dir, "glove_embeddings", filename)
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype = "float32")
            embeddings[word] = vector
    return embeddings