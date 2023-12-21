
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Check if matrix is valid
    if not isinstance(matrix, np.ndarray) or matrix.size == 0:
        raise ValueError("Matrix must be a non-empty NumPy array.")
    # Initialize output list
    submatrices = []

    # Iterate over all possible starting rows and columns of the submatrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the current submatrix from the original matrix
            submatrix = matrix[i:i+2, j:j+2]
            # Check if the sum of all integers in the submatrix is equal to 64
            if submatrix.sum() == 64:
                # Add the current submatrix to the output list
                submatrices.append(submatrix)

    return submatrices
