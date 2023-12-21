
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Calculate the sum of all integers in each submatrix
            submatrix_sum = np.sum(matrix[i][j]:))

            if submatrix_sum == 398:
                # Append the submatrix to the list
                submatrices.append(matrix[i][j])

    return submatrices
