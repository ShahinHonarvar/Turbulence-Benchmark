
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if all(matrix[i][j:j+n] == matrix[i+1][j:j+n] == ... == matrix[i+n-1][j:j+n]):
                count += 1
    return count
