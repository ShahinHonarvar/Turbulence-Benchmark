
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 48 integers each to 0
    count = 0
    # Loop over all possible starting positions of a submatrix in the given matrix
    for i in range(matrix.shape[0] - 47):
        for j in range(matrix.shape[1] - 47):
            # Initialize a variable to keep track of the number of integers in the current submatrix
            num_ints = 0
            # Loop over all rows and columns of the current submatrix
            for row in range(i, i + 48):
                for col in range(j, j + 48):
                    # Increment the number of integers in the current submatrix if the value at the current position is equal to 48
                    num_ints += (matrix[row, col] == 48)
            # If the number of integers in the current submatrix is equal to 48, increment the count of submatrices with 48 integers each
            if num_ints == 48:
                count += 1
    return count
