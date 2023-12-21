
import numpy as np

def submatrix_with_sum(matrix, sum_value):
    results = []
    rows, cols = matrix.shape
    
    for submatrix_size in range(1, min(rows, cols)+1):
        for r in range(rows - submatrix_size + 1):
            for c in range(cols - submatrix_size + 1):
                submatrix = matrix[r:r+submatrix_size, c:c+submatrix_size]
                if np.sum(submatrix) == sum_value:
                    results.append(submatrix.tolist())
                    
    return results

def submatrix_with_particular_sum(matrix):
    return submatrix_with_sum(matrix, -811)
