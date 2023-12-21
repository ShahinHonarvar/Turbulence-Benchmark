
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 80 integers each
    count = 0

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 80
            if matrix[i][j] == 80:
                # Initialize a variable to keep track of the number of elements in the submatrix
                num_elements = 1

                # Iterate over each row and column in the submatrix
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        # Check if the current element is equal to 80
                        if matrix[k][l] == 80:
                            # Increment the number of elements in the submatrix
                            num_elements += 1

                # Check if the number of elements in the submatrix is equal to 80
                if num_elements == 80:
                    # Increment the counter for the number of submatrices with 80 integers each
                    count += 1

    # Return the count of all submatrices with 80 integers each
    return count
