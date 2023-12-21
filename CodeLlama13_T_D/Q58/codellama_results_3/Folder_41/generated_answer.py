
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if all(matrix[i][j:j+n] == matrix[i+1][j:j+n] for _ in range(n)):
                count += 1
    return count
