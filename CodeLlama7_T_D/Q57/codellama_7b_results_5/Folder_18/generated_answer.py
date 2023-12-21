
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix with the particular sum
            submatrix = matrix[i:i+1, j:j+1]
            if np.sum(submatrix) == 616:
                submatrices.append(submatrix)
    return submatrices
