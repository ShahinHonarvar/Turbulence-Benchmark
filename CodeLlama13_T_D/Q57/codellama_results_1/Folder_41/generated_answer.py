
def submatrix_with_particular_sum(mat):
    # Initialize a list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(len(mat)):
        # Iterate over each column of the matrix
        for j in range(len(mat[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j) and extending to the end of the matrix
            curr_sum = 0
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    curr_sum += mat[k][l]

            # If the sum is equal to -26, add the submatrix to the result list
            if curr_sum == -26:
                result.append((i, j))

    return result
