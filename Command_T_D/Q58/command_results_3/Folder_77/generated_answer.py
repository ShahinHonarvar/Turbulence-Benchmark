import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.array([np.all(matrix[x:x+179] == x) for x in range(len(matrix))]), axis=1)))
