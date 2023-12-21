import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(arr[i:j+1,i:j+1] == 176, axis=0) for i in range(len(arr)-175) for j in range(i, len(arr)-175))
