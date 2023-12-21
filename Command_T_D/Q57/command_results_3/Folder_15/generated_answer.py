import numpy as np
def submatrix_with_particular_sum(matrix):
    return [np.array(matrix[i:j + 1]) for i in range(0, len(matrix) - 1) for j in range(0, len(matrix[0]) - 1) if matrix[i:j + 1].sum() == -9]
