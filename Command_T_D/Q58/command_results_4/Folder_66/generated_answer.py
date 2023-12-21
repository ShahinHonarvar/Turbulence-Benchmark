import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.where(np.sum(arr,axis=1)%42==0,1,0))
