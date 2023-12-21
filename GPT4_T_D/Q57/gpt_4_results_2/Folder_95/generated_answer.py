
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    
    for width in range(1, matrix.shape[1]+1): 
        for height in range(1, matrix.shape[0]+1): 
            for row in range(matrix.shape[0] - height + 1):
                for col in range(matrix.shape[1] - width + 1):
                    submatrix = matrix[row : row+height, col : col+width]
                    if np.sum(submatrix) == 19:
                        result.append(submatrix)
    return result
