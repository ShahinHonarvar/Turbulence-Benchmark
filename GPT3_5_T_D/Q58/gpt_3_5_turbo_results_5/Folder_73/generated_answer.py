
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Check if the current element is 41
            if matrix[i, j] == 41:
                # Check if the submatrix contains 41 integers
                if np.count_nonzero(matrix[i:i+2, j:j+2] == 41) == 4:
                    count += 1
    
    return count
