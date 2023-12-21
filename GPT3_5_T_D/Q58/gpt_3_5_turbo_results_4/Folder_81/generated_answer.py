
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 97:
                for p in range(i, len(matrix)):
                    for q in range(j, len(matrix[0])):
                        submatrix = matrix[i:p+1, j:q+1]
                        if np.size(submatrix) == 97:
                            count += 1
    return count
