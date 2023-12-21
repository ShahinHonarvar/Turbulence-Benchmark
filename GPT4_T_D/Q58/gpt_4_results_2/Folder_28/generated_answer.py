
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for k in range(rows - i + 1):
                for l in range(cols - j + 1):
                    if np.size(matrix[k:k+i,l:l+j]) == 37:
                        count += 1
    return count
