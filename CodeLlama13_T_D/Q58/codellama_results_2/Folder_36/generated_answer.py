
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 131 integers
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the current row
        for j in range(len(matrix[i])):
            # Check if the element at (i, j) is 131
            if matrix[i][j] == 131:
                # If it is, increment the counter by 1
                count += 1
    
    # Return the counter value as the result of the function
    return count
