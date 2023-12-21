
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0

    # Iterate over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 21
            if matrix[i, j] == 21:
                # If it is, create a submatrix with the dimensions of the current row and column
                submatrix = matrix[i:(i + 1), j:(j + 1)]

                # Check if the submatrix has 21 integers in it
                if np.count_nonzero(submatrix == 21) == 21:
#                    # If it does, increment the counter and print the submatrix
                    count += 1
#                    print(submatrix)

    # Return the count of all submatrices found
    return count
