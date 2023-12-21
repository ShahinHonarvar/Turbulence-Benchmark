
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Loop through each column of the row
        for j in range(row.size):
            # Check if the current element is equal to 37
            if row[j] == 37:
                # If it is, increment the count variable
                count += 1

    # Return the final count
    return count
