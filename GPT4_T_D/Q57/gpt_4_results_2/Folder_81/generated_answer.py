
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for x1 in range(m):
        for y1 in range(n):
            for x2 in range(x1, m):
                for y2 in range(y1, n):
                    submatrix = matrix[x1:x2+1, y1:y2+1]
                    if np.sum(submatrix) == -90:
                        result.append(submatrix)
    return result
