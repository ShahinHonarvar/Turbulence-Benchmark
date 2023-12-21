
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the current submatrix starting from (i, j)
            submatrix = matrix[i:, j:]
            
            # Check if the sum of all integers in the submatrix equals -863
            if np.sum(submatrix) == -863:
                # If it does, add the submatrix to the results list
                results.append(submatrix)
    
    # Return the results list
    return results
