
import numpy as np

def submatrix_with_particular_sum(matrix):
    list_submatrices = []
    rows, cols = matrix.shape

    for x in range(rows):
        for y in range(cols):
            for a in range(x+1, rows+1):
                for b in range(y+1, cols+1):
                    submatrix = matrix[x:a, y:b]
                    if np.sum(submatrix) == 87:
                        list_submatrices.append(submatrix)
                    
    return list_submatrices
