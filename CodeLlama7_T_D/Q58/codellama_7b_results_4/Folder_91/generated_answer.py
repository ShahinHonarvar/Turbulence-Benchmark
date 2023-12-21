
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 5 integers each
    count = 0

    # Loop over all possible starting positions in the matrix
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 4):
            # Check if there are 5 consecutive integers in the submatrix
            if np.all(np.diff(matrix[i:i+5, j:j+5]) == 1)):
                # Increment the counter for each valid submatrix
                count += 1

    # Return the number of submatrices with 5 integers each
    return count
