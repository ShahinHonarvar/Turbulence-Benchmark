
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows-3):
        for j in range(cols-3):
            submatrix = matrix[i:i+4,j:j+4]
            if np.all(submatrix == 48):
                count += 1
    return count
