
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 35
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == n:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[i])):
                        submatrix = matrix[i:k+1, j:l+1]
                        if np.size(submatrix) == n:
                            count += 1
    
    return count
