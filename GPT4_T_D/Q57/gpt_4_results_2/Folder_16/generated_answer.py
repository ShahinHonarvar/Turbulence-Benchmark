
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for x in range(n):
        for y in range(m):
            for x1 in range(x, n):
                for y1 in range(y, m):
                    sub = matrix[x:x1+1, y:y1+1]
                    if np.sum(sub) == -157:
                        result.append(sub)
    return result
