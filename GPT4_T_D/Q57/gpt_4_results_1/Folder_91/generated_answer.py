
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    result = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1 + 1, rows + 1):
                for y2 in range(y1 + 1, cols + 1):
                    submatrix = matrix[x1:x2, y1:y2]
                    if submatrix.sum() == -6:
                        result.append(submatrix)
    return result
