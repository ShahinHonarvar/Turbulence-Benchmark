
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over all possible starting positions for a submatrix
    for i in range(len(matrix) - 2 + 1):
        for j in range(len(matrix[0]) - 2 + 1):
            # Check if the sum of the integers in the submatrix equals -26
            if np.sum(matrix[i:i+3, j:j+3]) == -26:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i+3, j:j+3])
    return submatrices
