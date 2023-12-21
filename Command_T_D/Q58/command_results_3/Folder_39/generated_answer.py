import numpy as np
def submatrix_with_n_numbers(A):
    A = np.array(A)
    n, m = len(A), len(A[0])
    if n < m:
        return 0
    if m == n:
        return 1
    if n == 1:
        return A[0].count(59)
    return sum(A[i].count(59) for i in range(n))
