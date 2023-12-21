
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 18 + 1):
        for j in range(len(matrix[i]) - 18 + 1):
            if sum(matrix[i:i+18, j:j+18].flatten()) == 18 * 18:
                count += 1
    return count
