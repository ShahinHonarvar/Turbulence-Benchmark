
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Getting the shape of the input matrix
    rows, cols = np.shape(matrix)

    count = 0

    # Iterating through rows
    for row_count in range(1, rows+1):
        # Iterating through columns
        for col_count in range(1, cols+1):
            # Checking all possible submatrices of varying size
            for row_start in range(rows - row_count + 1):
                for col_start in range(cols - col_count + 1):
                    # If the count of integers in submatrix is 57
                    if (row_count * col_count == 57):
                        count += 1
                        
    # Return the count
    return count
