
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i+1, matrix.shape[0]+1):
                for y in range(j+1, matrix.shape[1]+1):
                    submatrix = matrix[i:x, j:y]
                    if np.sum(submatrix) == -811:
                        result.append(submatrix.tolist())
    return result
