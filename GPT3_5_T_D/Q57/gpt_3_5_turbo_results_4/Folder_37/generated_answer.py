
import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = []
    for i in range(n):
        for j in range(m):
            for x in range(i+1, n+1):
                for y in range(j+1, m+1):
                    sub = np.sum(matrix[i:x, j:y])
                    if sub == -82:
                        result.append(matrix[i:x, j:y])
    return result
