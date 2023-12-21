
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((3, 3))
            
            # Fill the temporary matrix with the values from the original matrix
            temp_mat[:, :] = matrix[i:i+3, j:j+3]
            
            # Check if the sum of all integers in the current submatrix is -9
            if np.sum(temp_mat) == -9:
                # If it is, add the submatrix to the list of found submatrices
                submatrices.append(temp_mat)
    
    return submatrices
