
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    indices = np.indices((rows, cols)).reshape(2, -1).T
    submatrices = []
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            for pos in indices:
                if pos[0]+r <= rows and pos[1]+c <= cols:
                    submatrix = matrix[pos[0]:pos[0]+r, pos[1]:pos[1]+c]
                    if np.sum(submatrix) == -97:
                        submatrices.append(submatrix)
    return submatrices
