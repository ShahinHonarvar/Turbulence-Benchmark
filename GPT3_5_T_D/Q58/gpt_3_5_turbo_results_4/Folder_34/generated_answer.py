
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows - 1):
        for j in range(columns - 1):
            if matrix[i, j] == 83:
                if (matrix[i+1:i+3, j:j+2] == 83).all():
                    count += 1
    return count
