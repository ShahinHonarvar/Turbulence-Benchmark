
import numpy as np
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows-114):
        for j in range(cols-114):
            if all(matrix[i:i+115,j:j+115] == 1):
                count += 1
    return count
