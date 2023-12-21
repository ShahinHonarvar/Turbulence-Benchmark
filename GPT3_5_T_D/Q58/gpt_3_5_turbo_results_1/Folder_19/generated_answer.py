
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    
    for i in range(row - 1):
        for j in range(col - 1):
            if matrix[i, j] == 17:
                if (matrix[i+1:i+2, j:j+2] == 17).all():
                    count += 1
                    
    return count
