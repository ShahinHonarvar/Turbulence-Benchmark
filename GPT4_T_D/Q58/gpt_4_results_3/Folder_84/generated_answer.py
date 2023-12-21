
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i, matrix.shape[0]):
                for n in range(j, matrix.shape[1]):
                    submatrix = matrix[i:m+1, j:n+1]
                    if submatrix.size == 127:
                        count += 1
    return count
