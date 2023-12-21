import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(np.sum(matrix[i][:5]) for i in range(len(matrix)))
