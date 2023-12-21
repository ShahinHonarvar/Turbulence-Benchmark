import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix[0]))
            for submatrix in [[row] + matrix[row][:-1]]
            if np.sum(submatrix) == -50]
