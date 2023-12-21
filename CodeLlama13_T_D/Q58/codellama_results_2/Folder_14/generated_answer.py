
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to 0
    count = 0
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 84
            if matrix[i, j] == 84:
                # If it is, increment the count by 1
                count += 1
    
    # Return the final count
    return count
