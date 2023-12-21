
import numpy as np

def insert_after_index(x):
    x = np.array(x)
    return np.insert(x, x.shape[0] + 1, [86, 77], 1)
