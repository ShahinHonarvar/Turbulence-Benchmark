
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 69
            if matrix[i, j] == 69:
                # If it is, increment the count by 1
                count += 1
                
    # Return the count of submatrices that contain 69 integers each
    return count
