
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
                for k in range(i+1, len(matrix)):
                    for l in range(j+1, len(matrix[k])):
                        if matrix[k][l] == 1:
                            count += 1
                        else:
                            break
                    else:
                        break
    return count
