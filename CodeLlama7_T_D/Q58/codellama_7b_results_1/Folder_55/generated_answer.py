
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 39 integers each
    count = 0

    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 39
            if matrix[i, j] == 39:
                # Initialize a variable to store the size of the submatrix
                size = 1

                # Iterate over the remaining elements in the row and column
                for k in range(i + 1, matrix.shape[0]):
                    for l in range(j + 1, matrix.shape[1]):
                        # Check if the current element is equal to 39
                        if matrix[k, l] == 39:
                            # Increment the size of the submatrix
                            size += 1

                # Check if the size of the submatrix is equal to 39
                if size == 39:
                    # Increment the counter for the number of submatrices with 39 integers each
                    count += 1

    # Return the count of all submatrices of the given matrix that contain 39 integers each
    return count
