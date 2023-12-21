
import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 15, or an empty list if no such submatrix is found.

    Parameters:
        matrix (numpy.ndarray[int]): The two-dimensional numpy matrix of integers.

    Returns:
        list[tuple]: A list of tuples representing the submatrices of the given matrix with the sum equal to 15. Each tuple contains two elements: the starting indices of the submatrix (row, column) and the ending indices (row, column).
    """
    # Initialize an empty list to store the results
    results = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix indices
            temp = [(i, j)]

            # Loop through each row and column after (i, j)
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # If the sum of the submatrix is equal to 15, add it to the results list
                    if np.sum(matrix[temp]) == 15:
                        results.append(temp)
                    # Add the current indices to the temporary list and continue iterating
                    temp.append((k, l))

    return results
