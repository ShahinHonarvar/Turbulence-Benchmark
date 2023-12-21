
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    n_rows, n_cols = mat.shape[0], mat.shape[1]
    
    for x1 in range(n_rows):
        for y1 in range(n_cols):
            for x2 in range(x1, n_rows):
                for y2 in range(y1, n_cols):
                    submatrix = mat[x1:x2+1, y1:y2+1]
                    if submatrix.size == 193:
                        count += 1
    return count
