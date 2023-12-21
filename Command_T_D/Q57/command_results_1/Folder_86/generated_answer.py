import numpy as np
def submatrix_with_particular_sum(A):
    B = np.zeros((len(A), len(A)))
    for i in range(len(A)):
        for j in range(len(A)):
            B[i][j] = A[i][j] - 394
    return np.where(B == 0).tolist()
