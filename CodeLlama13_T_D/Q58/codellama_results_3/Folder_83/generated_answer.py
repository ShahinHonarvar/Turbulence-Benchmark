
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row,col] == 47:
                count += 1
    return count
