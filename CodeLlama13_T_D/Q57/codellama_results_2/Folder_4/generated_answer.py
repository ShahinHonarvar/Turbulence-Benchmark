
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Fill the temporary matrix with the values from the original matrix
            for k in range(matrix.shape[0]):
                for l in range(matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the temporary matrix is equal to 87
            if np.sum(temp_matrix) == 87:
                # If it is, add the submatrix to the list of submatrices with a particular sum
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with a particular sum
    return submatrices
