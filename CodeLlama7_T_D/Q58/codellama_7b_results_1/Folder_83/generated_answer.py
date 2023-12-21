
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable
    count = 0

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]

        # Iterate over each column of the row
        for j in range(row.shape[0]):
            # Check if the current element is equal to 47
            if row[j] == 47:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 47 integers each
    return count
