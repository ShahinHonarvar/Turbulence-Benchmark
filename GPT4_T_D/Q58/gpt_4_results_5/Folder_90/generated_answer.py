
import numpy as np

def submatrix_with_n_numbers(matrix):
    count_submatrix = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i+1, matrix.shape[0]+1):
                for l in range(j+1, matrix.shape[1]+1):
                    if (k-i)*(l-j) == 176:
                        count_submatrix += 1
    return count_submatrix
