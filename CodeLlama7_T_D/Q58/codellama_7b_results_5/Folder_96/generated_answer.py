
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 20 integers each
    count = 0

    # Loop over all possible starting positions for a submatrix
    for i in range(len(matrix) - 19):
        for j in range(len(matrix[i]) - 19):
            # Check if the current submatrix has 20 integers each
            if all([len(row) == 20 for row in matrix[i:i+20]]) and \
                    all([len(column) == 20 for column in matrix[:, j:j+20]])):
                # Increment the count of submatrices with 20 integers each
                count += 1

    return count
