
import numpy as np

def submatrix_with_n_numbers(np_arr):
    count = 0
    rows, cols = np_arr.shape
    for r_dim in range(1, rows+1):
        for c_dim in range(1, cols+1):
            if r_dim*c_dim == 83:
                # Start scanning the matrix for such submatrices
                for r_idx in range(rows-r_dim+1):
                    for c_idx in range(cols-c_dim+1):
                        count += 1 
    return count
