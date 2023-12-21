import numpy as np
def submatrix_with_n_numbers(matrix):
    # find all submatrices of size 8x8
    # do it in one line to avoid creating a list and iterating it
    count = np.sum(np.sum(matrix[i:i+8, j:j+8] == 8, axis=1) == 8 for i in range(0, len(matrix), 8))
    return count
