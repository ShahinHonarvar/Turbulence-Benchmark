import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.where(np.array([arr[i:i+185] for i in range(0,len(arr),185)]),axis=1),axis=0)))
