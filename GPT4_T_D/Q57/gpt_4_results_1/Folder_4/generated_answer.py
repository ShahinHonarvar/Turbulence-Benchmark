
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Create a result list
    result = []
    # Get the shape of the matrix
    rows, cols = matrix.shape
    # Check all possible submatrices
    for x in range(rows):
        for y in range(cols):
            for width in range(1, cols - y + 1):
                for height in range(1, rows - x + 1):
                    submatrix = matrix[x:x+height, y:y+width]
                    # If sum of elements of submatrix is 87, append to result
                    if submatrix.sum() == 87:
                        result.append(submatrix)
    return result
