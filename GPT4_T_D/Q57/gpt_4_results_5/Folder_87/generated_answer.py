
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    out_arr = []
    
    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for i in range(rows - row_size + 1):
                for j in range(cols - col_size + 1):
                    submat = mat[i:i+row_size, j:j+col_size]
                    if np.sum(submat) == 35:
                        out_arr.append(submat)
    
    return out_arr
