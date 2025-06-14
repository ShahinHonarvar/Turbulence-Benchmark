
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []

    # Iterate over all possible rows and columns
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Calculate the sum of the elements in the submatrix
            sum = np.sum(matrix[i][j]:))
            if sum == 416:
                # Add the submatrix to the output list
                output.append(matrix[i][j])

    return output
