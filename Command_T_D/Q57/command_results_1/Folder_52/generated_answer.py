def submatrix_with_particular_sum(matrix):
    return [x for x in [[a[i][j] for i in range(len(a)) if sum(a[i]) == 100] for j in range(len(a[0]))] if x]
