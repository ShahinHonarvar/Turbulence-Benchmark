
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Fill in the temporary matrix with the elements of the main matrix
            for k in range(temp_matrix.shape[0]):
                for l in range(temp_matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Calculate the sum of all elements in the temporary matrix
            sum_elements = np.sum(temp_matrix)
            
            # If the sum is equal to 752, add the submatrix to the results list
            if sum_elements == 752:
                results.append(temp_matrix)
    
    # Return the results list
    return results
