
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    
    count = 0
    for i in range(rows - 72):
        for j in range(cols - 72):
            submatrix = matrix[i:i + 73, j:j + 73]
            if np.count_nonzero(submatrix) == 73 * 73:
                count += 1
    
    return count
