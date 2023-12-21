import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+127] == np.full(127, matrix[i]), axis=1) for i in range(len(matrix)-127) for j in range(i+1, len(matrix)))
