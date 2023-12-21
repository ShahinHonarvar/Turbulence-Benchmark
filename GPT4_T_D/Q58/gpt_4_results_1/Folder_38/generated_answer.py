
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            for k in range(r, rows):
                for l in range(c, cols):
                    sub_matrix = matrix[r:k+1, c:l+1]
                    if np.size(sub_matrix) == 34:
                        count += 1
                        
    return count
