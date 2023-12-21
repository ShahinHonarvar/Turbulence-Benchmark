
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Extract the submatrix from the given matrix
            submatrix = np.array([row[j] for row in matrix])

            if sum(submatrix) == -336:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    return submatrices
