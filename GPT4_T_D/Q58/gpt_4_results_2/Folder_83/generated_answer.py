
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for row in range(rows):
        for col in range(cols):
            for x in range(row, rows):
                for y in range(col, cols):
                    if (x-row+1)*(y-col+1) == 47:
                        count += 1
    return count
