def submatrix_with_particular_sum(A):
    return [submatrix for i in range(len(A)) for j in range(len(A[i])) for submatrix in A[i][j:]]
