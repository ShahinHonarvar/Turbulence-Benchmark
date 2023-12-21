import numpy as np
def submatrix_with_particular_sum(arr):
    return [sub for i in range(len(arr)) for j in range(len(arr[0])) for sub in np.where(np.sum(arr[i][j:j+5]) == 126)]
