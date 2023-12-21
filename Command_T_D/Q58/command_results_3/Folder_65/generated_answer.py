import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.where(np.sum(arr,axis=0)>=35,1,0))
