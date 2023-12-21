
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 126
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_sum = np.sum(matrix[i:k+1, j:l+1])
                    if submatrix_sum == target_sum:
                        count += 1
                        
    return count
