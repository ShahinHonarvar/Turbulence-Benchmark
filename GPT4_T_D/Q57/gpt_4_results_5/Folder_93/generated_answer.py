
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for submatrix_height in range(1, rows + 1):
        for submatrix_width in range(1, columns + 1):
            for i in range(0, rows - submatrix_height + 1):
                for j in range(0, columns - submatrix_width + 1):
                    submatrix = matrix[i:i + submatrix_height, j:j + submatrix_width]
                    if np.sum(submatrix) == -65:
                        submatrices.append(submatrix.tolist())
    return submatrices
