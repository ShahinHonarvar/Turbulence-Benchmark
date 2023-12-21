
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the current submatrix
            current_sum = np.sum(matrix[i:, j:])
            
            # If the sum is -394, add the current submatrix to the result list
            if current_sum == -394:
                result.append((i, j))
    
    # Return the result list
    return result
