
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    
    # checking for all possible submatrices
    for x in range(row):
        for y in range(col):
            for dx in range(1, row - x + 1):
                for dy in range(1, col - y + 1):
                    submatrix = matrix[x:x+dx, y:y+dy]
                    if np.sum(submatrix) == -82:
                        result.append(submatrix.tolist())
                        
    return result
