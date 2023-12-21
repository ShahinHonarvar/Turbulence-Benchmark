
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices with 16 integers each
    count = 0

    # Loop through each row and column of the matrix

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is a submatrix of size 4x4

            if len(matrix[i][j]) == 16:
                count += 1

    return count
