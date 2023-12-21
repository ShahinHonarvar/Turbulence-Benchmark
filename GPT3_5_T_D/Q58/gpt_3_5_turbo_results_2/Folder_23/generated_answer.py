
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 69:
                for sub_rows in range(i, rows):
                    for sub_cols in range(j, cols):
                        if np.sum(matrix[i:sub_rows+1, j:sub_cols+1]) == 69:
                            count += 1
                        
    return count
