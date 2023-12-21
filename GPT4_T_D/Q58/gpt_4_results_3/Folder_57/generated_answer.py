
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for submatrix_size in range(1, min(rows, columns) + 1):
        for row in range(rows - submatrix_size + 1):
            for column in range(columns - submatrix_size + 1):
                submatrix = matrix[row: row + submatrix_size,
                                   column: column + submatrix_size]
                if submatrix.size == 92:
                    count += 1
    return count
