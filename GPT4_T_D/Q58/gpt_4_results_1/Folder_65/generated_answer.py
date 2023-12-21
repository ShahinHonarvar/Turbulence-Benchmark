
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = np.shape(matrix)
    
    for row_size in range(1, rows+1):
        for col_size in range(1, columns+1):
            if row_size * col_size == 35:
                count += (rows - row_size + 1) * (columns - col_size + 1)
    return count
