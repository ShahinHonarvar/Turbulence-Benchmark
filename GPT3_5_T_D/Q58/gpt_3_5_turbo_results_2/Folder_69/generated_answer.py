
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 126:
                for m in range(i, len(matrix)):
                    for n in range(j, len(matrix[0])):
                        if np.sum(matrix[i:m+1, j:n+1]) == 126:
                            count += 1
    return count
