
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows+1):
        for j in range(cols+1):
            for p in range(i+1, rows+1):
                for q in range(j+1, cols+1):
                    if (p-i)*(q-j) == 159:
                        count += 1
    return count
