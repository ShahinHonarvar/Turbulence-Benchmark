
import numpy as np
def submatrix_with_n_numbers(matrix):
    n = 175
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
                if count == n:
                    return 1
    return 0
