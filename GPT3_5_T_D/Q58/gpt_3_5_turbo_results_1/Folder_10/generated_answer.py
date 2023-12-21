
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            if r <= rows - 8 and c <= cols - 7:
                submatrix = matrix[r:r+8, c:c+7]
                if np.count_nonzero(submatrix == 56) == 56:
                    count += 1
    return count
