
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 126 integers
    count = 0

    # Loop through each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If the current element is equal to 1, increment the counter
            if matrix[i][j] == 1:
                count += 1

            # If the counter is equal to 126, add the submatrix to the list of found submatrices
            if count == 126:
                found_submatrices.append(matrix[i-125:i+1, j-125:j+1])

    # Return the number of found submatrices
    return len(found_submatrices)
