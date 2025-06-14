
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Copy the elements from the main matrix to the temporary matrix
            for k in range(matrix.shape[0]):
                for l in range(matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the temporary matrix equals -185
            if np.sum(temp_matrix) == -185:
                # If so, add the submatrix to the results list
                results.append(temp_matrix)
    
    # Return the results list
    return results
