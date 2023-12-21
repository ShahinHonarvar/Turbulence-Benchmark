
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            row_sum = 0
            for k in range(i, rows):
                row_sum += sum(matrix[k][j:j+cols])
                if row_sum == 46 * cols:
                    count += 1
    
    return count
