
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[i]) - 4):
            if len(set(matrix[i:i+5, j:j+5].flatten())) == 5:
                count += 1

    return count
