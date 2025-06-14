
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Get the current row of the matrix
        row = matrix[i]

        # Loop through each column of the matrix
        for j in range(len(row)):
            # Get the current column of the matrix
            col = row[j]

            # Check if the submatrix contains 90 integers
            if len(col) == 90:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 90 integers each
    return count
