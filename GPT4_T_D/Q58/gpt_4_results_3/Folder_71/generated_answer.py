
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for subrow in range(row + 1):
        for subcol in range(col + 1):
            for i in range(row - subrow + 1):
                for j in range(col - subcol + 1):
                    if subrow * subcol == 78:
                        count += 1
    return count
