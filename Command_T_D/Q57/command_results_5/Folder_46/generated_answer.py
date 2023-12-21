import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    matrix = np.sum(matrix, axis=0) == 416
    return [matrix[i][:][:].tolist() for i in range(matrix.shape[0])]
