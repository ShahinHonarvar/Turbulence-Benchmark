
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 118
            if matrix[i, j] == 118:
                # Increment the count variable by 1
                count += 1
    
    # Return the final count
    return count
