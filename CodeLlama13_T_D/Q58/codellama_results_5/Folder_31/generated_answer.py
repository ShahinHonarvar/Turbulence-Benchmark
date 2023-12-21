
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Loop through each row in the matrix
    for i in range(matrix.shape[0] - n + 1):
        # Loop through each column in the matrix
        for j in range(matrix.shape[1] - n + 1):
            # Check if the submatrix with the current indices has n integers
            if np.count_nonzero(matrix[i:i+n, j:j+n]) == n**2:
                count += 1
    
    return count
