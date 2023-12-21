def submatrix_with_particular_sum(matrix):
    return [[row[i:i + 7] for row in matrix] for i in range(len(matrix[0])) if len(row) == 8 and sum(row) == -82]
