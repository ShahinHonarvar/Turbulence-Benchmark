
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 34
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix with sum 34
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Fill the temporary matrix with the submatrix starting from (i, j)
            for k in range(temp_matrix.shape[0]):
                for l in range(temp_matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the temporary matrix is 34
            if np.sum(temp_matrix) == 34:
                # If yes, add the submatrix to the list of submatrices with sum 34
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with sum 34
    return submatrices
