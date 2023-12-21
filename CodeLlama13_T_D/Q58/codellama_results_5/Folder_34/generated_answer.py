
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Loop through each row in the matrix
    for i in range(len(matrix)):
        # Loop through each column in the matrix
        for j in range(len(matrix[i])):
            # If the current element is equal to n, increment the counter
            if matrix[i][j] == n:
                count += 1
    
    # Return the number of submatrices with n integers
    return count
