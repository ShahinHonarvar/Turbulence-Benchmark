
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if j + 3 <= cols:
                submatrix = matrix[i:i+3, j:j+3]
                if np.sum(submatrix) == 95:
                    count += 1
    return count
