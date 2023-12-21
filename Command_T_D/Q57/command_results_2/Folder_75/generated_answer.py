def submatrix_with_particular_sum(matrix):
    if not matrix.shape[0] == matrix.shape[1] == 2:
        return []
    if matrix[0][0] + matrix[0][1] != 16:
        return []
    if matrix[1][0] + matrix[1][1] != 16:
        return []
    return [[matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]]
