
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submatrix = matrix[i:m+1, j:n+1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 416:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
