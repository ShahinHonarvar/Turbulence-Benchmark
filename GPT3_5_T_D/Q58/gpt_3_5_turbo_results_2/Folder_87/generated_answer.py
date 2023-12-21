 
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 7):
        for j in range(cols - 7):
            sub_matrix = matrix[i:i+8, j:j+8]
            if np.sum(sub_matrix) == 96:
                count += 1
    return count
