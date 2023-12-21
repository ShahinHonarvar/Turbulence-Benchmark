import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.linalg.matrix_power(np_matrix, 3).tolist()
