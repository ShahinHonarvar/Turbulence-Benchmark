
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    flat_matrix = matrix.flatten()
    for i in flat_matrix:
        if i == 1:
            count += 1
    return count
