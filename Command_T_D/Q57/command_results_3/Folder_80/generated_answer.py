import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return [list(row) for row in matrix if sum(row) == 245]
