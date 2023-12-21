
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    size_range = range(min(rows, cols), 0, -1)
    submatrices = []
    for submatrix_size in size_range:
        for i in range(rows - submatrix_size + 1):
            for j in range(cols - submatrix_size + 1):
                submatrix = matrix[i:i+submatrix_size, j:j+submatrix_size]
                if np.sum(submatrix) == -4:
                    submatrices.append(submatrix)
    
    return submatrices
