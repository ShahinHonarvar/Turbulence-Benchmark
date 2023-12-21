
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 130):
        for j in range(matrix.shape[1] - 130):
            if sum(matrix[i:i+131, j:j+131]) == 131 * 131:
                count += 1
    return count
