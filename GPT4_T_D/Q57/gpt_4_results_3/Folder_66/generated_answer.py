
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    
    for size_x in range(1, rows + 1):
        for size_y in range(1, cols + 1):
            for i in range(rows - size_x + 1):
                for j in range(cols - size_y + 1):
                    submatrix = matrix[i:i+size_x, j:j+size_y]
                    if np.sum(submatrix) == 99:
                        submatrices.append(submatrix.tolist())
    return submatrices
