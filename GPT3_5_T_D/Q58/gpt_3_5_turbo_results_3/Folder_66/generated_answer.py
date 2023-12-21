
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 42:
                for m in range(i, rows):
                    for n in range(j, cols):
                        sub_matrix = matrix[i:m+1, j:n+1]
                        if sub_matrix.size == 42:
                            count += 1
    return count
