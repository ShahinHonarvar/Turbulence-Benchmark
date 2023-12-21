
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and j + 1 < cols:
                sub_matrix = matrix[i:i+2, j:j+2]
                if np.count_nonzero(sub_matrix) == 4 and np.sum(sub_matrix) == 56:
                    count += 1
    
    return count
