import numpy as np
def submatrix_with_n_numbers(A):
    if not np.issubdtype(A.dtype, np.integer):
        raise ValueError("Matrix is not of integer type.")
    return np.sum(np.array(A, dtype=np.int64).reshape(len(A), -1).T[np.logical_or(A[::75] == -1, A[75:] == -1)])
