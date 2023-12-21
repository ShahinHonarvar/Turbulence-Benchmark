
import numpy as np

def submatrix_with_particular_sum(matrix):
    
    def sum_submatrix(matrix, x1, y1, x2, y2):
        return np.sum(matrix[x1:x2+1, y1:y2+1])
 
    m, n = matrix.shape
    results = []
    for x1 in range(m):
        for y1 in range(n):
            for x2 in range(x1, m):
                for y2 in range(y1, n):
                    if sum_submatrix(matrix, x1, y1, x2, y2) == 0:
                        results.append(matrix[x1:x2+1, y1:y2+1])
                    
    return results
