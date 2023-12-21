import numpy as np
def submatrix_with_particular_sum(arr):
    # Your code here
    return np.where(np.all(np.sum(arr, axis=1) == -86, axis=1))[0]
