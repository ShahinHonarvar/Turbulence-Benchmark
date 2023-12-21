
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = np.shape(matrix)
    
    for x1 in range(m):
        for y1 in range(n):
            for x2 in range(x1, m):
                for y2 in range(y1, n):
                    subMatrix = matrix[x1:x2+1, y1:y2+1]
                    if np.sum(subMatrix) == -93:
                        result.append(subMatrix)
    return result
