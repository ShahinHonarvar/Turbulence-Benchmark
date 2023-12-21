
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to 4, increase the count by 1
            if matrix[i][j] == 4:
                count += 1
    # Return the count of all submatrices that contain 4 integers each
    return count
