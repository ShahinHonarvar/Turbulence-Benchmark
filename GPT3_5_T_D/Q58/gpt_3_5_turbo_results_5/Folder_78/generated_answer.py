
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 91:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        total = 0
                        for m in range(i, k+1):
                            for n in range(j, l+1):
                                total += matrix[m][n]
                        if total == 91:
                            count += 1
    return count
