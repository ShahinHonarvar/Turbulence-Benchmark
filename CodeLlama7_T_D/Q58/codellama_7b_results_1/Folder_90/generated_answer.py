
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 165):
        for j in range(len(matrix[i]) - 165):
            if matrix[i:i+176, j:j+176].all():
                count += 1
    return count
