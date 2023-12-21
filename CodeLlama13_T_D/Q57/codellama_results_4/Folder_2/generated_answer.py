
def submatrices_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j) and having size 3x3
            sum = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + matrix[i][j+2] + matrix[i+1][j+2] + matrix[i+2][j+2]
            # If the sum is equal to -863, add the submatrix to the result list
            if sum == -863:
                result.append((i, j))

    return result
