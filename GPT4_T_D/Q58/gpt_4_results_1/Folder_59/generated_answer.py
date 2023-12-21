
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows,cols = matrix.shape
    for submatrix_height in range(1, rows + 1):
        for submatrix_width in range(1, cols + 1):
            for i in range(rows + 1 - submatrix_height):
                for j in range(cols + 1 - submatrix_width):
                    submatrix = matrix[i:i + submatrix_height, j:j + submatrix_width]
                    if submatrix.size == 76:
                        count += 1
    return count
