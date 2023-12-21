
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_mat = np.zeros((64, 64))
            
            # Fill the temporary matrix with the values from the main matrix
            for k in range(i, i+64):
                for l in range(j, j+64):
                    temp_mat[k-i][l-j] = matrix[k][l]
            
            # Check if the temporary matrix contains 64 integers each
            if np.sum(temp_mat == 0) == 0:
                count += 1
    
    return count
