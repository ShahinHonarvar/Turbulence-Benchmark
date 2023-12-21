
import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    
    for i in range(num_rows - 3):
        for j in range(num_cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            
            if np.count_nonzero(submatrix == 49) == 16:
                count += 1
    
    return count
