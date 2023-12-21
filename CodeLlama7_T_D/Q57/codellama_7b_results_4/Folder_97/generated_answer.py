
import numpy as np

def submatrix_with_particular_sum(A):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix A
    for i in range(A.shape[0]):
        # Iterate over each column of the matrix A
        for j in range(A.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Iterate over each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the current element to the sum of the submatrix
                    submatrix_sum += A[row, col]

            # Check if the sum of the submatrix is equal to -617
            if submatrix_sum == -617:
                # If the sum is equal to -617, add the submatrix to the list of submatrices
                submatrices.append(A[i:i + 3, j:j + 3])

    # Return the list of all submatrices that have a sum of -617
    return submatrices
