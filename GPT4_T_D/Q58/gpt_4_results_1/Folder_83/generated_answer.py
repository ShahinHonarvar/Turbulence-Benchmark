
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_columns = matrix.shape
    for x in range(num_rows):
        for y in range(num_columns):
            for m in range(x, num_rows):
                for n in range(y, num_columns):
                    if (m-x+1)*(n-y+1) == 47:
                        count += 1
    return count
