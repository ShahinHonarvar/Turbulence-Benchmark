
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the element to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to -82
            if np.sum(temp) == -82:
                # If so, add the submatrix to the result list
                result.append(temp)
    
    # Return the result list
    return result
