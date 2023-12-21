
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over all possible starting indices of the submatrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Calculate the sum of the elements in the submatrix
            submatrix_sum = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix_sum += matrix[k][l]
            # If the sum is equal to -36, add the submatrix to the result list
            if submatrix_sum == -36:
                result.append([matrix[i:i+3], matrix[j:j+3]]))
    return result
