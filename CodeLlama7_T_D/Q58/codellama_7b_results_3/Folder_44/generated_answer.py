
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the submatrix has 191 integers
            if (matrix[i:i+2, j:j+2] == 191).all():
                # Increment the count variable
                count += 1

    # Return the count of all submatrices with 191 integers each
    return count
