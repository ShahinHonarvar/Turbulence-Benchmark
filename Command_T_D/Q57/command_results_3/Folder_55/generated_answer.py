def submatrix_with_particular_sum(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0])) if sum(row) == 1]
