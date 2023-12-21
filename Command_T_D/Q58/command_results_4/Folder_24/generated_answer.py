import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(np.all(np.array(A[i:j, j:k] == A[i:j, k:n] == np.full(n, 51)), axis=0))
