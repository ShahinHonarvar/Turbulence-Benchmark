
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows - 3 + 1):
        for j in range(columns - 3 + 1):
            submatrix = matrix[i:i+3, j:j+3]
            if np.count_nonzero(submatrix == 76) == 9:
                count += 1
    return count
