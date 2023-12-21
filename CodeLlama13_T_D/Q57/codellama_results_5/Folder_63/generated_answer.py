
import numpy as np

def submatrix_with_particular_sum(arr):
    rows, cols = arr.shape
    for i in range(rows-2):
        for j in range(cols-2):
            submat = arr[i:i+3,j:j+3]
            if np.sum(submat) == 64:
                return submat
    return []
