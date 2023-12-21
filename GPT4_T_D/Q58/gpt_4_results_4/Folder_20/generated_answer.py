
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(r+1, rows+1):
                for j in range(c+1, cols+1):
                    submatrix = matrix[r:i, c:j]
                    if np.size(submatrix) == 49:
                        count += 1

    return count
