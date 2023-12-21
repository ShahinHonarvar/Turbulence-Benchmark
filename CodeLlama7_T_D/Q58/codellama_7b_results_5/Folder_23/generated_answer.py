
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 69 integers each
    count = 0
    # Loop over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 69
            if matrix[i][j] == 69:
                # Initialize a flag variable to keep track of whether we have found a submatrix with 69 integers each
                flag = False

                # Loop over the rest of the rows and columns in the matrix
                for k in range(i, matrix.shape[0]):
                    for l in range(j, matrix.shape[1]):
                        # Check if the current element is equal to 69
                        if matrix[k][l] == 69:
                            # Increment the count of submatrices with 69 integers each
                            count += 1

                            # Set the flag variable to True since we have found a submatrix with 69 integers each
                            flag = True

                            # Break out of the inner loop since we do not need to check any more elements in the current row or column
                            break

                        # If the flag variable is still False, then we have not found a submatrix with 69 integers each yet
                        if not flag:
                            # Break out of the outer loop since we do not need to check any more elements in the current row or column
                            break

    # Return the count of submatrices with 69 integers each
    return count
