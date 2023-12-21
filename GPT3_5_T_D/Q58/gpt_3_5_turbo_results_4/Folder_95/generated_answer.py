
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 87 * submatrix.size:
                        count += 1
    
    return count
