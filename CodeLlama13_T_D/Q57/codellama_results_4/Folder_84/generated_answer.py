
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0] - i, matrix.shape[1] - j))
            
            # Fill the temporary matrix with the elements of the main matrix
            for k in range(temp_matrix.shape[0]):
                for l in range(temp_matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all elements in the temporary matrix is equal to -308
            if np.sum(temp_matrix) == -308:
                # If it is, add the temporary matrix to the result list
                result.append(temp_matrix)
    
    # Return the result list
    return result
