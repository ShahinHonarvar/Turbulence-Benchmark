
import numpy as np

def submatrix_with_n_numbers(matrix):
    
    rows, columns = matrix.shape
    count = 0
    
    for row in range(rows):
        for column in range(columns):
            for sub_row in range(row + 1, rows + 1):
                for sub_col in range(column + 1, columns + 1):
                    if np.size(matrix[row:sub_row, column:sub_col]) == 47:
                        count += 1
    
    return count
