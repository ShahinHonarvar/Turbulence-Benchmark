
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current element as the first element
            temp_submatrix = np.array([[matrix[i, j]]])
            
            # Loop through the remaining elements in the row and column
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    # Add the current element to the temporary submatrix
                    temp_submatrix = np.append(temp_submatrix, [[matrix[k, l]]], axis=0)
                    
                    # Check if the sum of all integers in the temporary submatrix is equal to -394
                    if np.sum(temp_submatrix) == -394:
                        # If it is, add the temporary submatrix to the result list
                        result.append(temp_submatrix)
    
    # Return the result list
    return result
