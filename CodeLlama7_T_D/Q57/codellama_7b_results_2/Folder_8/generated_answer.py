
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the submatrix
            subsum = np.sum(matrix[i:i + 2, j:j + 2])
            # If the sum is equal to the desired value, add the submatrix to the list
            if subsum == sum:
                submatrices.append(matrix[i:i + 2, j:j + 2])

    return submatrices
