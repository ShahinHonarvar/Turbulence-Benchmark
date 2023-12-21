
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Iterate over all possible submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Extract the submatrix starting from (i,j) and ending at (i+2,j+2)
            submatrix = matrix[i:i+3, j:j+3]
            # Check if the sum of all elements in the submatrix is equal to 432
            if np.sum(submatrix) == 432:
                return [submatrix]
    # If no such submatrix is found, return an empty list
    return []
