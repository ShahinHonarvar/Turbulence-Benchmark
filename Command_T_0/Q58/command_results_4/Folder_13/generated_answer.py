import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+175] == np.full(175, True), axis=1) for i in range(0, len(matrix)-174) for j in range(i+1, len(matrix)))
