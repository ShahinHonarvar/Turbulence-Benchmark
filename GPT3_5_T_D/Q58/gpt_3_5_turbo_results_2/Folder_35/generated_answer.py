 
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 111:
                for k in range(i+1, rows+1):
                    for l in range(j+1, cols+1):
                        if np.sum(matrix[i:k, j:l] == 111) == (k-i)*(l-j):
                            count += 1
    
    return count
