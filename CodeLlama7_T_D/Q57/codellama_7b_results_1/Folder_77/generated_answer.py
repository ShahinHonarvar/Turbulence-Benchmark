
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Find all submatrices of the given matrix
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            submatrices.append(np.array([matrix[k][l] for k in range(i, i + 2) for l in range(j, j + 2)])))
    # Filter the submatrices to only those that have a sum of -336
    filtered_submatrices = []
    for submatrix in submatrices:
        if np.sum(submatrix) == -336:
            filtered_submatrices.append(submatrix)
    return filtered_submatrices
