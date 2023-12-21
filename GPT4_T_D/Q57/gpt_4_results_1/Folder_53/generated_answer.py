
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    res = []
    for row in range(rows):
        for col in range(cols):
            for x in range(row + 1, rows + 1):
                for y in range(col + 1, cols + 1):
                    submatrix = matrix[row:x, col:y]
                    if np.sum(submatrix) == -37:
                        res.append(submatrix)
    return res
