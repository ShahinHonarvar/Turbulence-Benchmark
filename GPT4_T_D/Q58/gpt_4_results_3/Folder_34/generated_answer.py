
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for row_size in range(1, row + 1):
        for col_size in range(1, col + 1):
            if row_size * col_size == 83:
                for x in range(row - row_size + 1):
                    for y in range(col - col_size + 1):
                        count += 1
    
    return count
