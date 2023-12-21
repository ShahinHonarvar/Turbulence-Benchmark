
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Iterate over all possible starting indices
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            # Calculate the sum of elements in the submatrix
            sum_of_elements = 0
            for k in range(i, j + 1):
                sum_of_elements += matrix[k][j]
            # If the sum is equal to -87, add the submatrix to the result list
            if sum_of_elements == -87:
                result.append([matrix[i:j + 1], matrix[i:j + 1]]))
    return result
