
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape

    for row in range(rows):
        for column in range(columns):
            for i in range(row, rows):
                for j in range(column, columns):
                    submatrix = matrix[row:i + 1, column:j + 1]
                    if submatrix.size == 94:
                        count += 1
    
    return count
