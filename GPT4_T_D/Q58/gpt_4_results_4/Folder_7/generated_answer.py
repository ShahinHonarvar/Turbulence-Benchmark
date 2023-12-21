
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row_count in range(1, rows+1):
        for column_count in range(1, columns+1):
            for row in range(rows-row_count+1):
                for column in range(columns-column_count+1):
                    submatrix = matrix[row:row+row_count, column:column+column_count]
                    if submatrix.size == 121:
                        count += 1
    return count
