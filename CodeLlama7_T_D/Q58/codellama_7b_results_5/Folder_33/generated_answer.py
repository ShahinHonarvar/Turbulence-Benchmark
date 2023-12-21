
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 118 integers each to 0
    count = 0
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a counter variable to keep track of the number of integers in the submatrix
            counter = 0
            # Loop through each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Check if the current element is a 1 or an integer in the range [0, 118)
                    if matrix[k][l] == 1 or (matrix[k][l] >= 0 and matrix[k][l] < 118)):
                        # Increment the counter variable
                        counter += 1

            # Check if the current submatrix has 118 integers each
            if counter == 9:
                # Increment the count of submatrices with 118 integers each
                count += 1

    return count
