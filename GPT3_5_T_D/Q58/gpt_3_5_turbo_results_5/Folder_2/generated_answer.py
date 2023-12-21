
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i+1, len(matrix)+1):
                for l in range(j+1, len(matrix[0])+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 107 * (k-i) * (l-j):
                        count += 1
    return count
