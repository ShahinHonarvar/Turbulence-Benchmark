
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 115
            if matrix[i,j] == 115:
                # Increment the counter by one
                count += 1
    
    return count
