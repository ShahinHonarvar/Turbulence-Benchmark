
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 131 + 1):
        for j in range(len(matrix[0]) - 131 + 1):
            if matrix[i:i+131, j:j+131].all():
                count += 1
    return count
