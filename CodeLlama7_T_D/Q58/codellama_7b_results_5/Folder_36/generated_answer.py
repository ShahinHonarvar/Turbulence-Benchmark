
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 131 integers each to 0
    count = 0
    # Loop over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a counter for the current submatrix with 131 integers each
            curr_count = 0
            # Loop over all rows and columns in the matrix
            for k in range(i, i + 131):
                for l in range(j, j + 131):
                    # Increment the counter if the current element is non-zero
                    if matrix[k][l] != 0:
                        curr_count += 1
            # If the current submatrix with 131 integers each has at least one non-zero element, increment the count of submatrices with 131 integers each
            if curr_count > 0:
                count += 1

    return count
