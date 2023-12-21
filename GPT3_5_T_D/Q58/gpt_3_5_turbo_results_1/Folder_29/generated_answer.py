
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[i:k+1, j:l+1]
                    if sub_matrix.size == 19 and np.all(sub_matrix == 19):
                        count += 1
    
    return count
