
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Calculate the sum of all integers in the current row
        row_sum = np.sum(matrix[i])

        # If the current row sum is equal to the desired sum, add the entire row as a submatrix
        if row_sum == sum:
            submatrices.append(matrix[i])

    # Return the list of all submatrices that have the desired sum
    return submatrices
