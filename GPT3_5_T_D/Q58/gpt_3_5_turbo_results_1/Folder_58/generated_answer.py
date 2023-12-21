
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 185:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        submatrix_sum = np.sum(matrix[i:k+1, j:l+1])
                        if submatrix_sum == 185 * (k-i+1) * (l-j+1):
                            count += 1
    return count
