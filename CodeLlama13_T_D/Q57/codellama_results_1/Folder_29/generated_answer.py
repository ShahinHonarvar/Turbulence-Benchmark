
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each possible starting row and column index
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Initialize a temporary submatrix with the current starting row and column index
            temp = matrix[i:i+2, j:j+2]
            
            # Check if the sum of all integers in the temporary submatrix is equal to 84
            if np.sum(temp) == 84:
                # If yes, add the submatrix to the result list
                result.append(temp)
    
    # Return the result list
    return result
