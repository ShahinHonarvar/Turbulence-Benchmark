import numpy as np
def submatrix_with_particular_sum(arr):
    return [r for r in np.where(np.sum(arr[i:j+1],axis=1)==64) if np.sum(r) == 64]
