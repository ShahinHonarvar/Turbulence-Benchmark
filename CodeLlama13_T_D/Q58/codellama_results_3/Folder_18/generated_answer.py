
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 104
    count = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            submatrix = matrix[i][j]
            if len(submatrix) == n:
                count += 1
                
    return count
