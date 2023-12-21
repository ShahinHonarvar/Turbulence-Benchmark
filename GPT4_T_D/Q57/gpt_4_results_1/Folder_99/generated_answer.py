
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    res = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    submatrix = matrix[x1:x2+1, y1:y2+1]
                    if np.sum(submatrix) == -185:
                        res.append(submatrix)
    return res
