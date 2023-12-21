
import numpy as np

def submatrix_with_particular_sum(matrix):
    size_x, size_y = matrix.shape
    submatrices = []
    for x in range(size_x):
        for y in range(size_y):
            for i in range(x+1, size_x+1):
                for j in range(y+1, size_y+1):
                    submatrix = matrix[x:i, y:j]
                    if np.sum(submatrix) == -37:
                        submatrices.append(submatrix)
    return submatrices
