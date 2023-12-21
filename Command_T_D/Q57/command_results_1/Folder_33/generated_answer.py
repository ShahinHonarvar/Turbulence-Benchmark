def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return [[-811] + list(row) + [-811] for row in matrix]
