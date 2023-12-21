def submatrix_with_particular_sum(A):
    return [s for i in range(len(A)) for j in range(len(A[0])) for s in A[i][j:]] if A[i][0] == 2 else []
