
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 146):
        for j in range(matrix.shape[1] - 146):
            if all(matrix[i:i+147, j:j+147].flat == 147):
                count += 1
    return count
