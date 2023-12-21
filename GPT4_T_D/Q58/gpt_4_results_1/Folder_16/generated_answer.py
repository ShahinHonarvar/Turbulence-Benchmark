
import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for r in range(rows+1):
        for c in range(cols+1):
            for x in range(r):
                for y in range(c):
                    if (r-x)*(c-y) == 154:
                        count += 1
    return count
