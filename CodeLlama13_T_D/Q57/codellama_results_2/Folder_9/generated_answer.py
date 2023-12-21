
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the found submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Set the values of the temporary matrix based on the current row and column indices
            for k in range(temp_mat.shape[0]):
                for l in range(temp_mat.shape[1]):
                    temp_mat[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the temporary matrix is equal to -86
            if np.sum(temp_mat) == -86:
                # If yes, add the temporary matrix to the list of submatrices
                submatrices.append(temp_mat)
    
    # Return the list of all found submatrices
    return submatrices
