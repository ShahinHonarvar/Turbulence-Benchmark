
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Get the shape of the matrix
    m, n = matrix.shape
    
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each row and column of the matrix
    for i in range(m):
        for j in range(n):
            # Get the submatrix starting from (i, j) with size 3x3
            submatrix = matrix[i:i+3, j:j+3]
            
            # Check if the sum of all integers in the submatrix is equal to 92
            if np.sum(submatrix) == 92:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    
    return submatrices
