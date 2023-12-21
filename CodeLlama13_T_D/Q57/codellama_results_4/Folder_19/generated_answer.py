
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary variable to store the sum of integers in the submatrix
            temp_sum = 0
            
            # Loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current integer to the temporary variable
                    temp_sum += matrix[k][l]
            
            # If the sum of integers in the submatrix is -97, add the submatrix to the result list
            if temp_sum == -97:
                result.append(matrix[i:i+1, j:j+1])
    
    # Return the result list
    return result
