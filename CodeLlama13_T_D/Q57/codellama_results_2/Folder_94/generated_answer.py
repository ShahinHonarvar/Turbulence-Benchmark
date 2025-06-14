
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current submatrix has a sum equal to 92
            if np.sum(matrix[i:j+1]) == 92:
                # If so, add it to the result list
                result.append(matrix[i:j+1])
    
    # Return the result list
    return result
