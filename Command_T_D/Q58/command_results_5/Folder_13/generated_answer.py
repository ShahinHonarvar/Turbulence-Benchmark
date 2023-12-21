import numpy as np
def submatrix_with_n_numbers(A):
    if A.shape[0] < 175:
        return 0
    Y = A[A.shape[0] - 174:].T
    m = Y.shape[0]
    X = np.full((m, 175), -1)
    for i in range(m):
        for j in range(174):
            if Y[i][j] != -1:
                X[i][j + 1] = Y[i][j]
    return sum(1 for x in X if x != -1)
