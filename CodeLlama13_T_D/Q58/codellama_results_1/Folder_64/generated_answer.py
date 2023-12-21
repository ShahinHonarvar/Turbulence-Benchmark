
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a count variable to keep track of submatrices with n integers
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is equal to n
            if matrix[i][j] == n:
                # If it is, increment the count variable
                count += 1
    
    # Return the final count of submatrices with n integers
    return count
