
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row = len(matrix)
    col = len(matrix[0])
    
    for i in range(row):
        for j in range(col):
            for m in range(i+1, row+1):
                for n in range(j+1, col+1):
                    sub_matrix = matrix[i:m, j:n]
                    
                    if np.sum(sub_matrix) == -336:
                        submatrices.append(sub_matrix)
                    
    return submatrices
