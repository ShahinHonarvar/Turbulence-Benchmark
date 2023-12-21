
import numpy as np

def submatrix_with_n_numbers(np_matrix):
    count = 0
    for row in range(np_matrix.shape[0]):
        for col in range(np_matrix.shape[1]):
            for m in range(row, np_matrix.shape[0]):
                for n in range(col, np_matrix.shape[1]):
                    if (m-row+1)*(n-col+1) == 24:
                        count += 1
    return count
