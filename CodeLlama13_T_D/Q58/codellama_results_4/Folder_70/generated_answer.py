
import numpy as np
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows - 163 + 1):
        for j in range(cols - 173 + 1):
            submatrix = np.array([[matrix[i+x][j+y] for x in range(163)] for y in range(173)])
            if np.count_nonzero(submatrix) == 286:
                submatrices.append(submatrix)
    return len(submatrices)
