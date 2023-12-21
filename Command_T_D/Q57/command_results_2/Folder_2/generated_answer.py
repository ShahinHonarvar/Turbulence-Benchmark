import numpy as np
def submatrix_with_particular_sum(arr):
    return np.array([submatrix for submatrix in arr if np.sum(submatrix) == -863]).tolist()
