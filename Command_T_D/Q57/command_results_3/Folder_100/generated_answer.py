def submatrix_with_particular_sum(matrix):
    return [list(submatrix) for submatrix in [matrix[i:j + 1, k:l + 1] for i in range(len(matrix)) for j in range(i, len(matrix)) for k in range(len(matrix[i])) for l in range(k, len(matrix[i])) if sum(submatrix) == 28]]
