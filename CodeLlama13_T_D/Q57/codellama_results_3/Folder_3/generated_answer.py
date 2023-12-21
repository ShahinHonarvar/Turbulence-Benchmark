
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    
    for i in range(rows-1):
        for j in range(cols-1):
            current_sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    current_sum += matrix[k][l]
                if current_sum == 54:
                    return [matrix[i:k+1, j:l+1]]
            else:
                continue
        else:
            continue
    
    return []
