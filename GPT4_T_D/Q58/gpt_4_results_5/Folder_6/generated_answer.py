
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for r in range(1, rows+1):
        for c in range(1, cols+1):
            for i in range(rows-r+1):
                for j in range(cols-c+1):
                    submatrix = matrix[i:i+r, j:j+c]
                    if np.size(submatrix) == 122:
                        count += 1
    return count
