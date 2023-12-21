
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 72 + 1):
        for j in range(len(matrix[i]) - 72 + 1):
            if len(set(matrix[i:i+72, j:j+72]))) == 72:
                count += 1
    return count
