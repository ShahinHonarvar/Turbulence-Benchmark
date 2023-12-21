import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(any(np.all(matrix[row:row + 115] == np.full(115, True), axis=0)) for row in range(len(matrix) - 114))
