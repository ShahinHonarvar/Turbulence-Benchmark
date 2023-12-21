
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a count variable to keep track of the number of submatrices with n numbers
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((n, n), dtype=int)
            
            # Fill the temporary matrix with the values from the original matrix
            for k in range(n):
                for l in range(n):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the temporary matrix contains n integers
            if np.all(temp_matrix == 1):
                count += 1
    
    return count
