
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 121:
                count += 1
                for k in range(i+1, rows):
                    for l in range(j+1, cols):
                        if (matrix[k, l] == 121 and 
                            np.sum(matrix[i:k+1, j:l+1]) == 121):
                            count += 1
    
    return count
