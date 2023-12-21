
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is 90
            if matrix[i][j] == 90:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 90 integers each
    return count
