
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize an empty list to store the counts of all submatrices
    submatrices = []

    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((8, 8), dtype=int)

            # Fill the temporary matrix with elements from the original matrix
            for k in range(temp_matrix.shape[0]):
                for l in range(temp_matrix.shape[1]):
                    temp_matrix[k, l] = matrix[i + k, j + l]

            # Check if the temporary matrix contains 88 integers
            if np.sum(temp_matrix) == 88:
                submatrices.append((i, j))

    return len(submatrices)
