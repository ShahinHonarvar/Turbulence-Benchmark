
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 29 integers
    count = 0

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary submatrix with dimensions 3x3
            temp_submatrix = np.zeros((3, 3), dtype=int)

            # Populate the temporary submatrix with the values from the original matrix
            for k in range(3):
                for l in range(3):
                    temp_submatrix[k][l] = matrix[i+k-1][j+l-1]

            # Check if the temporary submatrix contains 29 integers
            if np.sum(temp_submatrix) == 29:
                count += 1

    return count
