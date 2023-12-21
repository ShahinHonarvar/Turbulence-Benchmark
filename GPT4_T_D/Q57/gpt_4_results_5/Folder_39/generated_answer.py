
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for x in range(rows):
        for y in range(cols):
            for dx in range(1,rows - x + 1):
                for dy in range(1,cols - y + 1):
                    submat = matrix[x:x+dx, y:y+dy]
                    if submat.sum() == 66:
                        result.append(submat)
    return result
