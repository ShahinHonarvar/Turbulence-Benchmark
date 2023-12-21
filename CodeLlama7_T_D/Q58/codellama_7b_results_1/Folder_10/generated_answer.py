
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if (matrix[i][j] == 56).all():
                count += 1
    
    return count
