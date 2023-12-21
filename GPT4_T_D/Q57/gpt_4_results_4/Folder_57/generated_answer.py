
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    submatrices = []

    for size in range(1, min(rows, columns) + 1):
        for i in range(rows - size + 1):
            for j in range(columns - size + 1):

                submatrix = matrix[i:i+size, j:j+size]
                if np.sum(submatrix) == 13:
                    submatrices.append(submatrix)
                    
    return submatrices
