
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 5
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and matrix[i+1][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j+1] == 1 and matrix[i+2][j+2] == 1:
                count += 1
    return count
