
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    
    # Loop over all possible submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            
            # Calculate the sum of the current submatrix
            curr_sum = np.sum(matrix[i:i+2, j:j+2])
            
            # If the sum is equal to the desired value, add the submatrix to the result list
            if curr_sum == 38:
                result.append(matrix[i:i+2, j:j+2])
                
    # Return the result list
    return result
