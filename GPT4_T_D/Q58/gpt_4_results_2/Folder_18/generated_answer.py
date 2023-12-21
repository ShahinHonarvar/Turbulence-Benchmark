
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for subrow in range(1, shape[0]+1):
        for subcol in range(1, shape[1]+1):
            if subrow * subcol == 104:
                count += (shape[0] - subrow + 1) * (shape[1] - subcol + 1)
    return count
