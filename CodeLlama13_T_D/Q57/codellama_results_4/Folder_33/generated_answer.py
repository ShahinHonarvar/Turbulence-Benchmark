
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Extract the current submatrix
            submatrix = matrix[i:i+2, j:j+2]
            
            # Check if the sum of all integers in the current submatrix is equal to -811
            if np.sum(submatrix) == -811:
                # If it is, add it to the result list
                result.append(submatrix)
    
    # Return the result list
    return result
