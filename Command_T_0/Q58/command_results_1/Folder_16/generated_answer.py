import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+1] == 154, axis=1) for i in range(len(matrix)-153) for j in range(i+1, len(matrix)))
