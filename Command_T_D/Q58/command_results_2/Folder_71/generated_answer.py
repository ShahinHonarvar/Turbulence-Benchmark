import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.all(matrix[i:i + 78] == matrix[i + 78:i + 156], axis=1) for i in range(0, len(matrix), 78))
