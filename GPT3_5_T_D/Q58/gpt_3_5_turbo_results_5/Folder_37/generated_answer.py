
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 64:
                if i + 7 <= rows and j + 7 <= cols:
                    submatrix = matrix[i:i+8, j:j+8]
                    if np.count_nonzero(submatrix) == 64:
                        count += 1
    
    return count
