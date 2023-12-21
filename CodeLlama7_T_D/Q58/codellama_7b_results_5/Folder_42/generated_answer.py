
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop through each submatrix of size 193x193
    for i in range(matrix.shape[0] - 192):
        for j in range(matrix.shape[1] - 192):
            # Check if the current submatrix contains all 193 integers
            if (matrix[i:i + 193, j:j + 193] == 193).all():
                # Increment the count variable
                count += 1

    # Return the count of all submatrices of the given matrix that contain 193 integers each
    return count
