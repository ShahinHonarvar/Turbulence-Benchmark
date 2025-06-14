
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 126 integers each
    count = 0

    # Loop through all possible submatrices

    for i in range(matrix.shape[0] - 126 + 1):
        for j in range(matrix.shape[1] - 126 + 1):
            # Check if the current submatrix contains 126 integers each

            if all(all(matrix[k, l] == matrix[i + k, j + l]) for l in range(126)) for k in range(126)):
                count += 1

    # Return the count of all submatrices with 126 integers each

    return count
