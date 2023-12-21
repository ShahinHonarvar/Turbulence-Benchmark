
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to 0
    count = 0
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 37
            if matrix[i][j] == 37:
                # Increment the count variable
                count += 1
    
    # Return the count variable
    return count
