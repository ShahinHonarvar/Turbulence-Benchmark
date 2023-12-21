
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            if i + 1 >= 10 and j + 1 >= 10:
                submatrix = matrix[i-9:i+1, j-9:j+1]
                if submatrix.size == 100:
                    count += 1
    
    return count
