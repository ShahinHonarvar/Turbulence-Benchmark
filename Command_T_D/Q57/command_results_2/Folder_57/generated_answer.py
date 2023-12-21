import numpy as np
def submatrix_with_particular_sum(np_matrix):
    matrix = np.array(np_matrix)
    return [submatrix for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) for submatrix in zip(matrix[i], matrix[i][j]) if sum(submatrix) == 13]
