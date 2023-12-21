
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if i + 1 < rows and j + 1 < columns:
                submatrix = matrix[i:i+2, j:j+2]
                if np.sum(submatrix) == 54:
                    count += 1
    return count
