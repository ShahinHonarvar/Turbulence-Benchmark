
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    num_rows, num_columns = matrix.shape
    
    for x1 in range(num_rows):
        for y1 in range(num_columns):
            for x2 in range(x1, num_rows):
                for y2 in range(y1, num_columns):
                    submatrix = matrix[x1:x2+1, y1:y2+1]
                    if np.sum(submatrix) == 394:
                        submatrices.append(submatrix)
                        
    return submatrices
