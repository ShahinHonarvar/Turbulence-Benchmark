import numpy as np
def submatrix_with_particular_sum(A):
    result = []
    A_array = np.array(A)
    if A_array.shape[0] * A_array.shape[1] == 0:
        return []
    for i in range(A_array.shape[0]):
        for j in range(A_array.shape[1]):
            if A[i][j] == -97:
                result += [[i, j]]
    return result
