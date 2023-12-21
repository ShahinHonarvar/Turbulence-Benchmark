
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j:j+2].sum() == 51 and matrix[i+1][j:j+2].sum() == 51:
                count += 1
    
    return count
