
import numpy as np

def submatrix_with_particular_sum(matrix):
    matrices = []
    rows, columns = matrix.shape
    for size in range(1, min(rows, columns) + 1):
        for row in range(0, rows - size + 1):
            for column in range(0, columns - size + 1):
                submatrix = matrix[row:(row + size), column:(column + size)]
                if np.sum(submatrix) == 432:
                    matrices.append(submatrix)
    return matrices
