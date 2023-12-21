import numpy as np
def submatrix_with_n_numbers(A):
    n = len(A)
    if n == 1:
        return 1
    else:
        return np.sum(np.sum(np.sum(A[i:j+17] == 1, axis=1) == 17 for i in range(n-1)) for j in range(n-1))
