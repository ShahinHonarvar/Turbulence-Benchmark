
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 21
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Find all possible submatrices with sum 21 starting from the current cell
            submatrices += find_submatrices(matrix, i, j, 21)

    return submatrices

def find_submatrices(matrix, row, col, target):
    # Base case: if the current cell is not part of any submatrix with sum 21
    if matrix[row][col] > target or matrix[row][col] < -target:
        return []

    # Recursive case: if the current cell is part of a submatrix with sum 21
    if matrix[row][col] == target:
        return [[row, col]]

    # Recursively find all possible submatrices with sum 21 in the rows above and columns to the left of the current cell
    submatrices = []
    for i in range(row):
        for j in range(col):
            submatrices += find_submatrices(matrix, i, j, target - matrix[row][col])

    # Add the current cell to each submatrix and return the result
    for submatrix in submatrices:
        submatrix.append([row, col])
    return submatrices
