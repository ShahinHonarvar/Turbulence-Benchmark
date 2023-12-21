
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the current row
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the submatrix starting from the current element and spanning 3 rows and 3 columns
            subsum = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i][j+2] + matrix[i+1][j+2] + matrix[i+2][j+2]
            # If the sum is -15, add the submatrix to the list of submatrices
            if subsum == -15:
                submatrices.append((i, j))
    
    return submatrices
