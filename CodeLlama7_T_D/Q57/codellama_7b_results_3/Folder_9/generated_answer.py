
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Iterate over all possible rows and columns
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the submatrix
            submatrix_sum = matrix[i:i+2, j:j+2].sum()
            # If the sum is equal to -86, add the submatrix to the result list
            if submatrix_sum == -86:
                result.append(matrix[i:i+2, j:j+2])
    return result
