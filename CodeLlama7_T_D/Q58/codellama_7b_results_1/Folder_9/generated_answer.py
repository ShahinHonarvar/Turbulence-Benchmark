
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 33 integers each
    count = 0

    # Loop over the rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 33
            if matrix[i][j] == 33:
                # If it is, increment the counter and break out of the loop
                count += 1
                break

    return count
