
import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 80:
        return 0
    count = 0
    for rows in range(matrix.shape[0]):
        for cols in range(matrix.shape[1]):
            for drows in range(rows, matrix.shape[0]):
                for dcols in range(cols, matrix.shape[1]):
                    if (drows-rows+1)*(dcols-cols+1) == 80:
                        count += 1
    return count
