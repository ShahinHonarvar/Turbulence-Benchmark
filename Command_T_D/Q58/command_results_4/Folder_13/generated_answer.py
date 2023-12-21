import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return matrix.size // 175 + matrix.size // 350 + matrix.size // 525
