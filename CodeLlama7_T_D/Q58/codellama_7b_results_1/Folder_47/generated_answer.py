
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 90 integers each
    count = 0
    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a counter variable to keep track of the number of integers in the submatrix
            counter = 0
            # Iterate over the rows and columns of the matrix within the current submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Check if the current element is a integer
                    if type(matrix[row][col]) == int:
                        # Increment the counter variable
                        counter += 1

            # Check if the counter variable has reached the desired value of 90 integers in the submatrix
            if counter == 90:
                # Increment the count of submatrices with 90 integers each
                count += 1

    return count
