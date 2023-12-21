
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target = 185
    
    for i in range(rows):
        for j in range(cols):
            for a in range(i, rows):
                for b in range(j, cols):
                    submatrix = matrix[i:a+1, j:b+1]
                    if submatrix.size == target and np.sum(submatrix) == (target * 185):
                        count += 1
    
    return count
