
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Check if the row contains the integer 127
        if 127 in row:
            # Increment the count variable
            count += 1
    # Return the count variable
    return count
