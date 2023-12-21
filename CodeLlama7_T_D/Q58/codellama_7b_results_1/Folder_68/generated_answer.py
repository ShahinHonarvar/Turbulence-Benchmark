
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 74 integers each to 0
    count = 0
    # Iterate over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to 74, add its value to the sum
            if matrix[i, j] == 74:
                sum += matrix[i, j]
    return count
