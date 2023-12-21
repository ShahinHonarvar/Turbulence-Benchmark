
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 37:
                count += check_submatrix(matrix, i, j)
    return count

def check_submatrix(matrix, row, col):
    rows, cols = matrix.shape
    count = 0
    for i in range(row, rows):
        for j in range(col, cols):
            if matrix[i, j] == 37:
                count += 1
            if count == 37:
                return 1
            if count > 37:
                return 0
    return 0
