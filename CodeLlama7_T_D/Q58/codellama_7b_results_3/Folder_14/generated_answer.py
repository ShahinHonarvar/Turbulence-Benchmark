
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter variable
    count = 0

    # Iterate over all possible submatrices of the given matrix
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            # Check if the current submatrix contains 84 integers each
            if (matrix[i:j, :].sum() == 84 * (j - i)) and (matrix[:, i:j].sum() == 84 * (j - i))):
                # Increment the counter variable if a valid submatrix is found
                count += 1

    # Return the count of all valid submatrices that contain 84 integers each
    return count
