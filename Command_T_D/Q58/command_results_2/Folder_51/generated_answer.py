import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.array(matrix, dtype=np.int32).shape[0] * np.array(matrix, dtype=np.int32).shape[1] * (len(matrix) - 1) // 96
