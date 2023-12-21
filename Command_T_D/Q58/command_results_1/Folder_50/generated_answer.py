import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+40] == 40 * [0] + matrix[i+40:j] == 40 * [1] + matrix[j+1:j+40] == 40 * [0] + matrix[j+40:k] == 40 * [1] + matrix[k+1:k+40] == 40 * [0] + matrix[k+40:]))
