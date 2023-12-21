
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    submatrix = matrix[i: x+1, j: y+1]
                    if np.sum(submatrix) == 92:
                        result.append(submatrix)
    return result
