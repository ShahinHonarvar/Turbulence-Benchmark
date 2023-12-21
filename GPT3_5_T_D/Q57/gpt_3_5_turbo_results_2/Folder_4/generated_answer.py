
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i+1, nrows+1):
                for l in range(j+1, ncols+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 87:
                        result.append(submatrix.tolist())
    
    return result
