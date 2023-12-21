
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows < 10 or cols < 10:
        return 0
    for i in range(rows - 9):
        for j in range(cols - 9):
            sub_matrix = matrix[i:i+10, j:j+10]
            if np.size(sub_matrix) == 100:
                count += 1
    return count
