
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find all submatrices that have a sum equal to 40
            if np.sum(matrix[i:, j]) == 40:
                result.append(matrix[i:, j])

    # Return the list of all submatrices with a sum equal to 40
    return result
