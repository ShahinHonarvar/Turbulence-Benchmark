
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 130:
                submatrix = matrix[i: i+2, j: j+2]
                if submatrix.shape == (2, 2) and np.all(submatrix == 130):
                    count += 1
    return count
