import numpy as np
def submatrix_with_particular_sum(arr):
    return [ [sub] for sub in np.where(np.sum(sub,axis=1)==-37)[0] ]
