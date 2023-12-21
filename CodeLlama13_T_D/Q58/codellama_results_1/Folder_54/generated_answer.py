
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over the rows of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over the columns of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to n
            if matrix[i,j] == n:
                # Increment the count variable
                count += 1
    
    # Return the count variable
    return count
