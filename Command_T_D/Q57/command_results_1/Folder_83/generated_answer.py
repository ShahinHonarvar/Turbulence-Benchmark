def submatrix_with_particular_sum(matrix):
    return [[row[i:j + 1] for i in range(len(row) - 1)] for j in range(len(row) - 1) for row in matrix]
