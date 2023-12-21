
import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
        
    count = 0
    rows, columns = matrix.shape
    
    for sub_row in range(1, rows+1):
        for sub_col in range(1, columns+1):
            if sub_row*sub_col == 59:
                count += (rows - sub_row + 1) * (columns - sub_col + 1)
                
    return count
