
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows - 4):
        for j in range(columns - 4):
            sub_matrix = matrix[i:i+5, j:j+7]
            if np.sum(sub_matrix == 35) == 35:
                count += 1
    return count
