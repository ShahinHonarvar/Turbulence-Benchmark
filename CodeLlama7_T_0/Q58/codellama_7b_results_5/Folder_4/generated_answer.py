
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 15 + 1):
        for j in range(len(matrix[i]) - 15 + 1):
            if sum(matrix[i:i+15, j:j+15].flatten()) == 15:
                count += 1
    return count
