
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for dx in range(1, rows - x + 1):
                for dy in range(1, cols - y + 1):
                    submatrix = matrix[x:x+dx, y:y+dy]
                    if np.sum(submatrix) == 13:
                        submatrices.append(submatrix.tolist())
                        
    return submatrices
