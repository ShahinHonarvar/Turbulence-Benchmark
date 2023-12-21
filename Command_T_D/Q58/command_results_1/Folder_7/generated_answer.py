import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:j+121] == [x for x in range(120)]))
