
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            current_sum = np.sum(matrix[i:i+2, j:j+2])
            
            # Check if the sum equals -137
            if current_sum == -137:
                # If yes, add the submatrix to the result list
                result.append(matrix[i:i+2, j:j+2])
    
    # Return the result list
    return result
