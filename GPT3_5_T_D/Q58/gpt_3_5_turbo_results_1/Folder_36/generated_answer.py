
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 131:
                for k in range(i+1, rows+1):
                    for l in range(j+1, cols+1):
                        if np.sum(matrix[i:k, j:l]) == 131:
                            count += 1
    
    return count
