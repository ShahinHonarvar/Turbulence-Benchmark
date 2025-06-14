
import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of a given matrix with a particular sum.

    Args:
        matrix (numpy.ndarray): The input matrix.

    Returns:
        list[list]: A list of lists, where each inner list represents a submatrix that has the desired sum.
    """
    # Initialize an empty list to store the results
    result = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []

            # Loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k][l])

            # Check if the sum of all elements in the submatrix is 78
            if sum(temp) == 78:
                # If it is, add the submatrix to the results list
                result.append(temp)

    return result
