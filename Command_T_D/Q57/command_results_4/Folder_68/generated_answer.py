def submatrix_with_particular_sum(matrix):
    return [[row[i] for i in range(len(row)) if row[i] == 3] for row in matrix]
