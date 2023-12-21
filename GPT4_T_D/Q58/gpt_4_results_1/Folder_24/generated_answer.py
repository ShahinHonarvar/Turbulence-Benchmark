
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows - row, cols - col) + 1):
                submatrix = mat[row:row+size, col:col+size]
                if submatrix.size == 51:
                    count += 1
    return count
