import numpy as np
def submatrix_with_n_numbers(A):
    A = np.array(A)
    if A.ndim != 2:
        return 0
    if A.shape[0] < A.shape[1]:
        return 0
    if A.shape[0] < 77:
        return 0
    N = A.shape[0]
    count = 0
    for i in range(N):
        if i % 11 == 0:
            continue
        for j in range(i, N, 11):
            if j % 11 == 0:
                continue
            A[i][j] = 77
            count += np.sum(np.any(A, axis=1))
    return count
