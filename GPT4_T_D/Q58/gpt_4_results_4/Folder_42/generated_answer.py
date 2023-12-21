
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    if (x+1-i)*(y+1-j) == 193:
                        count += 1
    return count
