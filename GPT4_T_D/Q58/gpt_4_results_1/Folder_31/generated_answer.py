
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape

    for i in range(1, row+1):
        for j in range(1, col+1):
            for m in range(i, row+1):
                for n in range(j, col+1):
                    submatrix = matrix[i-1:m, j-1:n]
                    if submatrix.size == 45:
                        count += 1
    return count
