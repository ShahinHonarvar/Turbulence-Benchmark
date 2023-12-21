
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the indices of the elements in the current row that sum to -13
        indices = np.where(matrix[i, :].sum() == -13)
        # If any indices were found, add the submatrix to the list
        if len(indices[0]) > 0:
            submatrices.append(matrix[i, indices[0][0]]))
    return submatrices
