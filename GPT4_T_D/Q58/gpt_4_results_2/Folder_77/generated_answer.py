
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for p in range(i, shape[0]):
                for q in range(j, shape[1]):
                    submatrix = matrix[i:p+1, j:q+1]
                    if submatrix.size == 179:
                        count += 1
    return count
