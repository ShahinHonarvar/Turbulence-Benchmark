import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+47] == 47*[i] + 47*[j] + np.array([i,j]), axis=1))
