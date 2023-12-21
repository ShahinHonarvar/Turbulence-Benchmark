
import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -38:
                        results.append(submatrix.tolist())
    
    return results
