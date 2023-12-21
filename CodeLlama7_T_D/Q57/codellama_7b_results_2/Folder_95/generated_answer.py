
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum equal to 19
    submatrices = []
    # Iterate over all possible submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the submatrix
            submatrix_sum = matrix[i:i+2, j:j+2].sum()
            # If the sum is equal to 19, add the submatrix to the list
            if submatrix_sum == 19:
                submatrices.append(matrix[i:i+2, j:j+2])
    return submatrices
