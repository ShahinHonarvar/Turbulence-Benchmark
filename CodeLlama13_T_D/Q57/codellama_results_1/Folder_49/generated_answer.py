
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Get the shape of the matrix
    m, n = matrix.shape
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(m):
        # Iterate over each column of the matrix
        for j in range(n):
            # Check if the sum of the submatrix starting from (i, j) equals -42
            if np.sum(matrix[i:, j:]) == -42:
                # If yes, add the submatrix to the result list
                result.append((i, j))
    
    return result
