
import numpy as np

def submatrix_with_n_numbers(my_matrix):
    count = 0
    rows, cols = my_matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x+1-i)*(y+1-j) == 7:
                        count += 1
    return count
