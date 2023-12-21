
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the current submatrix
            current_submatrix = []
            
            # Loop through each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Loop through each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the submatrix
                    current_submatrix.append(matrix[k, l])
            
            # Check if the sum of all elements in the submatrix is -336
            if np.sum(current_submatrix) == -336:
                # If it is, add the submatrix to the results list
                result.append(current_submatrix)
    
    # Return the results list
    return result
