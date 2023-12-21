
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape

    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] == 127:
                for k in range(i, rows):
                    for l in range(j, columns):
                        if np.sum(matrix[i:k+1, j:l+1]) == 127 * (k - i + 1) * (l - j + 1):
                            count += 1
    
    return count
