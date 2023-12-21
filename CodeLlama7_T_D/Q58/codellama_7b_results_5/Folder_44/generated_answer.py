
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 191 integers each
    count = 0

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the current row and column
            submatrix = matrix[i:i+1, j:j+1]
            # Check if the submatrix has 191 integers each
            if np.all(submatrix == 191):
                # Increment the count of submatrices with 191 integers each
                count += 1

    # Return the count of submatrices with 191 integers each
    return count
