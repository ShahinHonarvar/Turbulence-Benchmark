import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.array(arr[i:j, i:j]) for i in range(len(arr)) for j in range(i+1, len(arr)) if np.sum(arr[i:j, i:j]) == -82]
