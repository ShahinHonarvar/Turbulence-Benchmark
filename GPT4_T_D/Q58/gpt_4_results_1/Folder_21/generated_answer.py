
import numpy as np

def submatrix_with_n_numbers(matrix_2D):
    nrows, ncols = np.array(matrix_2D.shape) - 138 
    count = 0
    for x in range(nrows + 1):
        for y in range(ncols + 1):
            arr = matrix_2D[x:x+139, y:y+139]
            if arr.size == 139:
                count += 1
    return count
