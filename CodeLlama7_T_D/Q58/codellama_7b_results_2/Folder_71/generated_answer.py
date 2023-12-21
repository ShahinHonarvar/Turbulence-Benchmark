
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Get the current row as a list
        row = list(matrix[i])
        # Loop through each column of the row
        for j in range(len(row)):
            # Initialize a variable to keep track of the number of 78s found in the submatrix
            num_sevens = 0
            # Get the indices of the submatrix
            start_row = i - 2 if i > 2 else 0
            end_row = i + 2 if i + 2 < len(matrix) else len(matrix) - 1
            start_col = j - 2 if j > 2 else 0
            end_col = j + 2 if j + 2 < len(row) else len(row) - 1
            # Loop through each element of the submatrix
            for k in range(start_row, end_row + 1):
                for l in range(start_col, end_col + 1):
                    # Check if the current element is equal to 78
                    if matrix[k][l] == 78:
                        # Increment the number of 78s found in the submatrix
                        num_sevens += 1
            # If the number of 78s found in the submatrix is equal to 78, increment the count
            if num_sevens == 78:
                count += 1
    # Return the count of all submatrices of the given matrix that contain 78 integers each
    return count
