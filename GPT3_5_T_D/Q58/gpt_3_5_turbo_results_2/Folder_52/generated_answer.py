
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if matrix[i][j] == 147:
                submatrix = matrix[i:i+3, j:j+3]
                if np.sum(submatrix) == 441:
                    count += 1
    return count
