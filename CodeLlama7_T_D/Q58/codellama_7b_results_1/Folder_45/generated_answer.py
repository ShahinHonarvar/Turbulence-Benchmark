
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0

    # Iterate over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 28
            if matrix[i][j] == 28:
                # Initialize a flag to indicate whether a submatrix has been found
                found_submatrix = False

                # Iterate over each possible size of the submatrix
                for k in range(1, matrix.shape[0] - i + 1):
                    for l in range(1, matrix.shape[1] - j + 1):
                        # Check if the current submatrix has 28 integers
                        if np.sum(matrix[i:i+k, j:j+l]) == 28:
                            # Increment the counter for the number of submatrices found
                            count += 1

                            # Set the flag to indicate that a submatrix has been found
                            found_submatrix = True

                # Check if a submatrix has been found and increment the counter accordingly
                if found_submatrix:
                    count += 1

    # Return the count of all submatrices of the given matrix that contain 28 integers each
    return count
