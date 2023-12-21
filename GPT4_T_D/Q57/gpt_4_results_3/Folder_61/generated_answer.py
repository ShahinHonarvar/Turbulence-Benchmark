
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for r_size in range(1, rows+1):
        for c_size in range(1, cols+1):
            for row in range(0, rows-r_size+1): 
                for col in range(0, cols-c_size+1): 
                    submatrix = matrix[row:row+r_size, col:col+c_size]
                    if np.sum(submatrix) == 8:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
