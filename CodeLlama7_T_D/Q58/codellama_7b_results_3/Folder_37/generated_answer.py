
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over each row of the matrix
    for i in range(matrix.shape[0] - 63):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1] - 63):
            # Check if the submatrix has 64 integers
            if np.all(matrix[i:i+64, j:j+64] == 1)):
                # Increment the count variable
                count += 1

    # Return the count variable
    return count
