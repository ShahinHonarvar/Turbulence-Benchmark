
import numpy as np

def submatrix_with_particular_sum(matrix):
    size = matrix.shape[0]
    result = []
    
    for x in range(size):
        for y in range(size):
            for i in range(x+1, size+1):
                for j in range(y+1, size+1):
                    submatrix = matrix[x:i, y:j]
                    if np.sum(submatrix) == 93:
                        result.append(submatrix)
                        
    return result
