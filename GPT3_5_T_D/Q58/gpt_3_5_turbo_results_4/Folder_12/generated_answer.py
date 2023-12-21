
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 46:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        if ((k - i + 1) * (l - j + 1)) == 46:
                            count += 1
    return count
