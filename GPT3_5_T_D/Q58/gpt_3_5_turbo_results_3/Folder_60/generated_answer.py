
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if (i + 2 < rows) and (j + 2 < cols):
                submatrix = matrix[i:i+3, j:j+3]
                if np.count_nonzero(submatrix == 88) == 9:
                    count += 1
    return count
