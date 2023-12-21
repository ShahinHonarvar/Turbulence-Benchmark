import numpy as np
def submatrix_with_particular_sum(arr):
    return [submatrix for i in range(len(arr)) for j in range(len(arr[0])) for submatrix in range(i, i+1, 1) for submatrix in range(j, j+1, 1) if np.sum(arr[submatrix:submatrix + i]) == -6]
