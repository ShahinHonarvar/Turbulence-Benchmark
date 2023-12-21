import numpy as np
def submatrix_with_particular_sum(A):
    B = np.sum(A, axis=1) == -61
    return [A[i][j] for i in range(len(A)) for j in range(len(A[0])) if B[i][j]]
