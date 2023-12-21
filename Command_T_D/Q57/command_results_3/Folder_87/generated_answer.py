import numpy as np
def submatrix_with_particular_sum(A):
    a, b, c, d = np.where(A == 35)
    if not a.size or not b.size or not c.size or not d.size:
        return []
    A[a] = 1
    A[b] = 1
    A[c] = 1
    A[d] = 1
    a = np.arange(len(A))
    return [A[a[i]:a[i + 1]] for i in range(len(a) - 1)]
