
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 138:
                for k in range(i+1, rows+1):
                    for l in range(j+1, cols+1):
                        sub_matrix = matrix[i:k, j:l]
                        if np.sum(sub_matrix) == 138 * sub_matrix.size:
                            count += 1
    return count
