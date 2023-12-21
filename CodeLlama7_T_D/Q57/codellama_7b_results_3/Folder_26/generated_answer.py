
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over all possible starting positions of a submatrix in the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the current submatrix
            current_sum = 0

            # Iterate over all elements in the current submatrix
            for k in range(i, i + matrix.shape[0]):
                for l in range(j, j + matrix.shape[1]):
                    # Add the current element to the sum of the current submatrix
                    current_sum += matrix[k][l]

            # If the sum of the current submatrix is equal to the given sum, append it to the list of submatrices
            if current_sum == sum:
                submatrices.append(np.array([matrix[i:i + matrix.shape[0], j:j + matrix.shape[1]]]))

    # Return the list of all submatrices with the given sum, or an empty list if no such submatrix is found
    return submatrices
