
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with zeros
    submatrices = [[0 for _ in range(len(row))] for row in matrix]
    # Loop over each element in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to -44
            if matrix[i][j] == -44:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append([row[:j] + row[j+1:] for row in matrix])
    # Return the list of submatrices with the sum equal to -44
    return submatrices
