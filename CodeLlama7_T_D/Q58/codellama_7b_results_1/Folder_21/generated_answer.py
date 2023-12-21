
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 139 integers each
    count = 0
    # Iterate over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is 139, add the corresponding submatrix to the count
            if matrix[i][j] == 139:
                count += 1

    return count
