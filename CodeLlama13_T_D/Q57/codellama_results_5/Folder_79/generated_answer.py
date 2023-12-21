
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Flatten the matrix and calculate the sum of all elements
    flat_matrix = np.reshape(matrix, (-1,))
    total_sum = flat_matrix.sum()

    # Create a set to store the indices of submatrices with the desired sum
    submatrix_indices = set()

    # Iterate over all possible submatrices and calculate their sums
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of the current submatrix
            submatrix_sum = np.reshape(matrix[i:,j:], (-1,)).sum()

            # If the sum is equal to -47, add the indices to the set
            if submatrix_sum == -47:
                submatrix_indices.add((i, j))

    # Convert the set to a list and return it
    return list(submatrix_indices)
