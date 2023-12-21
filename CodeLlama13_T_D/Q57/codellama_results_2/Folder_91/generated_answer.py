
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over all possible starting indices for each row
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((len(matrix), len(matrix[0])), dtype=np.int)
            
            # Copy the elements of the main matrix to the temporary matrix
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    temp_matrix[k-i][l-j] = matrix[k][l]
            
            # Check if the sum of all elements in the temporary matrix is -6
            if np.sum(temp_matrix) == -6:
                # If it is, add the temporary matrix to the result list
                result.append(temp_matrix)
    
    # Return the result list
    return result
