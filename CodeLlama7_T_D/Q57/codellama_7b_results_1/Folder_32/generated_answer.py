
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Get a reference to the current element
            element = matrix[i][j]

            if element == sum:
                # If the element is equal to the sum, add the submatrix to the list
                submatrices.append(matrix[i:i+1, j:j+1])

    return submatrices
