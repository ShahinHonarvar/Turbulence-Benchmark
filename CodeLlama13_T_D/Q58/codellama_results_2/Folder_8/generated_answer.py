
import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    
    for i in range(num_rows - 28):
        for j in range(num_cols - 28):
            submatrix = matrix[i:i+29, j:j+29]
            if np.all(submatrix == 29):
                count += 1
                
    return count
