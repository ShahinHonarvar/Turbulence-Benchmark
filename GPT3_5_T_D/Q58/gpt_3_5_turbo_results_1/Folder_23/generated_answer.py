
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 69:
                sub_matrix = matrix[i:i+2, j:j+2]
                if np.count_nonzero(sub_matrix == 69) == 4:
                    count += 1
    
    return count
