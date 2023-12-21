
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    """
    Returns the count of all submatrices of the given matrix that contain n integers each.
    If no such submatrix is found, returns 0.
    """
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Loop over each row in the matrix
    for i in range(len(matrix)):
        # Loop over each column in the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary submatrix with size n x n
            temp_submatrix = np.zeros((n, n), dtype=int)
            
            # Fill the temporary submatrix with values from the original matrix
            for k in range(n):
                for l in range(n):
                    temp_submatrix[k, l] = matrix[i + k][j + l]
                    
            # Check if the temporary submatrix contains n integers
            if np.count_nonzero(temp_submatrix) == n ** 2:
                count += 1
                
    return count
