import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix[i][:53] == i) == 53 for i in range(len(matrix)))
