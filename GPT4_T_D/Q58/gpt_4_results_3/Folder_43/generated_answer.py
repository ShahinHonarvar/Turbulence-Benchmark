
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for p in range(n_rows):
        for q in range(n_cols):
            for i in range(p+1, n_rows+1):
                for j in range(q+1, n_cols+1):
                    if (i-p)*(j-q) == 85:
                        count += 1
    return count
