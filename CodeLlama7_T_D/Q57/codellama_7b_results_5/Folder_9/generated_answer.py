
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with zeros
    submatrices = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    # Iterate over each element of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Initialize the sum variable to the current element
            sum = matrix[i][j]
            # Iterate over the remaining elements of the row and column
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Add the element to the sum if it is not the current element
                    if (k != i or l != j):
                        sum += matrix[k][l]
            # If the sum equals -86, add the submatrix to the list of submatrices
            if sum == -86:
                submatrices.append([])
                for k in range(i, len(matrix)):
                    submatrices[-1].append([])
                    for l in range(j, len(matrix[0])):
                        submatrices[-1][-1].append(matrix[k][l])
    # Return the list of all submatrices that have a sum equal to -86
    return submatrices
