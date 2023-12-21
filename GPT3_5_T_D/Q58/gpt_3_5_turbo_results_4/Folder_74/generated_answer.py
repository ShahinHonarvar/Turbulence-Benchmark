
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    
    for i in range(rows):
        for j in range(columns):
            if i+5 <= rows and j+5 <= columns:
                sub_matrix = matrix[i:i+5, j:j+5]
                if np.count_nonzero(sub_matrix == 48) == 25:
                    count += 1
    
    return count
