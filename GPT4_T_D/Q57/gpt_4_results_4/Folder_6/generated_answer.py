
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = np.shape(matrix)

    for i in range(rows):
        for j in range(cols):
            for m in range(i+1, rows+1):
                for n in range(j+1, cols+1):
                    submatrix = matrix[i:m, j:n]
                    if np.sum(submatrix) == 126:
                        result.append(submatrix.tolist())
    
    return result
