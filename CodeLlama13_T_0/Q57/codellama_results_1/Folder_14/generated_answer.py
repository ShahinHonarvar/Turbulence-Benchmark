
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Add the current element to the temporary list
            temp.append(matrix[i,j])
            
            # Iterate over the remaining elements of the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k,l])
            
            # Check if the sum of all elements in the temporary list is equal to -93
            if np.sum(temp) == -93:
                # If so, add the submatrix to the result list
                result.append(temp)
    
    # Return the result list
    return result
