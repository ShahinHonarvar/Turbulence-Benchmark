
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D array to store the current submatrix
            current_submatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Iterate over each element of the submatrix
            for k in range(current_submatrix.shape[0]):
                for l in range(current_submatrix.shape[1]):
                    # Check if the current element is within the bounds of the matrix
                    if i + k < matrix.shape[0] and j + l < matrix.shape[1]:
                        # Add the element to the submatrix
                        current_submatrix[k, l] = matrix[i + k, j + l]
                        
            # Check if the sum of all elements in the submatrix is equal to 93
            if np.sum(current_submatrix) == 93:
                # Add the submatrix to the results list
                result.append(current_submatrix)
    
    # Return the results list
    return result
