
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = np.shape(matrix)
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    if (k - i + 1) * (l - j + 1) == 40:
                        count += 1
    return count
