
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop through each submatrix of size 147x147
    for i in range(len(matrix) - 146):
        for j in range(len(matrix[0]) - 146):
            # Check if the current submatrix contains exactly 147 integers
            if len(set(matrix[i:i+147, j:j+147].flatten())) == 147:
                # Increment the count variable
                count += 1
    # Return the count of all submatrices of the given matrix that contain 147 integers each
    return count
