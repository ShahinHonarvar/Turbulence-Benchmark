
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows - 1):
        for j in range(cols - 1):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.prod(submatrix.shape) == 84 and np.sum(submatrix) == 84:
                        count += 1

    return count
