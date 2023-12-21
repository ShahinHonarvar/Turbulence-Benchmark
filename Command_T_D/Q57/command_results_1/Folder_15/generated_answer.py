import numpy as np
def submatrix_with_particular_sum(arr):
    return [sub for row in range(len(arr)) for sub in range(len(arr[0]))
            if np.sum(arr[row][:sub] + arr[row][sub+1:]) == -9]
