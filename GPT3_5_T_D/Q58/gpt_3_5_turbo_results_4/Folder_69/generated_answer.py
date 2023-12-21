
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    
    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] == 126:
                for k in range(i, rows):
                    for l in range(j, columns):
                        if (k - i + 1) * (l - j + 1) == 126:
                            count += 1
                            
    return count
