
import numpy as np

def submatrix_with_particular_sum(matrix):
    shape = matrix.shape
    submatrices = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            for x in range(i, shape[0]):
                for y in range(j, shape[1]):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.sum(submatrix) == 411:
                        submatrices.append(submatrix)
    return submatrices
