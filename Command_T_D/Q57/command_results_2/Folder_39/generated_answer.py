import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    if matrix[0][0] != 0:
        matrix[0][0] = 0
    # Add the first row of the given matrix to the list of submatrices
    submatrices = [(matrix[0].tolist())]
    # Do the dynamic programming
    for i in range(1, matrix.shape[0]):
        for j in range(1, matrix.shape[1]):
            # If the submatrix i, j does not equal 66, do nothing
            if matrix[i][j] == 66:
                # Add the submatrix i, j to the list of submatrices
                submatrices.append((matrix[i].tolist()))
                # Recursively call the function with the submatrix i, j
                submatrices += submatrix_with_particular_sum(matrix[i])
    # If the list of submatrices is empty, return an empty list
    return submatrices
