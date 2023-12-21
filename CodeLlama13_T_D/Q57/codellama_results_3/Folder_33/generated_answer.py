
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over all possible starting indices of the submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of integers in the submatrix with the current starting indices
            sum_of_submatrix = np.sum(matrix[i:i+2,j:j+2])

            # If the sum is equal to -811, add the submatrix to the result list
            if sum_of_submatrix == -811:
                result.append(matrix[i:i+2,j:j+2])

    return result
