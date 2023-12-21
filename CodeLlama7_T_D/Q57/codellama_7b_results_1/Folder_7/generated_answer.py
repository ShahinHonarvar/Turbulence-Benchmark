
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over all possible starting positions for the submatrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a counter for the sum of elements in the submatrix
            sum = 0

            # Loop over all elements in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Check if the element is out of bounds
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        # Add the element to the sum
                        sum += matrix[row][col]

            # If the sum equals -128, add the submatrix to the output list
            if sum == -128:
                submatrices.append((i, j))

    # Return the output list of all found submatrices
    return submatrices
