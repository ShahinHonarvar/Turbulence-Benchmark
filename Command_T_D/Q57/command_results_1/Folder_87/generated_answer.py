import numpy as np
def submatrix_with_particular_sum(A):
    m, n = A.shape
    A = np.array(A)
    masks = []
    for i in range(m):
        for j in range(n):
            curr = A[i][j]
            curr += 35
            if curr <= n:
                masks.append((i, j, curr))
    return masks
