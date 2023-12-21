import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if matrix.shape[0] == 1:
        return [matrix]
    elif matrix.shape[1] == 1:
        return [[row] for row in matrix]
    else:
        return [
            [row[i:j+1] for i in range(0, matrix.shape[1]-1)]
            for j in range(0, matrix.shape[1]-1)
            for row in matrix
        ]
