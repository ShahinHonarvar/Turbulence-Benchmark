 
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    
    for r in range(rows):
        for c in range(columns):
            for i in range(r, rows):
                for j in range(c, columns):
                    submatrix = matrix[r:i+1, c:j+1]
                    if np.sum(submatrix) == -617:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
