
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 104 integers each
    count = 0

    # Loop over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a variable to keep track of the number of integers in the submatrix
            num_ints = 0

            # Loop over all elements in the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # If the element is not a zero, increment the number of integers in the submatrix
                    if matrix[k][l] != 0:
                        num_ints += 1

            # If the number of integers in the submatrix is equal to 104, increment the counter
            if num_ints == 104:
                count += 1

    # Return the count of all submatrices with 104 integers each
    return count
