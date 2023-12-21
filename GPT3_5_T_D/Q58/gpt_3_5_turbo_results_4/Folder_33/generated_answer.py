
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 118:
                for m in range(i, len(matrix)):
                    for n in range(j, len(matrix[m])):
                        if np.sum(matrix[i:m+1, j:n+1]) == 118*(m-i+1)*(n-j+1):
                            count += 1
    return count
