
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for rdimension in range(rows+1):
        for cdimension in range(cols+1):
            for x in range(rows-rdimension+1):
                for y in range(cols-cdimension+1):
                    submatrix = matrix[x:xdimension+x, y:y+cdimension]
                    sum_submatrix = np.sum(submatrix)
                    if sum_submatrix == -261:
                        result.append(submatrix)
                    
    return result
