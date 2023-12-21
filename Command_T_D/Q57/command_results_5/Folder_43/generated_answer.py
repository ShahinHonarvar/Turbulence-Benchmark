import numpy as np
def submatrix_with_particular_sum(matrix):
    return [
        matrix[i1:i2+1][j1:j2+1]
        for i1, j1, i2, j2 in zip(range(len(matrix)), range(len(matrix[0])), range(1, len(matrix)-1), range(1, len(matrix[0])-1))
        if np.sum(matrix[i1:i2+1][j1:j2+1]) == -81
    ]
