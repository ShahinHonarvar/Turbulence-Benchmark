
import numpy as np

def submatrix_with_n_numbers(np_matrix):
    row, col = np_matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for x in range(i, row):
                for y in range(j, col):
                    if (x+1-i)*(y+1-j) == 45:
                        count += 1
    return count
