def submatrix_with_n_numbers(A):
    return sum(1 for x in range(len(A)) for y in range(len(A)) if A[x][y] == 120)
