
import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    rows, cols = mat.shape
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1 + 1, rows + 1):
                for y2 in range(y1 + 1, cols + 1):
                    submatrix = mat[x1:x2, y1:y2]
                    if np.sum(submatrix) == 382:
                        result.append(submatrix)
    return result
