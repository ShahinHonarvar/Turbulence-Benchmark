
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0

    # Iterate over each element in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to 185, increment the counter
            if matrix[i,j] == 185:
                count += 1

    # Return the count of submatrices found
    return count
