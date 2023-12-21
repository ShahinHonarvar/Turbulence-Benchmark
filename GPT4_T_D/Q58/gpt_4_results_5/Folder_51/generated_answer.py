
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    for ro in range(rows):
        for co in range(cols):
            for r in range(ro+1, rows+1):
                for c in range(co+1, cols+1):
                    submatrix = matrix[ro:r, co:c]
                    if np.size(submatrix) == 95:
                        count += 1
    return count
