import numpy as np
def submatrix_with_particular_sum(arr):
    return [x for x in np.array_split(arr, 78) if x.size]
