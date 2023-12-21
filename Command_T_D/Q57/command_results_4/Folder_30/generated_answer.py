import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    matrix_sum = np.sum(matrix, axis=1)
    return [np.array(matrix[i:i + 21]) for i in range(len(matrix)) if matrix_sum[i] == 21]
