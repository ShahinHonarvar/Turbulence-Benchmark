
import numpy as np

def submatrix_with_particular_sum(mat):
    """
    Returns a list of all submatrices of the given matrix such that the sum
    of all integers in each submatrix equals 69. If no such submatrix is found,
    returns an empty list.
    """
    # Initialize an empty list to store the results
    result = []

    # Iterate over all possible starting indices for the top-left corner of the submatrix
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            # Initialize a 3x3 numpy array to store the submatrix
            sub = np.zeros((3, 3), dtype=int)

            # Fill the submatrix with the values from the original matrix
            for k in range(3):
                for l in range(3):
                    sub[k, l] = mat[i + k, j + l]

            # Check if the sum of all integers in the submatrix is 69
            if np.sum(sub) == 69:
                # If it is, add the submatrix to the result list
                result.append(sub)

    # Return the result list
    return result
