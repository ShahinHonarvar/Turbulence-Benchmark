
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 83 integers
    count = 0
    
    # Loop through each row in the matrix
    for i in range(len(matrix)):
        # Loop through each column in the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((83, 83))
            
            # Fill the temporary matrix with the values from the original matrix
            for k in range(i, i+83):
                for l in range(j, j+83):
                    temp_mat[k-i][l-j] = matrix[k][l]
            
            # Check if all elements in the temporary matrix are non-zero
            if np.all(temp_mat != 0):
                count += 1
    
    return count
