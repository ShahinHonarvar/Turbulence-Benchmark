
import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_columns = matrix.shape
    
    count = 0
    for row in range(num_rows):
        for column in range(num_columns):
            for window_row in range(row, num_rows):
                for window_column in range(column, num_columns): 
                    submatrix = matrix[row:window_row + 1, column:window_column + 1]
                    if submatrix.size == 24:
                        count += 1
    return count
