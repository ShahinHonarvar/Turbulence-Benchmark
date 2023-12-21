
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, column = matrix.shape
    result = []
    for size in range(1, min(row, column) + 1):
        for x in range(row - size + 1):
            for y in range(column - size + 1):
                submatrix = matrix[x:x+size, y:y+size]
                if np.sum(submatrix) == -65:
                    result.append(submatrix)
    return result
