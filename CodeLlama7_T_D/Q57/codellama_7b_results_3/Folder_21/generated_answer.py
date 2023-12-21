
import numpy as np

def submatrix_with_particular_sum(A):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(A.shape[0]):
        # Iterate over each column of the matrix
        for j in range(A.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix = []

            # Iterate over each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the element to the list
                    submatrix.append(A[k][l]])

            # Check if the sum of all elements in the submatrix is equal to -936
            if sum(submatrix) == -936:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
