
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for k in range(rows - i + 1):
                for l in range(cols - j + 1):
                    submatrix = matrix[k:k + i, l:l + j]
                    if submatrix.size == 46:
                        count += 1
                        
    return count
