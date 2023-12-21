
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if sum(matrix[i:j+1]) == n:
                count += 1
    
    return count
