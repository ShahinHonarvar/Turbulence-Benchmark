import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+185] == np.full(185, True), axis=1) for i in range(len(matrix)-184) for j in range(i+185))
