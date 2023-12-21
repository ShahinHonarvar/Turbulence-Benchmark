
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 115 integers
    count = 0

    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0] - 114):
        for j in range(matrix.shape[1] - 114):
            # Check if the submatrix has 115 integers
            if sum([1 for x in matrix[i:i+115, j:j+115]]) == 115**2:
                # Increment the counter if the submatrix is found
                count += 1

    # Return the number of submatrices with 115 integers
    return count
