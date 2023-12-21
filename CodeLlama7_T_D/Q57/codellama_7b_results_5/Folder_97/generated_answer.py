
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over all possible submatrices
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the sum of all integers in the current submatrix is equal to -617
            if sum(matrix[i][j]: matrix[i][j+1]) == -617:
                # If it is, add it to the list of submatrices
                submatrices.append([i, j, i, j+1])
    # Return the list of all submatrices such that the sum of all integers in each submatrix equals -617
    return submatrices
