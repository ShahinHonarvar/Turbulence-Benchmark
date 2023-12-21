import numpy as np
def submatrix_with_particular_sum(A):
    return np.where(A == -4, np.array([submatrix(A, i, j) for i in range(len(A)) for j in range(len(A))]), np.array([])).tolist()
def submatrix(A, i, j):
    return A[i][j]
