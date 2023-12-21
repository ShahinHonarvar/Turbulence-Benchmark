
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count variable
    count = 0
    
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Check if the submatrix has 144 integers
            if sum(matrix[i:i+n, j:j+n]) == 144:
                # Increment the count variable
                count += 1
                
    # Return the count of all submatrices that contain 144 integers each
    return count
