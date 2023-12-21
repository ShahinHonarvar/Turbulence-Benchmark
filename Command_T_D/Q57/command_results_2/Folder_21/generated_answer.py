import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.array(sub, dtype=int) for i in range(len(arr)) for j in range(len(arr[0])) for sub in (arr[i][j:j+3], arr[i+1:i+3][j], arr[i:i+2][j:j+2], arr[i:i+3][j:j+2]) if np.sum(sub) == -936]
