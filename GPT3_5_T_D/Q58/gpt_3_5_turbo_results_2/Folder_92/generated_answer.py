
import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    
    row_count = len(matrix)
    col_count = len(matrix[0])
    count = 0
    
    for i in range(row_count-1):
        for j in range(col_count-1):
            submatrix = np.array([
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]]
            ])
            if submatrix.size == 8:
                count += 1
    
    return count
