
import numpy as np

def submatrix_with_particular_sum(matrix, target_sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the current submatrix
            current_sum = matrix[i:i+2, j:j+2].sum()
            if current_sum == target_sum:
                # If the current submatrix has the desired sum, add it to the list
                submatrices.append(matrix[i:i+2, j:j+2])
    return submatrices
