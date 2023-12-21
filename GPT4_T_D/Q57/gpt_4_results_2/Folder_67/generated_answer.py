
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []

    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submatrix = matrix[i:x, j:y]
                    if np.sum(submatrix) == 40:
                        submatrices.append(submatrix)

    return submatrices
