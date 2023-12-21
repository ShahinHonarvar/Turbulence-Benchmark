 
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                for n in range(i, rows):
                    for m in range(j, cols):
                        submatrix = matrix[i:n+1, j:m+1]
                        if np.sum(submatrix) == 122:
                            count += 1
    return count
