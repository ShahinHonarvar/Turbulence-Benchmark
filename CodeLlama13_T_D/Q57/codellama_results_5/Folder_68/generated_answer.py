
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary submatrix with dimensions 3x3
            temp_submatrix = np.zeros((3, 3), dtype=int)

            # Fill the temporary submatrix with values from the original matrix
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if k >= 0 and k < len(matrix) and l >= 0 and l < len(matrix[0]):
                        temp_submatrix[k - i + 1][l - j + 1] = matrix[k][l]

            # Calculate the sum of all integers in the temporary submatrix
            submatrix_sum = np.sum(temp_submatrix)

            # If the sum is equal to 3, add the submatrix to the results list
            if submatrix_sum == 3:
                results.append(temp_submatrix)

    return results
