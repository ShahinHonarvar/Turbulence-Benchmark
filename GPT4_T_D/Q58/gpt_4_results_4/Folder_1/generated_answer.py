
import numpy as np

def submatrix_with_n_numbers(matrix):

    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for p in range(i+1, rows+1):
                for q in range(j+1, cols+1):
                    if (p-i)*(q-j) == 23:
                        count += 1
    return count
