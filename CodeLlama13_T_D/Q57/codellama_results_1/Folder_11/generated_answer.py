
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j) and having size 7x7
            sub_sum = np.sum(matrix[i:i+7,j:j+7])

            # If the sum is equal to 38, add the submatrix to the result list
            if sub_sum == 38:
                result.append(matrix[i:i+7,j:j+7])

    return result
