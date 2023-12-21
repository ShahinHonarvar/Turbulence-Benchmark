
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            count += sum(np.size(matrix[row:row+i+1, col:col+j+1]) == 2 for i in range(rows - row) for j in range(cols - col))
    return count
