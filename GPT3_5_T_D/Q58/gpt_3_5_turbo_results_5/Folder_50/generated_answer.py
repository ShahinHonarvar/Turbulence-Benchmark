
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] == 40:
                if matrix[i][j+1] == 40 and matrix[i+1][j] == 40 and matrix[i+1][j+1] == 40:
                    count += 1
    return count
