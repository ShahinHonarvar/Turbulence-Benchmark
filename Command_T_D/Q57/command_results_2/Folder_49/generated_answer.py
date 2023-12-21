import numpy as np
def submatrix_with_particular_sum(np_matrix):
    if np.sum(np_matrix) != -42:
        return []
    return [np_matrix[i][:][:].tolist() for i in range(len(np_matrix[0]))]
