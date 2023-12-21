
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submatrix = matrix[i:m+1, j:n+1]
                    if submatrix.size == 2:
                        count += 1
                        
    return count
