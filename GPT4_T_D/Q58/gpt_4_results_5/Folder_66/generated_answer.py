
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for m in range(i, rows):
                for n in range(j, columns):
                    sub_matrix = matrix[i:m+1, j:n+1]
                    if sub_matrix.size == 42:
                        count += 1
    return count
