
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with a single element at (i, j)
            submatrix = np.array([[matrix[i][j]]]])
            # Loop over all elements of the matrix that are not at (i, j)
            for k in range(matrix.shape[0]):
                if k == i or k == j:
                    continue

                # Add the element at (k, l) to the submatrix
                submatrix = np.append(submatrix, [[matrix[k][l]]]], axis=1)
                for l in range(matrix.shape[1]):
                    if l == j:
                        continue

                    # Add the element at (m, n) to the submatrix
                    submatrix = np.append(submatrix, [[matrix[m][n]]]], axis=0)
                    # Check if the sum of all elements in the submatrix is equal to 40
                    if np.sum(submatrix) == 40:
                        # Add the submatrix to the result list
                        result.append(submatrix)
    return result
