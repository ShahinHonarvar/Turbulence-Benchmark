
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0

    # Iterate over each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If the element is 1, increment the count
            if matrix[i][j] == 1:
                count += 1

    return count
