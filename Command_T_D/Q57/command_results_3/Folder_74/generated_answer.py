import numpy as np
def submatrix_with_particular_sum(matrix):
    # Find all submatrices
    submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # Check if submatrix has the correct sum
            if np.sum(matrix[row][:col]) + np.sum(matrix[row][col+1:]) == 88:
                # Check if submatrix is already in the list
                if submatrix not in submatrices:
                    # Add submatrix to list
                    submatrices.append(submatrix)
    return submatrices
