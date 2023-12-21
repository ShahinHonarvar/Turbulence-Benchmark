import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+179] == np.full(179, True), axis=1) for i in range(len(matrix)-178) for j in range(i+1, len(matrix)))
