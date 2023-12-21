
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 57:
                for x in range(i, len(matrix)):
                    for y in range(j, len(matrix[0])):
                        if (x - i + 1) * (y - j + 1) == 57:
                            count += 1
    return count
