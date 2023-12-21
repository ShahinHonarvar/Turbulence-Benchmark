
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):  
            for m_rows in range(row, rows):
                for n_cols in range(col, cols):
                    submatrix = matrix[row: m_rows + 1, col: n_cols + 1]
                    if submatrix.size == 68:
                        count += 1
    return count
