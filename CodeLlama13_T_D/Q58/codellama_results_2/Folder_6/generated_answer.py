
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 122 integers
    count = 0
    
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 122
            if matrix[i, j] == 122:
                # Increment the counter by 1
                count += 1
    
    return count
