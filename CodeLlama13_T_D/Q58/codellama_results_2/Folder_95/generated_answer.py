
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows-7):
        for j in range(cols-7):
            submatrix = matrix[i:i+8, j:j+8]
            if np.count_nonzero(submatrix == 87) == 64:
                submatrices.append(submatrix)
    return len(submatrices)
