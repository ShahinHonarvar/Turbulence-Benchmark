
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for row in range(rows - 1):
        for col in range(cols - 1):
            if matrix[row, col] == 139:
                sub_matrix = matrix[row:row+2, col:col+2]
                if np.count_nonzero(sub_matrix == 139) == 4:
                    count += 1
                    
    return count
