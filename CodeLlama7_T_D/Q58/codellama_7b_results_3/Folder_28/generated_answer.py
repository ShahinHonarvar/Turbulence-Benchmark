
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            if matrix[i, j] == 37:
                submatrix = matrix[i:i+3, j:j+3]
                if all(x == 37 for x in submatrix.ravel()):
                    count += 1
    return count
