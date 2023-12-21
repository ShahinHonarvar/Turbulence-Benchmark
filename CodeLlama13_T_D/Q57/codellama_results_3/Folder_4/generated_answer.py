
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Loop over all possible starting indices for the submatrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((2, 2), dtype=np.int64)
            
            # Copy the values from the main matrix to the temporary matrix
            for k in range(2):
                for l in range(2):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the current submatrix is equal to 87
            if np.sum(temp_matrix) == 87:
                # If it is, add the submatrix to the list of found submatrices
                found_submatrices.append(temp_matrix)
    
    # Return the list of found submatrices
    return found_submatrices
