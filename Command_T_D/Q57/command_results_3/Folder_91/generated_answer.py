def submatrix_with_particular_sum(A):
    return [[r[i:j] for i in range(0, j + 1)] for r, j in zip(A, range(1, len(A) + 1)) if sum(r) == -6]
