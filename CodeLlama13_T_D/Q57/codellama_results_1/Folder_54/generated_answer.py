
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over all possible starting indices for the submatrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the current submatrix
            curr_sum = np.sum(matrix[i:i+2, j:j+2])
            
            # If the sum is equal to -59, add the submatrix to the result list
            if curr_sum == -59:
                result.append(matrix[i:i+2, j:j+2])
    
    # Return the result list
    return result
