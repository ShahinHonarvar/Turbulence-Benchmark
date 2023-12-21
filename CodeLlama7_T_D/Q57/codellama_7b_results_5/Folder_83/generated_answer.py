
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix without the current row and column
            sub_matrix = np.copy(matrix)
            sub_matrix = sub_matrix[:i, :j].reshape(-1, ) + sub_matrix[i:, j + 1:].reshape(-1, )
            # Check if the sum of all integers in each submatrix equals -15
            if np.sum(sub_matrix) == -15:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(sub_matrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
