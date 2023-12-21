
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i+1, rows+1):
                for n in range(j+1, cols+1):
                    submatrix = matrix[i:m, j:n]
                    if submatrix.size == 60:
                        count += 1
    return count
