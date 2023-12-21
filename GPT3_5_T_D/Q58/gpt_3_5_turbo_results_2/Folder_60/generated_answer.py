
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] == 88:
                submatrix = matrix[i:i+2, j:j+2]
                if np.sum(submatrix) == 352:
                    count += 1

    return count
