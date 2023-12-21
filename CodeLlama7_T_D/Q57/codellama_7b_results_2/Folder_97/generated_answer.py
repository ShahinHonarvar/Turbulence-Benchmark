
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over all possible starting positions for a submatrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Initialize the sum of the current submatrix
            current_sum = 0

            # Loop over all elements in the current submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Update the sum of the current submatrix
                    current_sum += matrix[k][l]

                    # Check if the sum of the current submatrix equals -617
                    if current_sum == -617:
                        # Add the current submatrix to the list of submatrices
                        submatrices.append(matrix[i:i + 2, j:j + 2])

            # Reset the sum of the current submatrix
            current_sum = 0

    # Return the list of all submatrices that satisfy the given condition
    return submatrices
