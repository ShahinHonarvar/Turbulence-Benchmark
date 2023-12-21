
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for size in range(1, min(rows,cols)+1):
        for r in range(rows - size + 1):
            for c in range(cols - size + 1):
                submatrix = matrix[r:r+size, c:c+size]
                if np.sum(submatrix) == 3:
                    submatrices.append(submatrix.tolist())

    return submatrices
