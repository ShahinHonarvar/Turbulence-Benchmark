import numpy as np
def submatrix_with_particular_sum(arr):
    A = np.sum(arr, axis=0) == 80
    return [arr[i] for i in range(len(arr)) if A[i]]
