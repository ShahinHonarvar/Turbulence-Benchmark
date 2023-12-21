
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to -86
            if sum(temp) == -86:
                # If it is, add the submatrix to the result list
                result.append(temp)
    
    # Return the result list
    return result
