import numpy as np
def submatrix_with_particular_sum(A):
    if np.sum(A) != -20:
        return []
    return [A[i:j] for i in range(len(A)) for j in range(i, len(A))]
