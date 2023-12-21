
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.sum(submatrix) == -57:
                        result.append(submatrix.tolist())
    return result
