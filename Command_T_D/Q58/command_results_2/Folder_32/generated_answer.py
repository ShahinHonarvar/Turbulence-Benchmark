import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[start:start+max_size] == 103, axis=1) for start in range(0, len(matrix), max_size))
