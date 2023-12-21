
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(0, rows - 1):
        for c in range(0, cols - 1):
            if matrix[r, c] == 130:
                submatrix = matrix[r:r+2, c:c+2]
                if np.count_nonzero(submatrix == 130) == 4:
                    count += 1
    return count
