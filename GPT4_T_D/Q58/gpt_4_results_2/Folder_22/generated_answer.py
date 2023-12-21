
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for r in range(row):
        for c in range(col):
            for subr in range(r+1, row+1):
                for subc in range(c+1, col+1):
                    if np.size(matrix[r:subr, c:subc]) == 21:
                        count += 1
    return count
