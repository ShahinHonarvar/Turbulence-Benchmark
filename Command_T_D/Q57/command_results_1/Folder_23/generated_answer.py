def submatrix_with_particular_sum(matrix):
    return [row[1:-1] for row in range(len(matrix)) if sum(row) == 59]
