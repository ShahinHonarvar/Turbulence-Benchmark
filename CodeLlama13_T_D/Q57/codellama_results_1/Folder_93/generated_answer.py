
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Get the shape of the matrix
    rows, cols = matrix.shape
    
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each possible row and column indices
    for i in range(rows):
        for j in range(cols):
            # Get the current submatrix
            submatrix = matrix[i:, j:]
            
            # Check if the sum of all integers in the submatrix is -65
            if np.sum(submatrix) == -65:
                # If so, add the submatrix to the list
                submatrices.append(submatrix)
                
    # Return the list of submatrices with the particular sum
    return submatrices
