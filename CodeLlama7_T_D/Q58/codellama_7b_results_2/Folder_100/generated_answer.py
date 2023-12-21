
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with a size of 1x1
            temp_submatrix = np.array([[matrix[i,j]]]])

            # Loop over each row of the matrix
            for k in range(matrix.shape[0] - i + 1):
                # Loop over each column of the matrix
                for l in range(matrix.shape[1] - j + 1):
                    # If the current submatrix contains 10 integers, increment the count variable
                    if temp_submatrix.size == 10:
                        count += 1

                    # Add the current value to the temporary submatrix
                    temp_submatrix = np.append(temp_submatrix, matrix[i + k - 1, j + l - 1], axis=None)

    # Return the count variable
    return count
