
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 96:
                if i + 3 <= rows and j + 3 <= cols:
                    submatrix = matrix[i:i+3, j:j+3]
                    if np.count_nonzero(submatrix == 96) == 9:
                        count += 1
    return count
